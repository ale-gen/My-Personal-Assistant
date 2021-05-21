class Meal(object):
    def __init__(self, title, is_vegetarian, prepare_time, servings, price_per_servings, ingredients):
        self.__title = title
        self.__is_vegetarian = bool(is_vegetarian)
        self.__prepare_time = prepare_time
        self.__servings = servings
        self.__price_per_servings = (float(price_per_servings) / 100).__round__(2)
        self.__ingredients = ingredients

    def generate_shopping_list(self):
        with open(f'shopping_list_{self.__title}.txt', 'w') as file:
            file.write(f"Shopping list for {self.__title}:\n")
            file.writelines("%s: %s %s\n" % (line[0], line[1], line[2]) for line in self.__ingredients)

    def __str__(self):
        description = "time needed to prepare is equal {0} minutes. In file I prepare a shopping " \
                      "list for you for {1} servings. The price is equal {2} dollars per serving." \
            .format(self.__prepare_time, self.__servings, self.__price_per_servings)
        if self.__is_vegetarian == "True":
            return "Your dish {0} {1} vegetarian, {2}" \
                .format(self.__title, "is", description)
        else:
            return "Your dish {0} {1} vegetarian, {2}" \
                .format(self.__title, "isn't", description)
