import unittest
from app.main import app
import json


class RecipeAPITest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.test_recipe = {
            'name': 'Test Recipe',
            'country': 'Test Country',
            'instructions': 'Test Instructions'
        }

    def test_create_recipe(self):
        response = self.app.post('/recipes/upload', json=self.test_recipe)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data.get('message'))
        self.assertTrue(data.get('recipe_id'))

    def test_create_recipe_missing_data(self):
        incomplete_recipe = {'name': 'Incomplete Recipe', 'country': 'Incomplete Country'}
        response = self.app.post('/recipes/upload', json=incomplete_recipe)
        self.assertEqual(response.status_code, 400)

    def test_update_recipe(self):
        create_response = self.app.post('/recipes/upload', json=self.test_recipe)
        data = json.loads(create_response.data.decode('utf-8'))
        recipe_id = data.get('recipe_id')

        updated_recipe = {
            'name': 'Updated Recipe',
            'country': 'Updated Country',
            'instructions': 'Updated Instructions'
        }
        update_response = self.app.put(f'/recipes/{recipe_id}', json=updated_recipe)
        self.assertEqual(update_response.status_code, 200)

    def test_search_recipes_by_country(self):
        response = self.app.get('/recipes/search?country=Test Country')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue(data)

    def test_search_recipes_by_nonexistent_country(self):
        response = self.app.get('/recipes/search?country=Nonexistent Country')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data.get('message'), 'No recipes found for the specified country')


if __name__ == '__main__':
    unittest.main()
