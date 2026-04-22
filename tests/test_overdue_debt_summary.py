from services.metrics import overdue_debt_summary


def test_overdue_debt_summary_tracks_finance_workflow():
    summary = overdue_debt_summary()
    assert summary['receivable_overdue'] >= 0
    assert summary['payable_due'] >= 0
    assert summary['partial_payments'] >= 0
