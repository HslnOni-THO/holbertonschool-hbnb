class InMemoryRepository:
    def __init__(self):
        self._data = {}

    def add(self, entity):
        self._data[entity.id] = entity

    def get(self, entity_id):
        return self._data.get(entity_id)

    def delete(self, entity_id):
        if entity_id in self._data:
            del self._data[entity_id]
