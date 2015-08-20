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
        

nick = Customer(200, "nick")
dave = Customer(500, "dave")
josh = Customer(1000, "josh")

customers = [nick, dave, josh]

bike1 = Bike("bmx", 20, 300)
bike2 = Bike("road", 20, 100)
bike3 = Bike("cruiser", 10, 800)
bike4 = Bike("mountain", 30, 500)
bike5 = Bike("bmx", 15, 150)
bike6 = Bike("road", 5, 1000)

inventory = {bike1:2, bike2:3, bike3:1, bike4:5, bike5:2, bike6:4}

store = Bike_shop("Barry's Bikes", inventory, 0.2)

for customer in customers:
    print customer.name, customer.fund

    for bike in inventory.keys():

        if customer.fund >= bike.cost * (1 + store.markup):
            print bike.name, bike.cost * (1 + store.markup)

    print 

print(store.name)

for bike in store.inventory.keys():

    print bike.name + ":", store.inventory[bike], "in stock"

print

nick.buy_bike(store, bike2)
print "Nick bought:", nick.bike.name
print "Cost:", nick.bike.cost * (1 + store.markup)
print "nick has", nick.fund, "left"
print

dave.buy_bike(store, bike1)
print "dave bought:", dave.bike.name
print "Cost:", dave.bike.cost * (1 + store.markup)
print "dave has", dave.fund, "left"
print

josh.buy_bike(store, bike3)
print "josh bought:", josh.bike.name
print "Cost:", josh.bike.cost * (1 + store.markup)
print "josh has", josh.fund, "left"
print

print(store.name)

for bike in store.inventory.keys():
    print bike.name + ":", store.inventory[bike], "in stock"

print "total profit:", store.profit


    
