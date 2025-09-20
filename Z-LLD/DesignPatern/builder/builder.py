# Product
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None
        self.cheese = None

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, {self.topping} topping, {self.cheese} cheese"

# Builder
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough
        return self  # for chaining

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def set_topping(self, topping):
        self.pizza.topping = topping
        return self

    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def build(self):
        return self.pizza

# Client code
builder = PizzaBuilder()
pizza = (builder
         .set_dough("Thin Crust")
         .set_sauce("Tomato")
         .set_topping("Pepperoni")
         .set_cheese("Mozzarella")
         .build())

print(pizza)