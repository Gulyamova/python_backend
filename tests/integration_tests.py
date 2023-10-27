import unittest
from app.main import app
import json


class RecipeIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.test_recipe = {
            'name': 'Kurutob',
            'country': 'Tajikistan',
            'instructions': 'lalala'
        }

    def test_create_update_and_search_recipe(self):
        # Создаем рецепт
        create_response = self.app.post('/recipes/upload', json=self.test_recipe)
        data = json.loads(create_response.data.decode('utf-8'))
        self.assertEqual(create_response.status_code, 200)
        self.assertTrue(data.get('recipe_id'))

        # Обновляем рецепт
        recipe_id = data['recipe_id']
        updated_recipe = {
            'name': 'Shakarob',
            'country': 'Tajikistan',
            'instructions': 'lalalalala'
        }
        update_response = self.app.put(f'/recipes/{recipe_id}', json=updated_recipe)
        self.assertEqual(update_response.status_code, 200)

        # Проверяем, что рецепт обновился
        search_response = self.app.get('/recipes/search?country=Updated Country')
        self.assertEqual(search_response.status_code, 200)
        search_data = json.loads(search_response.data.decode('utf-8'))
        self.assertTrue(search_data)
        self.assertEqual(search_data[0]['name'], 'Updated Recipe')


if __name__ == '__main__':
    unittest.main()
