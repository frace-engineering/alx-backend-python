#!/usr/bin/env python3
"""Unittest"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Instanciate testcase class for the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """nested_map test method using assertEqual"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that the access_nested_map function raises a KeyError"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
            self.assertEqual(str(err.exception), expected)


class TestGetJson(unittest.TestCase):
    """
    TestCase instance for json.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_payload, test_url):
        """
        Test that the get_json return the expected result.
        """
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    class TestClass:
        def a_method(Self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        obj = self.TestClass()
        with patch.object(obj, 'a_method') as mock_method:
            result1 = obj.a_property()
            result2 = obj.a_property()
            mock_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, result1)


if __name__ == '__main__':
    unittest.main()
