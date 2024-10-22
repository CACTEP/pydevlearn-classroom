class Human:
    name: str
    last_name: str
    _ids = set()

    def __init__(self, name: str, last_name: str, id=None):
        self.name = name
        self.last_name = last_name
        self._id = id or self._generate_id()

    @classmethod
    def _generate_id(cls):
        new_id = 1
        while new_id in cls._ids:
            new_id += 1
        cls._ids.add(new_id)
        return new_id

    def __lt__(self, other):
        return (self.last_name, self.name) < (other.last_name, other.name)

    def __hash__(self):
        return hash(str(self.name + self.last_name + self.__id))

    def __repr__(self):
        return f"Человек (Имя = '{self.name}', Фамилия = '{self.last_name}', id={self._id})"

    def __str__(self):
        return f"{self.name} {self.last_name}"
