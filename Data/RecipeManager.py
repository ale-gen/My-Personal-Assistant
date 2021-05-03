import requests
import sys


class RecipeManager:

    def __init__(self, personal_assistant, recipe_data):
        self.personal_assistant = personal_assistant
        self.recipe_data = recipe_data

    def fetch_recipes_json(self, api_key, random, meal=None):
        if random:
            url = f"https://api.spoonacular.com/recipes/random?apiKey={api_key}"
        else:
            base_url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}"
            url = base_url + f"&query={meal}"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                response = 'N/A'
                return -1
            else:
                data = response.json()
                data_encoder = self.recipe_data(data)
                recipe_data_encoded = data_encoder.decode_data()
                return recipe_data_encoded
        except requests.exceptions.RequestException as error:
            print(error)
            sys.exit(1)

    def check_recipe(self, api_key, random, meal=None):
        data = self.fetch_recipes_json(api_key, random, meal)
        if data != -1:
            if random:
                self.personal_assistant.respond(f"You draw {data['name']}")

        price_per_serving = (float(data['price per servings']) / 100).__round__(2)
        self.personal_assistant.respond(f"Your dish is vege: {data['vegetarian']}, time needed to prepare is equal "
                                        f"{data['time to prepare']} minutes. In file I prepare a shopping list for "
                                        f"you for {data['servings']} servings. The price is equal "
                                        f"{price_per_serving} dollars per serving.")

        with open('shopping_list.txt', 'w') as file:
            file.write(f"Shopping list for {data['name']}:\n")
            file.writelines("%s: %s %s\n" % (line[0], line[1], line[2]) for line in data['ingredients'])
