import unittest
import tempfile
import os
from main import last_lines


class TestLastLines(unittest.TestCase):
    def setUp(self):
        self.test_file_path = tempfile.NamedTemporaryFile(delete=False).name

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_basic_case(self):
        content = "This is a file\nThis is line 2\nAnd this is line 3\n"
        with open(self.test_file_path, "w") as f:
            f.write(content)

        lines = last_lines(self.test_file_path)
        self.assertEqual(next(lines), "And this is line 3\n")
        self.assertEqual(next(lines), "This is line 2\n")
        self.assertEqual(next(lines), "This is a file\n")

    def test_empty_file(self):
        with open(self.test_file_path, "w") as f:
            pass

        lines = last_lines(self.test_file_path)
        with self.assertRaises(StopIteration):
            next(lines)

    def test_large_file(self):
        content = "\n".join([f"Line {i}" for i in range(0, 101)]) + "\n"
        with open(self.test_file_path, "w") as f:
            f.write(content)

        lines = last_lines(self.test_file_path)
        self.assertEqual(next(lines), "Line 100\n")
        self.assertEqual(next(lines), "Line 99\n")
        self.assertEqual(next(lines), "Line 98\n")

    def test_large_file_min_buffer(self):
        content = (
            "\n".join([f"This line is bigger than buffer {i}" for i in range(0, 1001)])
            + "\n"
        )
        with open(self.test_file_path, "w") as f:
            f.write(content)

        lines = last_lines(self.test_file_path, 1)
        self.assertEqual(next(lines), "This line is bigger than buffer 1000\n")
        self.assertEqual(next(lines), "This line is bigger than buffer 999\n")
        self.assertEqual(next(lines), "This line is bigger than buffer 998\n")


if __name__ == "__main__":
    unittest.main()
