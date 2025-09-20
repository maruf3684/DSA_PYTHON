from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Bitcoin")

# Context
class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy  # dynamically change strategy

    def checkout(self, amount):
        self.strategy.pay(amount)

# Client code
cart = ShoppingCart(CreditCardPayment())
cart.checkout(100)  # Paid $100 using Credit Card

cart.set_strategy(PayPalPayment())
cart.checkout(200)  # Paid $200 using PayPal

cart.set_strategy(BitcoinPayment())
cart.checkout(300)  # Paid $300 using Bitcoin

#
# 🔹 Key Points
# 	1.	Strategy interface → PaymentStrategy defines pay().
# 	2.	Concrete strategies → CreditCardPayment, PayPalPayment, BitcoinPayment implement the interface.
# 	3.	Context → ShoppingCart uses a strategy and can switch it at runtime.
# 	4.	Client → can choose or change the algorithm dynamically without modifying the context.


# 🔹 Why this is important
#
# Without Strategy Pattern, you might write ShoppingCart like this:
# class ShoppingCart:
#     def checkout(self, amount, method):
#         if method == "credit":
#             # credit card code
#         elif method == "paypal":
#             # paypal code
#         elif method == "bitcoin":
#             # bitcoin code