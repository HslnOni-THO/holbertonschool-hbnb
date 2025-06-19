from hbnb.persistence.repository import InMemoryRepository

class BusinessLogic:
    def __init__(self, repository):
        self.repository = repository

    def get_entity(self, entity_id):
        return self.repository.get(entity_id)
