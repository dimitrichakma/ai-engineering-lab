from track1_structured_output.s3_ticket_triage.models import Triage
from track1_structured_output.s3_ticket_triage.triage import evaluate


def test_evaluate_counts_accuracy_without_llm():
    gold = [
        {"id": "1", "category": "delivery", "urgency": "medium"},
        {"id": "2", "category": "payment", "urgency": "high"},
    ]
    preds = [
        Triage(category="delivery", urgency="medium", language="english", summary="late order"),
        Triage(category="refund", urgency="high", language="english", summary="double payment"),
    ]
    report = evaluate(gold, preds)
    assert report["category_accuracy"] == 0.5
    assert report["urgency_accuracy"] == 1.0
    # TODO: assert the confusion matrix has ("payment", "refund") once
    # TODO: assert "wrong" has exactly one item with id "2"
