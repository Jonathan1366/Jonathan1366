import unittest
from datetime import datetime, timezone
import xml.etree.ElementTree as ET
from profile_pulse import count_days, render

class MetricsTest(unittest.TestCase):
    def test_utc_window_and_duplicate_commits(self):
        start = datetime(2026, 9, 8, tzinfo=timezone.utc)
        now = datetime(2026, 9, 21, 12, tzinfo=timezone.utc)
        def commit(sha, date):
            return {'sha': sha, 'commit': {'committer': {'date': date}}}
        commits = [commit('a', '2026-09-08T00:00:00Z'), commit('a', '2026-09-08T00:00:00Z'),
                   commit('b', '2026-09-21T13:00:00+02:00'), commit('c', '2026-09-21T13:00:00Z'),
                   commit('d', '2026-09-07T23:59:59Z')]
        counts = count_days(commits, start, now)
        self.assertEqual(sum(counts), 2)
        self.assertEqual((counts[0], counts[-1]), (1, 1))

    def test_zero_activity_and_escaped_labels(self):
        data = {'collected_at': '2026-09-21T12:00:00+00:00', 'repositories': [
            {'name': 'project<&>', 'languages': {}, 'daily_commits': [0]*14, 'last_push': None}]}
        svg = render(data)
        ET.fromstring(svg)
        self.assertIn('project&lt;&amp;&gt;', svg)
        self.assertIn('No language data', svg)
        self.assertNotIn('nan', svg)
        self.assertNotIn('height="0.00"', svg)

    def test_language_bar_widths(self):
        data = {'collected_at': '2026-09-21T12:00:00+00:00', 'repositories': [
            {'name': 'example', 'languages': {'Go': 3, 'Rust': 1}, 'daily_commits': [1]*14,
             'last_push': '2026-09-21T12:00:00Z'}]}
        svg = render(data)
        self.assertIn('Go 75.0%', svg)
        doc = ET.fromstring(svg)
        bars = [float(n.attrib['width']) for n in doc.findall('.//{http://www.w3.org/2000/svg}rect') if n.attrib.get('height') == '7']
        self.assertAlmostEqual(sum(bars), 194)

if __name__ == '__main__':
    unittest.main()
