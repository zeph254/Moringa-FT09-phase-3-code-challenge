class Author:
    def __init__(self, id, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'

