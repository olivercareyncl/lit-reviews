"""
Enrich DOIs/links from titles using the Crossref API.

- Input:  data/raw/all_articles.csv
- Output: data/interim/all_articles_enriched.csv
- Resumes if output exists
- Polite: sets Crossref User-Agent with mailto (use env CROSSREF_MAILTO)
"""

from __future__ import annotations
import os
import time
from pathlib import Path
from typing import Optional, Dict

import pandas as pd
import requests

RAW_PATH = Path("data/raw/all_articles.csv")
OUT_PATH = Path("data/interim/all_articles_enriched.csv")

SAVE_EVERY = int(os.getenv("ENRICH_SAVE_EVERY", "50"))
RATE_LIMIT_SECONDS = float(os.getenv("ENRICH_RATE_LIMIT_SECONDS", "1"))
MAX_RETRIES = int(os.getenv("ENRICH_MAX_RETRIES", "3"))
MAILTO = os.getenv("CROSSREF_MAILTO", "your.email@example.com")  # set in .env

def _session() -> requests.Session:
    s = requests.Session()
    # Crossref asks for mailto in UA: https://api.crossref.org/swagger-ui/index.html
    s.headers.update({
        "User-Agent": f"lit-reviews-enricher/0.1 (mailto:{MAILTO})"
    })
    return s

def fetch_doi_from_crossref(title: str, sess: Optional[requests.Session] = None) -> str:
    """Return a DOI string or 'N/A'."""
    if not title or str(title).strip().lower() in ("nan", "none"):
        return "N/A"

    sess = sess or _session()
    url = "https://api.crossref.org/works"
    params = {"query.bibliographic": title, "rows": 1}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = sess.get(url, params=params, timeout=15)
            # Backoff on rate-limit or server errors
            if r.status_code in (429, 500, 502, 503, 504):
                sleep_s = min(2 ** attempt, 20)
                time.sleep(sleep_s)
                continue
            r.raise_for_status()
            items = r.json().get("message", {}).get("items", [])
            if items:
                doi = items[0].get("DOI")
                return doi or "N/A"
            return "N/A"
        except requests.RequestException:
            if attempt == MAX_RETRIES:
                return "N/A"
            time.sleep(min(2 ** attempt, 20))
    return "N/A"

def enrich_csv(
    input_path: Path = RAW_PATH,
    output_path: Path = OUT_PATH,
    rate_limit_seconds: float = RATE_LIMIT_SECONDS,
    save_every: int = SAVE_EVERY,
) -> None:
    # Ensure directories exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Load input
    try:
        df = pd.read_csv(input_path, encoding="ISO-8859-1")
    except Exception as e:
        raise RuntimeError(f"Failed to load {input_path}: {e}") from e

    # Determine resume point
    if output_path.exists():
        enriched_df = pd.read_csv(output_path, encoding="ISO-8859-1")
        start_idx = len(enriched_df)
        if start_idx < len(df):
            # Extend enriched_df to match df length if needed (schema safety)
            if enriched_df.shape[1] < df.shape[1]:
                enriched_df = df.copy()
                start_idx = 0
    else:
        enriched_df = df.copy()
        start_idx = 0

    # Ensure DOI column exists
    if "DOI" not in enriched_df.columns:
        enriched_df["DOI"] = ""

    sess = _session()

    # Main loop
    total = len(df)
    for i in range(start_idx, total):
        title = str(df.loc[i, "Title"]) if "Title" in df.columns else ""
        existing_doi = str(enriched_df.loc[i, "DOI"]) if "DOI" in enriched_df.columns else ""
        existing_doi = (existing_doi or "").strip().lower()

        if existing_doi in ("", "nan", "n/a"):
            print(f"🔎 [{i+1}/{total}] Searching DOI for: {title[:80]}...")
            doi = fetch_doi_from_crossref(title, sess=sess)
            enriched_df.loc[i, "DOI"] = doi
            time.sleep(rate_limit_seconds)
        else:
            print(f"✅ [{i+1}/{total}] DOI exists. Skipping.")

        if (i + 1) % save_every == 0 or i == total - 1:
            # Save progress
            enriched_df.to_csv(output_path, index=False, encoding="ISO-8859-1")
            print(f"💾 Progress saved at row {i + 1}")

if __name__ == "__main__":
    enrich_csv()
