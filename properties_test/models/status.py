

class Status:
    def __init__(self, id: int, name: str, label: str):
        self.id = id
        self.name = name
        self.label = label

    @property
    def id(self):
        return self.id
    
    @property
    def name(self):
        return self.name
    
    @property
    def label(self):
        return self.label
    
    def __str__(self):
        return f"Status: {self.id}, {self.name}, {self.label}"