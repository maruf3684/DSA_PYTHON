# Base component
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Plain Coffee"

# Decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

# Concrete decorator: Milk
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Milk"

# Concrete decorator: Sugar
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", Sugar"

# Client code
coffee = Coffee()
print(coffee.description(), coffee.cost())  # Plain Coffee 5

coffee_milk = MilkDecorator(coffee)
print(coffee_milk.description(), coffee_milk.cost())  # Plain Coffee, Milk 7

coffee_milk_sugar = SugarDecorator(coffee_milk)
print(coffee_milk_sugar.description(), coffee_milk_sugar.cost())  # Plain Coffee, Milk, Sugar 8


#
# 🔹 Key Points
# 	1.	Component → Coffee (original class)
# 	2.	Decorator → CoffeeDecorator (base decorator)
# 	3.	Concrete decorators → MilkDecorator, SugarDecorator (adds behavior)
# 	4.	Client → can dynamically wrap objects with multiple decorators
#
# ⸻
#
# 🔹 Interview Tip
#
# “Decorator pattern is used when we want to add functionality to objects dynamically,
#     instead of creating a lot of subclasses. It wraps the original object and adds behavior at runtime.”