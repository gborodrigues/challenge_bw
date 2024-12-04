import os
import csv
from pathlib import Path
from pprint import pprint
from datetime import datetime
from collections import defaultdict

dir = Path(os.path.dirname(__file__))
transaction1 = list(csv.reader((dir / "transactions1.csv").open()))
transaction2 = list(csv.reader((dir / "transactions2.csv").open()))

FOUND = "FOUND"
MISSING = "MISSING"


def hashed_transactions(transactions):
    hashed = defaultdict(list)
    for transaction in transactions:
        date, *key = transaction
        hashed[tuple(key)].append((datetime.strptime(date, "%Y-%m-%d"), transaction))
    return hashed


def find_earliest(transaction, hashed_transactions, indexes_used):
    _, *key = transaction
    key = tuple(key)
    if key not in hashed_transactions:
        return False
    candidate = hashed_transactions[key]
    match = None
    for i, (candidate_date, candidate) in enumerate(candidate):
        if i not in indexes_used[key] and (match is None or candidate_date < match[1]):
            match = (i, candidate_date, candidate)
    return match


def fit_transactions(transactions1, transaction2, hashed_transactions):
    indexes_used = defaultdict(set)
    for transaction in transactions1:
        match = find_earliest(transaction, hashed_transactions, indexes_used)
        if match:
            i, _, candidate = match
            indexes_used[tuple(transaction[1:])].add(i)
            transaction.append(FOUND)
            index_transaction2 = transaction2.index(candidate)
            transaction2[index_transaction2].append(FOUND)
        else:
            transaction.append(MISSING)

    out2 = [
        transaction if FOUND in transaction else transaction + [MISSING]
        for transaction in transaction2
    ]

    return transactions1, out2


def reconcile_accounts(transaction1, transaction2):
    hashed = hashed_transactions(transaction2)
    out1, out2 = fit_transactions(transaction1, transaction2, hashed)
    return out1, out2


if __name__ == "__main__":
    try:
        out1, out2 = reconcile_accounts(transaction1, transaction2)
        pprint(out1)
        pprint(out2)
    except Exception as e:
        print(e)
