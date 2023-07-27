from ursina import *


class EntityPool:
    def __init__(self, size: int, entity):
        self.size = size
        if isinstance(entity, list):
            if self.size < len(entity):
                self.size = len(entity)

            self.pool = []
            enemy_type_counter = 0
            while len(self.pool) < self.size:
                for i in range(int(self.size / len(entity))):
                    entity_to_pool = entity[enemy_type_counter]()
                    entity_to_pool.disable()
                    self.pool.append(entity_to_pool)

                enemy_type_counter += 1

        else:
            self.pool = [entity() for _ in range(size)]
            [entity.disable() for entity in self.pool]

    def get_entity(self):
        for entity in self.pool:
            if not entity.enabled:
                entity.enable()
                return entity

        return None

    def destroy(self):
        [destroy(entity) for entity in self.pool]

    def __del__(self):
        self.destroy()
