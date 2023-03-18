class Database:
    def __init__(self, id: str):
        self.id = id
        self.data = {}

    def get_id(self) -> str:
        return self.id

    def add(self, key: str, value: str) -> None:
        self.data[key] = value

    def get(self, key: str) -> str:
        return self.data[key]

    def update(self, key: str, value: str) -> None:
        if key in self.data:
            self.data[key] = value

    def remove(self, key: str) -> None:
        if key in self.data:
            del self.data[key]

    def display(self, show_title=False) -> None:
        if show_title:
            print(f'Database {self.id}:')
            for key, value in self.data.items():
                print(f'{key} | {value}')
            print()
        else:
            for key, value in self.data.items():
                print(f'{key} | {value}')
            print()
