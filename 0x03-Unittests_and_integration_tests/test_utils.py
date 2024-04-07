#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Instanciate testcase class for the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        """nested_map test method using assertEqual"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError("Key 'a'not found in nested map")),
        ({"a": 1}, ("a", "b"), KeyError("Key 'a' not found in nested map"))
        ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception) -> None:
        """Test that the assess_nested_map function raises a KeyError"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertIsInstance(context.exception, KeyError)
        self.assertEqual(str(context.exception), str(expected_exception))


class TestGetJson(unittest.TestCase):
    """
    A test case for the get_json function in the utils module.
    """

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get) -> None:
        """
        Test that the get_json function returns the expected result.

        Args:
            test_url (str): The test URL to be passed to get_json.
            test_payload (dict): The expected payload to be returned by
            get_json.
            mock_get: Mock object for the requests.get function.

        Raises:
            AssertionError: If the output of get_json is not equal to
                            test_payload or if the mocked get method was
                            not called exactly once with test_url.
        """
        """Configure the mock object"""
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        """Call the function under test"""
        result = get_json(test_url)

        """Assertions"""
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
