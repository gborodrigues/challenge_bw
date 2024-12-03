import unittest
from main import reconcile_accounts


class TestReconcileAccounts(unittest.TestCase):
    def test_basic_case(self):
        transaction1 = [
            ["2020-12-04", "Tecnologia", "16.00", "Bitbucket"],
            ["2020-12-04", "Jurídico", "60.00", "LinkSquares"],
            ["2020-12-05", "Tecnologia", "50.00", "AWS"],
        ]
        transaction2 = [
            ["2020-12-04", "Tecnologia", "16.00", "Bitbucket"],
            ["2020-12-05", "Tecnologia", "49.99", "AWS"],
            ["2020-12-04", "Jurídico", "60.00", "LinkSquares"],
        ]

        expected_out1 = [
            ["2020-12-04", "Tecnologia", "16.00", "Bitbucket", "FOUND"],
            ["2020-12-04", "Jurídico", "60.00", "LinkSquares", "FOUND"],
            ["2020-12-05", "Tecnologia", "50.00", "AWS", "MISSING"],
        ]

        expected_out2 = [
            ["2020-12-04", "Tecnologia", "16.00", "Bitbucket", "FOUND"],
            ["2020-12-05", "Tecnologia", "49.99", "AWS", "MISSING"],
            ["2020-12-04", "Jurídico", "60.00", "LinkSquares", "FOUND"],
        ]

        result1, result2 = reconcile_accounts(transaction1, transaction2)
        self.assertEqual(result1, expected_out1)
        self.assertEqual(result2, expected_out2)

    def test_different_dates(self):
        transaction1 = [
            ["2020-12-01", "Tecnologia", "100.00", "Bitbucket"],
            ["2020-12-02", "Tecnologia", "100.00", "Bitbucket"],
            ["2020-12-03", "Jurídico", "200.00", "AWS"],
        ]
        transaction2 = [
            ["2020-12-02", "Tecnologia", "100.00", "Bitbucket"],
            ["2020-12-03", "Jurídico", "200.00", "AWS"],
        ]

        expected_out1 = [
            ["2020-12-01", "Tecnologia", "100.00", "Bitbucket", "FOUND"],
            ["2020-12-02", "Tecnologia", "100.00", "Bitbucket", "MISSING"],
            ["2020-12-03", "Jurídico", "200.00", "AWS", "FOUND"],
        ]

        expected_out2 = [
            ["2020-12-02", "Tecnologia", "100.00", "Bitbucket", "FOUND"],
            ["2020-12-03", "Jurídico", "200.00", "AWS", "FOUND"],
        ]

        result1, result2 = reconcile_accounts(transaction1, transaction2)
        self.assertEqual(result1, expected_out1)
        self.assertEqual(result2, expected_out2)

    def test_multiple_dates(self):
        transaction1 = [
            ["2020-12-25", "Tecnologia", "100.00", "Bitbucket"],
        ]
        transaction2 = [
            ["2020-12-26", "Tecnologia", "100.00", "Bitbucket"],
            ["2020-12-25", "Tecnologia", "100.00", "Bitbucket"],
            ["2020-12-24", "Tecnologia", "100.00", "Bitbucket"],
        ]

        expected_out1 = [
            ["2020-12-25", "Tecnologia", "100.00", "Bitbucket", "FOUND"],
        ]

        expected_out2 = [
            ["2020-12-26", "Tecnologia", "100.00", "Bitbucket", "MISSING"],
            ["2020-12-25", "Tecnologia", "100.00", "Bitbucket", "MISSING"],
            ["2020-12-24", "Tecnologia", "100.00", "Bitbucket", "FOUND"],
        ]

        result1, result2 = reconcile_accounts(transaction1, transaction2)
        self.assertEqual(result1, expected_out1)
        self.assertEqual(result2, expected_out2)


if __name__ == "__main__":
    unittest.main()
