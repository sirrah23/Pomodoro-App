import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import unittest
from datetime import datetime

from utils import FakePomodoro
from project.helpers.view_helper import build_graph_view


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

    def test_empty_context_no_days(self):
        fp = FakePomodoro([])
        dataset = build_graph_view(2, fp, 1, start=datetime(2017, 5, 10))
        self.assertEqual(dataset['dates'], ['2017-05-09', '2017-05-10'])
        self.assertEqual(dataset['data'], [])

    def test_one_context_gaps(self):
        fp = FakePomodoro([
            (1500, datetime(2017, 5, 7), "Work", 0, 1),
            (1500, datetime(2017, 5, 5), "Work", 0, 1),
        ])
        dataset = build_graph_view(3, fp, 1, start=datetime(2017, 5, 7))
        self.assertEqual(dataset['dates'], ['2017-05-05', '2017-05-06', '2017-05-07'])
        self.assertEqual(len(dataset['data']), 1)
        self.assertEqual(dataset['data'][0]['context'], 'Work')
        self.assertEqual(dataset['data'][0]['counts'], [1, 0, 1])

    def test_two_contexts_gaps(self):
        fp = FakePomodoro([
            (1500, datetime(2017, 5, 5), "Work", 0, 1),
            (1500, datetime(2017, 5, 5), "Home", 0, 1),
            (1500, datetime(2017, 5, 5), "Home", 0, 1),
            (1500, datetime(2017, 5, 6), "Work", 0, 1),
            (1500, datetime(2017, 5, 7), "Home", 0, 1),
        ])
        dataset = build_graph_view(3, fp, 1, start=datetime(2017, 5, 7))
        self.assertEqual(dataset['dates'], ['2017-05-05', '2017-05-06', '2017-05-07'])
        self.assertEqual(len(dataset['data']), 2)
        for d in dataset['data']:
            if d['context'] == 'Work':
                self.assertEqual(d['context'], 'Work')
                self.assertEqual(d['counts'], [1, 1, 0])
            else:
                self.assertEqual(d['context'], 'Home')
                self.assertEqual(d['counts'], [2, 0, 1])

    def test_one_context_missing_days(self):
        fp = FakePomodoro([
            (1500, datetime(2017, 5, 3), "Home", 0, 1),
            (1500, datetime(2017, 5, 4), "Home", 0, 1),
            (1500, datetime(2017, 5, 5), "Home", 0, 1),
            (1500, datetime(2017, 5, 6), "Home", 0, 1),
        ])
        dataset = build_graph_view(3, fp, 1, start=datetime(2017, 5, 7))
        self.assertEqual(dataset['dates'], ['2017-05-05', '2017-05-06', '2017-05-07'])
        self.assertEqual(len(dataset['data']), 1)
        self.assertEqual(dataset['data'][0]['context'], 'Home')
        self.assertEqual(dataset['data'][0]['counts'], [1, 1, 0])


if __name__ == '__main__':
    unittest.main()
