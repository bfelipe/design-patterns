# Context
class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def use(self, strategy):
        self.strategy = strategy
        return self

    def process(self, data):
        self.strategy.process(data)

class CreditCardStrategy:
    def process(self, data):
        print(f'Processing {data} using CreditCardStrategy')

class DebitCardStrategy:
    def process(self, data):
        print(f'Processing {data} using DebitCardStrategy')

class MoneyStrategy:
    def process(self, data):
        print(f'Processing {data} using MoneyStrategy')

credit_card_processor = PaymentProcessor(CreditCardStrategy()).process(123)
debit_card_processor = PaymentProcessor(DebitCardStrategy()).process(456)
money_processor = PaymentProcessor(MoneyStrategy()).process(789)

payment_processor = PaymentProcessor()
payment_processor.use(CreditCardStrategy()).process(123)
payment_processor.use(DebitCardStrategy()).process(456)
payment_processor.use(MoneyStrategy()).process(789)