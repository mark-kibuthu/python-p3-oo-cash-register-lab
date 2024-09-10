class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.last_transaction = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
        self.total += price * quantity
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0

    def set_discount(self, percent):
        self.discount = percent
