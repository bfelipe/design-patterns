from enum import Enum

class Carriers(Enum):
    MASTERCARD = 'MASTERCARD'
    VISA = 'VISA'
    PAYPAL = 'PAYPAL'

class PaymentAdapter:
    def __init__(self, carrier:Carriers):
        self.carrier = carrier

    def process(self, amount):
        raise Exception(f'{self.carrier} adapter is currently not implemented')
    
class MasterCardAdapter(PaymentAdapter):
    def __init__(self, token):
        super().__init__(Carriers.MASTERCARD)
        self.token = token

    def process(self, amount):
        print(f'Processing {amount} using {self.carrier} service')

class VisaAdapter(PaymentAdapter):
    def __init__(self, credentials, certificate, retry=1):
        super().__init__(Carriers.VISA)
        self.credentials = credentials
        self.certificate = certificate
        self.retry = retry

    def process(self, amount):
        print(f'Processing {amount} using {self.carrier} service')


class PaymentService:
    
    def pay(self, carrier: Carriers, amount):
        if carrier == Carriers.MASTERCARD:
            adapter = MasterCardAdapter('123')
            adapter.process(amount)
        elif carrier == Carriers.VISA:
            adapter = VisaAdapter('user:pass', 'my_cert.cert', 3)
            adapter.process(amount)
        else:
            adapter = PaymentAdapter(Carriers.PAYPAL)
            adapter.process(amount)
        
service = PaymentService()

service.pay(Carriers.MASTERCARD, 12.03)
service.pay(Carriers.VISA, 1000.02)
service.pay(Carriers.PAYPAL, 50.00)