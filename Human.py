class Human:
    name: str
    last_name: str

    ids = set()

    def __init__(self, name, last_name, id=None):
        #print("init HUMAN")
        self.name = name
        self.last_name = last_name
        if id is not None:
            ...
        else:
            ...

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def __repr__(self):
        return f"{self.ids}"

    def __hash__(self):
        return hash(str(self.name) + str(self.last_name))