
# “Adapter allows a class with incompatible methods to be used - by a client - by wrapping it and translating its methods.”

# 🔹 Scenario
# 	•	Client code wants to process payments using a standard interface: process_payment(amount)
# 	•	Different payment providers (PayPal, Stripe) have different method names and parameters
# 	•	Adapter allows the client to use them without changing client code



# Target interface expected by client
class PaymentProcessor:
    def process_payment(self, amount):
        pass

# Adaptee 1: PayPal (incompatible interface)
class PayPal:
    def send_payment(self, total):
        print(f"PayPal processed payment of ${total}")

# Adaptee 2: Stripe (incompatible interface)
class Stripe:
    def make_payment(self, value):
        print(f"Stripe processed payment of ${value}")



# Adapter for PayPal
class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal):
        self.paypal = paypal

    def process_payment(self, amount):
        self.paypal.send_payment(amount)

# Adapter for Stripe
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe):
        self.stripe = stripe

    def process_payment(self, amount):
        self.stripe.make_payment(amount)





# Client code
def checkout(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

# Usage
paypal = PayPalAdapter(PayPal())
stripe = StripeAdapter(Stripe())

checkout(paypal, 100)   # PayPal processed payment of $100
checkout(stripe, 200)   # Stripe processed payment of $200

# 🔹 How the client benefits
# 	1.	Client calls the same method process_payment() for all payment providers.
# 	2.	No need to change client code if a new provider is added; just create a new adapter.
# 	3.	Legacy or third-party libraries can be reused without modifying them.