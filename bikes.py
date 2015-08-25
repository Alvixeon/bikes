"""
This module will model the bike industry by creating classes to 
represent:

-bikes
-bike stores
-customers

"""


class Bike(object):
    """The bike class creates instances of individual bikes

    Attributes:
        name (str): Bike model name
	weight (int): Weight of bike
	cost (int): Cost of bike

    
    """

    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost


class Bike_shop(object):
    """The Bike_shop class creates instances of bike shops

    Attributes:
	name (str): Name of bike shop
	inventory (dict): Each model of bicycle mapped to the number of the model in stock at store
	markup (float): Percentage markup that the store charges above the cost of the bicycle
	profit(float): Amount of profit that the store has generated from its sales 

    Methods:
	sell: Sells one of the bikes in inventory and increases profit by cost * markup

    """


    def __init__(self, name, inventory, markup):
        self.name = name
        self.inventory = inventory
        self.profit = 0
        self.markup = markup
    
    def sell(self,bike):
        self.inventory[bike] = self.inventory[bike] - 1
        self.profit += bike.cost * self.markup


class Customer(object):
    """Customer class creates an instance of a customer who can buy and own a bike

    Attributes:
	name (str): Name of the customer
	fund (float): Amount of money that the customer has and can spend on bikes
	bike (Bike): Bike that the customer owns

    Methods:
	buy_bike: Customer buys a bike and decreases his or her fund by its cost


    """

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
