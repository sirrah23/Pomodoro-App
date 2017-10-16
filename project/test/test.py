import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import unittest
from datetime import datetime

from utils import FakePomodoro
from project.helpers.view_helper import build_graph_view


# TODO: Test day ranges with no data in it
# TODO: Test data plus empty data range

class TestViewDataGeneration(unittest.TestCase):

    def test_one_context_multiple_days(self):
        fp = FakePomodoro([
            (1500, datetime(2017, 5, 6), "Work", 0, 1),
            (1500, datetime(2017, 5, 5), "Work", 0, 1),
        ])
        dataset = build_graph_view(2, fp, 1, start=datetime(2017, 5, 6))
        self.assertEqual(dataset['dates'], ['2017-05-05', '2017-05-06'])
        self.assertEqual(dataset['data'][0]['context'], 'Work')
        self.assertEqual(dataset['data'][0]['counts'], [1, 1])

    def test_two_contexts_one_day(self):
        fp = FakePomodoro([
            (1500, datetime(2017, 5, 5), "Work", 0, 1),
            (1500, datetime(2017, 5, 5), "Home", 0, 1),
        ])
        dataset = build_graph_view(2, fp, 1, start=datetime(2017, 5, 6))
        self.assertEqual(dataset['dates'], ['2017-05-05', '2017-05-06'])
        for d in dataset['data']:
            if d['context'] == 'Work':
                self.assertEqual(d['context'], 'Work')
                self.assertEqual(d['counts'], [1, 0])
            else:
                self.assertEqual(d['context'], 'Home')
                self.assertEqual(d['counts'], [1, 0])


if __name__ == '__main__':
    unittest.main()
