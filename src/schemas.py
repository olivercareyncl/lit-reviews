# Strict JSON Schemas for screening and extraction

screening_schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "include": {"type": "boolean"},
        "include_reason": {"type": "string"},
        "exclusion_reasons": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List specific criteria that failed, if include=false.",
        },
        "tags": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "uk_setting": {"type": "boolean"},
                "year_in_range_2019_2025": {"type": "boolean"},
                "language_english": {"type": "boolean"},
                "comparison_group_present": {"type": "boolean"},
                "cost_outcomes_present": {"type": "boolean"},
                "literature_type": {
                    "type": "string",
                    "enum": ["peer_reviewed", "report", "dissertation", "conference_abstract", "other_grey", "unknown"]
                },
                "evidence_map_shift": {
                    "type": "array",
                    "items": {"type": "string", "enum": ["community", "digital", "prevention"]},
                    "minItems": 0,
                    "uniqueItems": True
                },
                "cash_releasing_checks": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "direct_budget_reduction_explicit": {"type": "boolean"},
                        "clear_route_remove_from_baseline": {"type": "boolean"},
                        "robust_calc_vs_baseline_counterfactual": {"type": "boolean"},
                        "in_year_and_sustainable": {"type": "boolean"},
                        "net_single_auditable": {"type": "boolean"},
                        "no_cost_shifting_or_harm": {"type": "boolean"},
                        "overall_cash_releasing": {"type": "boolean"},
                    },
                    "required": [
                        "direct_budget_reduction_explicit",
                        "clear_route_remove_from_baseline",
                        "robust_calc_vs_baseline_counterfactual",
                        "in_year_and_sustainable",
                        "net_single_auditable",
                        "no_cost_shifting_or_harm",
                        "overall_cash_releasing"
                    ]
                }
            },
            "required": [
                "uk_setting", "year_in_range_2019_2025", "language_english",
                "comparison_group_present", "cost_outcomes_present", "literature_type",
                "evidence_map_shift", "cash_releasing_checks"
            ]
        },
        "evidence_spans": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "label": {"type": "string"},
                    "quote": {"type": "string"}
                },
                "required": ["label", "quote"]
            },
            "maxItems": 5
        },
        "confidence": {"type": "number", "minimum": 0, "maximum": 1}
    },
    "required": ["include", "include_reason", "tags", "evidence_spans", "confidence"]
}

extraction_schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "id": {"type": "string"},
        "title": {"type": "string"},
        "authors": {"type": "array", "items": {"type": "string"}},
        "year": {"type": "integer"},
        "journal_or_source": {"type": "string"},
        "doi": {"type": ["string", "null"]},
        "pmid": {"type": ["string", "null"]},
        "url": {"type": ["string", "null"]},

        "uk_setting": {"type": "boolean"},
        "setting_detail": {"type": "string"},
        "evidence_map_shift": {
            "type": "array",
            "items": {"type": "string", "enum": ["community", "digital", "prevention"]},
            "minItems": 1, "uniqueItems": True
        },

        "study_design": {"type": "string"},
        "literature_type": {
            "type": "string",
            "enum": ["peer_reviewed", "report", "dissertation", "conference_abstract", "other_grey"]
        },
        "population": {"type": "string"},
        "intervention": {"type": "string"},
        "comparator": {"type": ["string", "null"]},
        "comparison_group_present": {"type": "boolean"},

        "primary_outcomes": {"type": "array", "items": {"type": "string"}},
        "cost_metrics": {"type": "array", "items": {"type": "string"}},
        "effect_summary": {"type": "string"},
        "time_horizon": {
            "type": "string",
            "enum": ["≤1 month","3–12 months",">12–36 months",">3 years","Unknown"]
        },

        "cash_releasing_assessment": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "direct_budget_reduction_explicit": {"type": "boolean"},
                "clear_route_remove_from_baseline": {"type": "boolean"},
                "robust_calc_vs_baseline_counterfactual": {"type": "boolean"},
                "in_year_and_sustainable": {"type": "boolean"},
                "net_single_auditable": {"type": "boolean"},
                "no_cost_shifting_or_harm": {"type": "boolean"},
                "overall_cash_releasing": {"type": "boolean"},
                "notes": {"type": "string"}
            },
            "required": [
                "direct_budget_reduction_explicit",
                "clear_route_remove_from_baseline",
                "robust_calc_vs_baseline_counterfactual",
                "in_year_and_sustainable",
                "net_single_auditable",
                "no_cost_shifting_or_harm",
                "overall_cash_releasing",
                "notes"
            ]
        },

        "evidence_spans": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "label": {"type": "string"},
                    "quote": {"type": "string"}
                },
                "required": ["label", "quote"]
            },
            "maxItems": 8
        }
    },
    "required": [
        "id","title","authors","year","journal_or_source",
        "uk_setting","evidence_map_shift","study_design","literature_type",
        "population","intervention","comparison_group_present",
        "primary_outcomes","effect_summary","time_horizon",
        "cash_releasing_assessment","evidence_spans"
    ]
}
