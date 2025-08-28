import json
from jsonschema import validate
from src.schemas import screening_schema, extraction_schema

def test_screening_schema_contract():
    sample = {
        "include": True,
        "include_reason": "Meets all mandatory criteria.",
        "exclusion_reasons": [],
        "tags": {
            "uk_setting": True,
            "year_in_range_2019_2025": True,
            "language_english": True,
            "comparison_group_present": True,
            "cost_outcomes_present": True,
            "literature_type": "peer_reviewed",
            "evidence_map_shift": ["community"],
            "cash_releasing_checks": {
                "direct_budget_reduction_explicit": True,
                "clear_route_remove_from_baseline": True,
                "robust_calc_vs_baseline_counterfactual": True,
                "in_year_and_sustainable": True,
                "net_single_auditable": True,
                "no_cost_shifting_or_harm": True,
                "overall_cash_releasing": True
            }
        },
        "evidence_spans": [{"label":"cash_releasing","quote":"‘cash-releasing savings to the Trust’s operating budget’"}],
        "confidence": 0.86
    }
    validate(sample, screening_schema)

def test_extraction_schema_contract():
    sample = {
        "id": "doi:10.1234/abc",
        "title": "Community pharmacy-led intervention",
        "authors": ["Smith J", "Patel R"],
        "year": 2022,
        "journal_or_source": "BMJ",
        "doi": "10.1234/abc",
        "pmid": None,
        "url": None,
        "uk_setting": True,
        "setting_detail": "NHS community pharmacy in England",
        "evidence_map_shift": ["community","digital"],
        "study_design": "cluster RCT",
        "literature_type": "peer_reviewed",
        "population": "Adults with hypertension",
        "intervention": "Pharmacist-led home BP monitoring via NHS App",
        "comparator": "Usual care",
        "comparison_group_present": True,
        "primary_outcomes": ["total cost", "BP control"],
        "cost_metrics": ["total cost", "budget reduction"],
        "effect_summary": "Reduced total cost vs usual care with improved BP control.",
        "time_horizon": "3–12 months",
        "cash_releasing_assessment": {
            "direct_budget_reduction_explicit": True,
            "clear_route_remove_from_baseline": True,
            "robust_calc_vs_baseline_counterfactual": True,
            "in_year_and_sustainable": True,
            "net_single_auditable": True,
            "no_cost_shifting_or_harm": True,
            "overall_cash_releasing": True,
            "notes": "Savings net of implementation; headcount reduction explicit."
        },
        "evidence_spans": [{"label":"comparator","quote":"compared with usual care over 12 months"}]
    }
    validate(sample, extraction_schema)
