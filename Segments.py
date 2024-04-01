class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_food_items(self, food_item):
        self.menu[food_item.name] = food_item

    def delete_food_item(self, food_item_name):
        if food_item_name in self.menu:
            del self.menu[food_item_name]

    def update_food_item(self, food_item_name, updated_food_item):
        if food_item_name in self.menu:
            self.menu[food_item_name] = updated_food_item
