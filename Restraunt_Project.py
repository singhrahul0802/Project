"""Class Definition"""
class FoodItem:
    def __init__(self, name, price, restaurant, distance, delivery_charges, tags=None):
        self.name = name
        self.price = price
        self.restaurant = restaurant
        self.distance = distance
        self.delivery_charges = delivery_charges
        self.tags = tags if tags else []


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_food_item(self, food_item):
        self.menu[food_item.name] = food_item

    def delete_food_item(self, food_item_name):
        if food_item_name in self.menu:
            del self.menu[food_item_name]

    def update_food_item(self, food_item_name, updated_food_item):
        if food_item_name in self.menu:
            self.menu[food_item_name] = updated_food_item


class User:
    def __init__(self, username):
        self.username = username
        self.reviews = []
        self.wishlist = []
        self.cart = []


class Review:
    def __init__(self, user, food_item, rating, comment=None):
        self.user = user
        self.food_item = food_item
        self.rating = rating
        self.comment = comment


"""Admin Operations"""

restaurant = Restaurant("The Foodie's Paradise")
food_item = FoodItem("Burger", 5.99, restaurant, 2, 2, tags=["spicy", "non veg"])
restaurant.add_food_item(food_item)
restaurant.delete_food_item("Burger")
restaurant.update_food_item("Pizza", FoodItem("Pizza", 8.99, restaurant,
                                              2, 2, tags=["cheesy", "non veg"]))


"""User Operations"""
# User operations
user = User("Alice")
user.reviews.append(Review(user, food_item, 4, "Great burger!"))
user.wishlist.append(food_item)
user.cart.append(food_item)
