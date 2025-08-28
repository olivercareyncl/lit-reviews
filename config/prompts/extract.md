# Task
Extract structured metadata for an **included** study (evidence map). Follow the JSON Schema EXACTLY (no extra keys). Provide short verbatim evidence spans for auditable fields.

# Normalisation rules
- `evidence_map_shift`: one or more of ["community","digital","prevention"].
- `time_horizon`: map to one of ["≤1 month","3–12 months",">12–36 months",">3 years","Unknown"] based on follow-up/realisation period.
- `literature_type`: one of ["peer_reviewed","report","dissertation","conference_abstract","other_grey"].
- `uk_setting`: true if NHS/UK context is explicit.
- `comparison_group_present`: true if BAU/no-intervention/standard care/do nothing/no care is used.
- `primary_outcomes`: include at least one cost metric if present (e.g., total cost, cost per patient, budget line reduction).

# Evidence requirement
Provide `evidence_spans` (10–40 words, up to 8) with labels indicating which field(s) they support (e.g., "cash_releasing", "comparator", "uk_setting", "cost_outcome", "shift").

# Output
Return ONLY JSON (no prose).
