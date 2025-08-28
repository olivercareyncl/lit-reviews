import pandas as pd
from pathlib import Path
from src.enrich_links import fetch_doi_from_crossref

class DummyResp:
    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self._payload = payload or {"message": {"items": [{"DOI": "10.1234/abc"}]}}
    def json(self):
        return self._payload
    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception("HTTP error")

class DummySess:
    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self.payload = payload
        self.headers = {}
    def get(self, *args, **kwargs):
        return DummyResp(self.status_code, self.payload)

def test_fetch_doi_success():
    sess = DummySess()
    doi = fetch_doi_from_crossref("Some Title", sess=sess)
    assert doi == "10.1234/abc"

def test_fetch_doi_no_items():
    sess = DummySess(payload={"message": {"items": []}})
    doi = fetch_doi_from_crossref("Some Title", sess=sess)
    assert doi == "N/A"

def test_fetch_doi_bad_title():
    assert fetch_doi_from_crossref("", sess=DummySess()) == "N/A"
