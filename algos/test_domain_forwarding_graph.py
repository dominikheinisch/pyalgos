import unittest
from domain_forwarding_graph import solution


class TestDomainForwardingGraph(unittest.TestCase):
    def test_solution(self):
        input = [
            ["godaddy.net", "godaddy.com"],
            ["godaddy.org", "godaddycares.com"],
            ["godady.com", "godaddy.com"],
            ["godaddy.ne", "godaddy.net"],
        ]
        expected = [
            ["godaddy.com", "godaddy.ne", "godaddy.net", "godady.com"],
            ["godaddy.org", "godaddycares.com"],
        ]
        self.assertEqual(solution(input), expected)


if __name__ == '__main__':
    unittest.main()

