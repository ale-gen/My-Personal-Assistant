class RecipeData:
    def __init__(self, json_data):
        self.json_data = json_data

    def decode_data(self):
        vegetarian = self.json_data['recipes'][0]['vegetarian']
        name = self.json_data['recipes'][0]['title']
        instruction = self.json_data['recipes'][0]['instructions']
        time_to_prepare = self.json_data['recipes'][0]['readyInMinutes']
        servings = self.json_data['recipes'][0]['servings']
        price_per_serving = self.json_data['recipes'][0]['pricePerServing']
        ingredients_number = len(self.json_data['recipes'][0]['extendedIngredients'])
        ingredients = []
        for index in range(0, ingredients_number):
            base = self.json_data['recipes'][0]['extendedIngredients'][index]
            ingredients.append((base['name'], base['measures']['metric']['amount'], base['measures']['metric']['unitShort']))
        recipe_data = {"name": name, "vegetarian": vegetarian, "instruction": instruction, "time to prepare": time_to_prepare,
                       "servings": servings, "price per servings": price_per_serving, "ingredients": ingredients}
        return recipe_data
