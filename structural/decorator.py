class Product:
    def __init__(self, name='', cost=00.00, quantity=0, organic=False):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.organic = organic

    def __repr__(self):
        return f'<Product {self.name} - {self.cost} - {self.quantity} - {self.organic}>'

class TaxDecorator:
    def __init__(self, product):
        self.product = product

    def get_cost(self):
        return self.product.cost * self.product.quantity

    def calculate_tax(self):
        raise NotImplementedError("Subclasses must implement the calculate_tax method")

    
class OrganicTax(TaxDecorator):
    def calculate_tax(self):
        return self.get_cost() * 0.1


class NonOrganicTax(TaxDecorator):
    def calculate_tax(self):
        return self.get_cost() * 0.45
    
class ShopCart:
    def __init__(self, products=[]):
        self.products = products
        self.total_cost_organics = 0.0
        self.total_cost_non_organics = 0.0
        self.total_tax_organics = 0.0
        self.total_tax_non_organics = 0.0
        self.total_purchase = 0.0

    def process(self):
        for product in self.products:
            if product.organic:
                decorated_product = OrganicTax(product)
                self.total_cost_organics += decorated_product.get_cost()
                self.total_tax_organics += decorated_product.calculate_tax()
            else:
                decorated_product = NonOrganicTax(product)
                self.total_cost_non_organics += decorated_product.get_cost()
                self.total_tax_non_organics += decorated_product.calculate_tax()
        total_organics = self.total_cost_organics + self.total_tax_organics
        total_non_organics = self.total_cost_non_organics + self.total_tax_non_organics
        self.total_purchase = total_organics + total_non_organics
        return self


    def description(self):
        return {
            'organics': {
                'total_cost_organics': f'%.2f' % self.total_cost_organics,
                'total_tax_organics': f'%.2f' % self.total_tax_organics
            },
            'non_organics': {
                'total_cost_non_organics': f'%.2f' % self.total_cost_non_organics,
                'total_tax_non_organics': f'%.2f' % self.total_tax_non_organics
            },
            'total_purchase': f'%.2f' % self.total_purchase
        }
    
products = [
    Product('apple', 1.10, 7, True),
    Product('laptop', 523.75, 1, False),
    Product('banana', 0.68, 6, True),
    Product('grappes', 3.75, 1, True),
    Product('mouse', 62.80, 1, False),
]

cart = ShopCart(products).process()
print(cart.description())