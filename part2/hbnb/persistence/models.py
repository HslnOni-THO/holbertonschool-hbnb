class Entity:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")

class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get("city_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.number_rooms = kwargs.get("number_rooms", 0)
        self.number_bathrooms = kwargs.get("number_bathrooms", 0)
        self.max_guest = kwargs.get("max_guest", 0)
        self.price_by_night = kwargs.get("price_by_night", 0)
        self.latitude = kwargs.get("latitude", 0.0)
        self.longitude = kwargs.get("longitude", 0.0)
        self.amenity_ids = kwargs.get("amenity_ids", [])
        self.review_ids = kwargs.get("review_ids", [])

class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get("place_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.text = kwargs.get("text", "")

class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")
