class Contact:
    def __init__(self, phone, email, fax):
        self.phone = phone
        self.email = email
        self.fax = fax
    
    def __repr__(self):
        return f'<Contact {self.phone} - {self.email} - {self.fax}>'


class Address:
    def __init__(self, street, number, lat, long):
        self.street = street
        self.number = number
        self.lat = lat
        self.long = long
    
    def __repr__(self):
        return f'<Address {self.street} - {self.number} - {self.lat} - {self.long}>'


class Store:
    def __init__(self, store_id, name, address, contact):
        self.store_id = store_id
        self.name = name
        self.address = address
        self.contact = contact

    def __repr__(self):
        return f'<Store {self.store_id} - {self.name} - {self.address} - {self.contact}>'


class ContactBuilder:
    def __init__(self, phone='', email='', fax=''):
        self.phone = phone
        self.email = email
        self.fax = fax

    def with_phone(self, phone):
        self.phone = phone
        return self

    def with_email(self, email):
        self.email = email
        return self
    
    def with_fax(self, fax):
        self.fax = fax
        return self
    
    def build(self):
        return Contact(self.phone, self.email, self.fax)


class AddressBuilder:
    def __init__(self, street='', number=0, lat=0.0, long=0.0):
        self.street = street
        self.number = number
        self.lat = lat
        self.long = long
    
    def with_street(self, street):
        self.street = street
        return self
    
    def with_number(self, number):
        self.number = number
        return self
    
    def with_lat(self, lat):
        self.lat = lat
        return self
    
    def with_long(self, long):
        self.long = long
        return self
    
    def build(self):
        return Address(self.street, self.number, self.lat, self.long)


class StoreBuilder:
    def __init__(self, store_id='', name='', address=None, contact=None):
        self.store_id = store_id
        self.name = name
        self.address = address
        self.contact = contact
    
    def with_store_id(self, store_id):
        self.store_id = store_id
        return self
    
    def with_name(self, name):
        self.name = name
        return self
    def with_address(self, address):
        self.address = address
        return self
    
    def with_contact(self, contact):
        self.contact = contact
        return self

    def build(self):
        return Store(self.store_id, self.name, self.address, self.contact)

    
address = AddressBuilder()\
    .with_street('motherboard street')\
    .with_number(123)\
    .with_lat(-0022.1232)\
    .with_long(01.1232)\
    .build()

contact = ContactBuilder()\
    .with_phone('123-123-123')\
    .with_email('contact@mail.com')\
    .build()

store = StoreBuilder()\
    .with_store_id('123')\
    .with_name('Tech store')\
    .with_address(address)\
    .with_contact(contact)\
    .build()

print(store)