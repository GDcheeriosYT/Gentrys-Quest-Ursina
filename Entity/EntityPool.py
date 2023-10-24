from ursina import *


class EntityPool:
    def __init__(self, size: int, entity, shuffle: bool = False):
        self.size = size
        if isinstance(entity, list):
            self.pool = []
            if self.size < len(entity):
                self.size = len(entity)

            for i in range(self.size%len(entity)):
                self.pool.append(random.choice(entity)())

            entity_type_counter = 0
            while len(self.pool) < self.size:
                if entity_type_counter > len(entity) - 1:
                    break

                for i in range(int(self.size / len(entity))):
                    print(len(self.pool), i, entity_type_counter, entity[entity_type_counter])
                    entity_to_pool = entity[entity_type_counter]()
                    entity_to_pool.disable()
                    self.pool.append(entity_to_pool)

                entity_type_counter += 1

            if shuffle:
                self.shuffle()

        else:
            self.pool = [entity() for _ in range(size)]
            [entity.disable() for entity in self.pool]

    def get_entity(self, enable: bool = True):
        for entity in self.pool:
            if not entity.enabled:
                if enable:
                    entity.enable()

                return entity

        return None

    def get_ready_percent(self):
        counter = 0
        for entity in self.pool:
            if not entity.enabled:
                counter += 1

        return counter/self.size

    def get_ready_ratio(self):
        counter = 0
        for entity in self.pool:
            if not entity.enabled:
                counter += 1

        return f"{counter}|{self.size}"

    def destroy(self):
        [destroy(entity) for entity in self.pool]

    def shuffle(self):
        new_pool = []
        for i in range(self.size):
            new_pool.append(self.pool.pop(self.pool.index(random.choice(self.pool))))

        self.pool = new_pool

    def __del__(self):
        self.destroy()
