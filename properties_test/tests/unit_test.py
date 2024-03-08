import unittest
import requests


class TestPropertyEndpoint(unittest.TestCase):
    def test_get_properties(self):
        url = 'http://localhost:8000/properties'  # Replace with your endpoint URL
        params = {'city': 'bogota', 'year': 2000}
        response = requests.get(url, params=params)
        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check content type
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Check response body
        properties = response.json()
        self.assertIsInstance(properties, list)
        for property in properties:
            self.assertIsInstance(property, dict)
            self.assertIn('id', property)
            self.assertIn('address', property)
            self.assertIn('city', property)
            self.assertIn('price', property)
            self.assertIn('description', property)
            self.assertIn('year', property)
            self.assertIn('status', property)

    def test_must_fail_get_properties_wrong_params(self):
        url = 'http://localhost:8000/properties'  # Replace with your endpoint URL
        params = {'city': 'bogota', 'year': 'dos mil'
                                            ''
                                            ''}
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
