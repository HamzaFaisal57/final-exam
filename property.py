class Property:
    def __init__(self, property_id, name, location, description, price_per_night, availability_status):
        self.id = property_id
        self.name = name
        self.location = location
        self.desc = description
        self.price = price_per_night
        self.availability = availability_status

    def add_review(self):
        pass
