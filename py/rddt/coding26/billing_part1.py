"""
Part 1 — Rebuild BillingStatus from financial transaction logs.

Spec (billing.md): BillingStatus tracks monetary columns; each transaction adds
its monetary fields to the current totals. Build one BillingStatus per user_id.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any


MONETARY_COLUMNS = ("ad_delivery_pennies", "payment_pennies")


class BillingStatus:
    """Account state with fixed monetary columns (amounts in pennies)."""

    __slots__ = ("ad_delivery_pennies", "payment_pennies")

    def __init__(self) -> None:
        self.ad_delivery_pennies: int = 0
        self.payment_pennies: int = 0

    def ingest(self, transaction: dict[str, Any], monetary_columns: tuple[str, ...]) -> None:
        """Add this transaction's monetary column values into this status."""
        for col in monetary_columns:
            if col in transaction:
                current = getattr(self, col)
                setattr(self, col, current + int(transaction[col]))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BillingStatus):
            return NotImplemented
        return (
            self.ad_delivery_pennies == other.ad_delivery_pennies
            and self.payment_pennies == other.payment_pennies
        )

    def __repr__(self) -> str:
        return (
            f"BillingStatus(ad_delivery_pennies={self.ad_delivery_pennies}, "
            f"payment_pennies={self.payment_pennies})"
        )


def rebuild_billing_statuses(
    transactions: dict[str, dict[str, Any]],
    monetary_columns: tuple[str, ...],
) -> dict[int, BillingStatus]:
    """
    From a map of transaction_id -> transaction payload, return user_id -> BillingStatus.

    Transactions for each user are applied in chronological order (timestamp, then id).
    """
    by_user: dict[int, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    for tx_id, payload in transactions.items():
        by_user[payload["user_id"]].append((tx_id, payload))

    result: dict[int, BillingStatus] = {}
    for user_id, items in by_user.items():
        items.sort(key=lambda pair: (pair[1]["transaction_timestamp"], pair[0]))
        status = BillingStatus()
        for _, payload in items:
            status.ingest(payload, monetary_columns)
        result[user_id] = status
    return result


# --- Tests -----------------------------------------------------------------


def _part1_example_transactions() -> dict[str, dict[str, Any]]:
    return {
        "ff8bc1c2-8d45-11e9-bc42-526af7764f64": {
            "user_id": 1,
            "ad_delivery_pennies": 1000,
            "transaction_timestamp": 1500000001,
        },
        "ff8bc2e4-8d45-11e9-bc42-526af7764f64": {
            "user_id": 1,
            "ad_delivery_pennies": 1000,
            "transaction_timestamp": 1500000002,
        },
        "ff8bc4ec-8d45-11e9-bc42-526af7764f64": {
            "user_id": 1,
            "payment_pennies": 500,
            "transaction_timestamp": 1500000003,
        },
        "fv24z4ec-8d45-11e9-bc42-526af7764f64": {
            "user_id": 1,
            "ad_delivery_pennies": 1000,
            "payment_pennies": 500,
            "transaction_timestamp": 1500000004,
        },
    }


def test_part1_document_example() -> None:
    """Exact Part 1 scenario from billing.md."""
    out = rebuild_billing_statuses(_part1_example_transactions(), MONETARY_COLUMNS)
    expected = BillingStatus()
    expected.ad_delivery_pennies = 3000
    expected.payment_pennies = 1000
    assert out == {1: expected}


def test_empty_transactions() -> None:
    assert rebuild_billing_statuses({}, MONETARY_COLUMNS) == {}


def test_multiple_users_independent() -> None:
    txs = {
        "a": {"user_id": 1, "ad_delivery_pennies": 100, "transaction_timestamp": 1},
        "b": {"user_id": 2, "payment_pennies": 200, "transaction_timestamp": 2},
        "c": {"user_id": 1, "payment_pennies": 50, "transaction_timestamp": 3},
    }
    out = rebuild_billing_statuses(txs, MONETARY_COLUMNS)
    assert out[1].ad_delivery_pennies == 100
    assert out[1].payment_pennies == 50
    assert out[2].ad_delivery_pennies == 0
    assert out[2].payment_pennies == 200


def test_timestamp_order_affects_only_sequence_not_part1_totals() -> None:
    """Part 1 is pure addition; order is still defined for consistency."""
    txs = {
        "later": {"user_id": 1, "ad_delivery_pennies": 1, "transaction_timestamp": 2},
        "earlier": {"user_id": 1, "ad_delivery_pennies": 2, "transaction_timestamp": 1},
    }
    out = rebuild_billing_statuses(txs, MONETARY_COLUMNS)
    assert out[1].ad_delivery_pennies == 3


def test_stable_sort_same_timestamp() -> None:
    txs = {
        "id-b": {"user_id": 1, "ad_delivery_pennies": 1, "transaction_timestamp": 1},
        "id-a": {"user_id": 1, "ad_delivery_pennies": 1, "transaction_timestamp": 1},
    }
    out = rebuild_billing_statuses(txs, MONETARY_COLUMNS)
    assert out[1].ad_delivery_pennies == 2


def run_all_tests() -> None:
    test_part1_document_example()
    test_empty_transactions()
    test_multiple_users_independent()
    test_timestamp_order_affects_only_sequence_not_part1_totals()
    test_stable_sort_same_timestamp()
    print("All Part 1 tests passed.")


if __name__ == "__main__":
    run_all_tests()
