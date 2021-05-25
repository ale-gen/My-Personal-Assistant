import requests
import sys
from Data.Meal import Meal
from Views.Recipe_Images import Recipe_Images_View
import os


def fetch_recipes_json(api_key, random, meal_user=None, id_meal_searched=None):
    if random:
        url = f"https://api.spoonacular.com/recipes/random?apiKey={api_key}"
    elif meal_user is not None:
        base_url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}"
        url = base_url + f"&query={meal_user}"
    else:
        url = f"https://api.spoonacular.com/recipes/{id_meal_searched}/information?apiKey={api_key}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            response = 'N/A'
            return -1
        else:
            data = response.json()
            print(data)
            if random:
                recipe_data_encoded = decode_random_data(data)
            elif meal_user is not None:
                return data
            else:
                recipe_data_encoded = decode_data(data)
            return recipe_data_encoded
    except requests.exceptions.RequestException as error:
        print(error)
        sys.exit(1)


def check_recipe(assistant, api_key, random, meal=None):
    data = fetch_recipes_json(api_key, random, meal)
    if data != -1:
        if random:
            assistant.respond(f"You draw {data['name']}")
        elif meal is not None:
            data = choose_dish(api_key, assistant, data)

        meal = Meal(data['name'], data['vegetarian'], data['time to prepare'], data['servings'], data['price per servings'],
                    data['ingredients'])
        assistant.respond(meal.__str__())
        meal.generate_shopping_list()


def choose_dish(api_key, assistant, data):
    images = []
    titles = []
    results_number = len(data['results'])
    for i in range(0,results_number):
        images.append(data['results'][i]['image'])
        titles.append(data['results'][i]['title'])
    assistant.respond(f"I found {results_number} recipes. Please choose one of them. ")
    download_images(images, titles)
    recipe_view = Recipe_Images_View(images, titles)
    choice = ""
    while choice is "" or choice is None:
        choice = recipe_view.get_chosen_image()
    choice = int(choice)
    delete_images(images, titles)
    print(data)
    id = data['results'][choice]['id']
    return fetch_recipes_json(api_key, False, None, id)


def download_images(images, titles):
    for i in range(0, len(images)):
        with open(f'{titles[i]}.jpg', 'wb') as handle:
            response = requests.get(f"{images[i]}", stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)


def delete_images(images, titles):
    for i in range(0, len(images)):
        try:
            os.remove(f"{titles[i]}.jpg")
        except:
            print("File can't be removed")


def decode_data(json_data):
    vegetarian = json_data['vegetarian']
    name = json_data['title']
    instruction = json_data['instructions']
    time_to_prepare = json_data['readyInMinutes']
    servings = json_data['servings']
    price_per_serving = json_data['pricePerServing']
    ingredients_number = len(json_data['extendedIngredients'])
    ingredients = []
    for index in range(0, ingredients_number):
        base = json_data['extendedIngredients'][index]
        ingredients.append(
            (base['name'], base['measures']['metric']['amount'], base['measures']['metric']['unitShort']))
    recipe_data = {"name": name, "vegetarian": vegetarian, "instruction": instruction,
                   "time to prepare": time_to_prepare,
                   "servings": servings, "price per servings": price_per_serving, "ingredients": ingredients}
    return recipe_data


def decode_random_data(json_data):
    vegetarian = json_data['recipes'][0]['vegetarian']
    name = json_data['recipes'][0]['title']
    instruction = json_data['recipes'][0]['instructions']
    time_to_prepare = json_data['recipes'][0]['readyInMinutes']
    servings = json_data['recipes'][0]['servings']
    price_per_serving = json_data['recipes'][0]['pricePerServing']
    ingredients_number = len(json_data['recipes'][0]['extendedIngredients'])
    ingredients = []
    for index in range(0, ingredients_number):
        base = json_data['recipes'][0]['extendedIngredients'][index]
        ingredients.append((base['name'], base['measures']['metric']['amount'], base['measures']['metric']['unitShort']))
    recipe_data = {"name": name, "vegetarian": vegetarian, "instruction": instruction, "time to prepare": time_to_prepare,
                    "servings": servings, "price per servings": price_per_serving, "ingredients": ingredients}
    return recipe_data