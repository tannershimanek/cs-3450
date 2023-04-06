from typing import List, Union


class Component:
    def __init__(self, name: str):
        self.name = name
        self.parent = None

    def list(self) -> str:
        raise NotImplementedError

    def list_all(self, level: int = 0) -> str:
        raise NotImplementedError

    def change_dir(self, name: str):
        raise NotImplementedError

    def count_files(self) -> int:
        raise NotImplementedError

    def count_all_files(self) -> int:
        raise NotImplementedError

    def up(self):
        raise NotImplementedError


class File(Component):
    def list(self) -> str:
        return self.name

    def list_all(self, level: int = 0) -> str:
        return f"{'  ' * level}{self.name}\n"

    def count_files(self) -> int:
        return 1

    def count_all_files(self) -> int:
        return 1


class Directory(Component):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[Component] = []

    def add(self, component: Component):
        self.children.append(component)
        component.parent = self

    def list(self) -> str:
        return ', '.join(child.list() for child in self.children)

    def list_all(self, level: int = 0) -> str:
        result = f"{'  ' * level}{self.name}:\n"
        for child in self.children:
            result += child.list_all(level + 1)
        return result

    def change_dir(self, name: str):
        for child in self.children:
            if child.name == name and isinstance(child, Directory):
                return child
        return None

    def count_files(self) -> int:
        return sum(1 for child in self.children if isinstance(child, File))

    def count_all_files(self) -> int:
        return sum(child.count_all_files() for child in self.children)

    def up(self):
        return self.parent
