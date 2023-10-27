from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    instructions = Column(String)


engine = create_engine('sqlite:///recipes.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


@app.route('/recipes/upload', methods=['POST'])
def create_recipe():
    recipe_data = request.json
    name = recipe_data.get('name')
    country = recipe_data.get('country')
    instructions = recipe_data.get('instructions')

    if not name or not country or not instructions:
        return jsonify({'error': 'Missing data'}), 400

    session = Session()
    recipe = Recipe(name=name, country=country, instructions=instructions)
    session.add(recipe)
    session.commit()

    return jsonify({'recipe_id': recipe.id, 'message': 'Recipe created successfully'}), 200


def validate_recipe_data(recipe_data):
    if not recipe_data.get('name') or not recipe_data.get('country') or not recipe_data.get('instructions'):
        return False
    return True


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe_data = request.json

    if not validate_recipe_data(recipe_data):
        return jsonify({'error': 'Invalid recipe data'}), 400

    session = Session()
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404

    recipe.name = recipe_data['name']
    recipe.country = recipe_data['country']
    recipe.instructions = recipe_data['instructions']

    session.commit()

    return jsonify({'message': 'Recipe updated successfully'})


@app.route('/recipes/search')
def search_recipes_by_country():
    country_name = request.args.get('country')

    if not country_name:
        return jsonify({'error': 'Country parameter is missing'}), 400

    session = Session()
    recipes = session.query(Recipe).filter_by(country=country_name).all()

    if not recipes:
        return jsonify({'message': 'No recipes found for the specified country'})

    result = [{'name': recipe.name, 'country': recipe.country, 'instructions': recipe.instructions} for recipe in
              recipes]
    return jsonify(result)


if __name__ == '__main__':
    app.run()
