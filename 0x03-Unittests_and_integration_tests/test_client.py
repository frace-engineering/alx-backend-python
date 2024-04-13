#!/usr/bin/env python3
"""Unittest testcase instatnce"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from your_module import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Create testcase class that return known payload"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('your_module.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """Mock the return value of get_json method"""
        mock_get_json.return_value = {'login': org_name}

        github_client = GithubOrgClient(org_name)

        result = github_client.org()

        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

        self.assertEqual(result, {'login': org_name})


if __name__ == "__main__":
    unittest.main()
