import unittest

from day04_datetime.timestamp_generator import generate_timestamps


class TestTimestampGenerator(unittest.TestCase):

    def test_generate_basic_range(self):
        timestamps = generate_timestamps("2025-07-19", "2025-07-19", 60)
        self.assertEqual(len(timestamps), 24)
        self.assertTrue(all(ts.endswith(":00") for ts in timestamps))

    def test_custom_interval(self):
        timestamps = generate_timestamps("2025-07-19", "2025-07-19", 30)
        self.assertEqual(len(timestamps), 48)

    def test_format_correctness(self):
        timestamps = generate_timestamps("2025-07-19", "2025-07-19", 120)
        for ts in timestamps:
            self.assertRegex(ts, r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")

if __name__ == "__main__":
    unittest.main()
