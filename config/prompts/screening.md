# Task
Decide whether to INCLUDE a study in an evidence map based on the criteria below. You MUST return JSON that conforms to the provided JSON Schema (no extra keys).

# Scope to screen
- Source text may include: title, abstract, metadata, and/or excerpts from the full text.

# MUST INCLUDE — ALL of the following:
1) **Setting:** NHS or UK health & social care **or** community health settings (hospitals, primary care, patients’ homes).
2) **Cash-releasing benefits:** Intervention claims **cashable** savings (NOT just time/efficiency). Evidence should meet these tests:
   - *Direct budget reduction is explicit* (e.g., reduced departmental spend/budget; “cashable/cash-releasing”).
   - *Clear route to remove cash from baseline* (which budget line/owner reduces; e.g., lower contract price, headcount removed, estate exited).
   - *Robust calculation vs baseline + counterfactual* (baseline cost, “what would have happened otherwise”, and outturn are stated).
   - *Realised in-year (or time-phased) and sustainable* (captured in the year realised; recurring if claimed).
   - *Net, single, auditable* (net of costs; no double count; defensible to audit/assurance with traceable calc/evidence pack).
   - *No hidden cost shifting or performance harm* (no new costs elsewhere; no degraded outcomes/performance).
3) **Aligns to ≥1 NHS Three Shifts** (choose one or more):
   - **Community (Hospital → Community)**: shifting care out of hospital into neighbourhood/community; expanded community pharmacy; urgent care at home; shifting spend to out-of-hospital.
   - **Digital (Analogue → Digital)**: digital solutions replacing analogue/admin; NHS App expansion; unified patient record; continuous monitoring; AI/admin reduction.
   - **Prevention (Sickness → Prevention)**: anticipatory/preventive care; precision medicine for early risk ID; proactive neighbourhood care.
4) **Comparator present** (e.g., business as usual/standard care/do nothing/no change).
5) **Primary outcomes include costs** (e.g., cost reduction) and/or change in outcome/impact.
6) **Publication type:** peer-reviewed or grey literature (reports, dissertations, conference abstracts).
7) **Language & dates:** English; published 2019–2025 (inclusive).
8) **Geography:** UK setting or applied to the UK (NHS; England/Wales/Northern Ireland/Scotland).

# MUST EXCLUDE — ANY of the following:
- Outside health/social-care settings.
- No cost reduction or cash-releasing benefit.
- Not aligned to any of the Three Shifts.
- No cost-related outcomes.
- Predatory/non-peer-reviewed journals without credible grey-lit provenance.
- Published before 2019 or after 2025.
- Non-UK or non-English.
- Protocols, editorials, commentaries only (no empirical results).

# Evidence requirement
For every key decision, extract short **verbatim evidence spans** from the text (10–40 words each, up to 5) that justify your decision (e.g., lines that show “cash-releasing”, comparators, setting, dates).

# Output format
Return **ONLY** JSON compliant with the provided schema (no prose, no markdown).
