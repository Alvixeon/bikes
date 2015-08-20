import bikes


nick = bikes.Customer(200, "nick")
dave = bikes.Customer(500, "dave")
josh = bikes.Customer(1000, "josh")

customers = [nick, dave, josh]

bike1 = bikes.Bike("bmx", 20, 300)
bike2 = bikes.Bike("road", 20, 100)
bike3 = bikes.Bike("cruiser", 10, 800)
bike4 = bikes.Bike("mountain", 30, 500)
bike5 = bikes.Bike("bmx", 15, 150)
bike6 = bikes.Bike("road", 5, 1000)

inventory = {bike1:2, bike2:3, bike3:1, bike4:5, bike5:2, bike6:4}

store = bikes.Bike_shop("Barry's Bikes", inventory, 0.2)

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
print("Nick bought:", nick.bike.name)
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

print("total profit:", store.profit)
