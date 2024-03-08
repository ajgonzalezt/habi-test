from models.status import Status


class Property:

    def __init__(self, id: int, address: str, city: str, price:int, description: str, year: int, status: str):
        self._id = id
        self._address = address
        self._city = city
        self._price = price
        self._description = description
        self._year = year
        self._status = status

    @property
    def id(self):
        return self._id
    
    @property
    def address(self):
        return self._address
    
    @property
    def city(self):
        return self._city
    
    @property
    def price(self):
        return self._price
    
    @property
    def description(self):
        return self._description
    
    @property
    def year(self):
        return self._year
    
    @property
    def status(self):
        return self._status

    def __str__(self):
        return f"address: {self._address}, city: {self._city}, status: {self._status}, price: {self._price}, description: {self._description}"

    def to_dict(self):
        return {
            'id': self._id,
            'address': self._address,
            'city': self._city,
            'price': self._price,
            'description': self._description,
            'year': self._year,
            'status': self._status
        }

