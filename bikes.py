"""This is a module level string. It describes the overall purpose
of this module. For Thinkful courses, I suggest you provide a
summarization of the requirements given to you in assignments and
projects.

"""


class Bike(object):
    """This is a class-level docstring. You should describe classes
    with docstrings like this. Be sure to list and explain a class'
    attributes, I got you started!

    Attributes:
        name (str): Bike model name

    """

    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost


class Bike_shop(object):

    def __init__(self, name, inventory, markup):
        self.name = name
        self.inventory = inventory
        self.profit = 0
        self.markup = markup
    
    def sell(self,bike):
        self.inventory[bike] = self.inventory[bike] - 1
        self.profit += bike.cost * self.markup


class Customer(object):
    def __init__(self, fund, name):
        self.name = name
        self.fund = fund
        self.bike = None 
    
    def buy_bike(self, bike_shop, bike):
        if bike.cost * (1 + bike_shop.markup) <= self.fund and bike_shop.inventory[bike] > 0:
            self.bike = bike
            self.fund = self.fund - bike.cost * (1 +bike_shop.markup)
            bike_shop.sell(bike)
        else:
            print("Unable to complete sale")
