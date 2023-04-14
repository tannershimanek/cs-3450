from abc import ABC, abstractmethod
from typing import List


# Visitor base class
class ComponentVisitor(ABC):
    @abstractmethod
    def visit_file(self, file):
        pass

    @abstractmethod
    def visit_directory(self, directory):
        pass


# Derived Visitor classes
class ListVisitor(ComponentVisitor):
    def visit_file(self, file):
        return file.name

    def visit_directory(self, directory):
        return ', '.join(child.accept(self) for child in directory.children)


class ListAllVisitor(ComponentVisitor):
    def __init__(self, level: int = 0):
        self.level = level

    def visit_file(self, file):
        return f"{'  ' * self.level}{file.name}\n"

    def visit_directory(self, directory):
        result = f"{'  ' * self.level}{directory.name}:\n"
        for child in directory.children:
            visitor = ListAllVisitor(self.level + 1)
            result += child.accept(visitor)
        return result


class CountVisitor(ComponentVisitor):
    def visit_file(self, file):
        return 1

    def visit_directory(self, directory):
        return sum(child.accept(self) for child in directory.children)


class CountAllVisitor(ComponentVisitor):
    def visit_file(self, file):
        return 1

    def visit_directory(self, directory):
        return sum(child.accept(CountAllVisitor()) for child in directory.children)


# Component hierarchy
class Component(ABC):
    def __init__(self, name: str):
        self.name = name
        self.parent = None

    @abstractmethod
    def accept(self, visitor: ComponentVisitor):
        pass


class File(Component):
    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_file(self)


class Directory(Component):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[Component] = []

    def add(self, component: Component):
        self.children.append(component)
        component.parent = self

    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_directory(self)

    def change_dir(self, name: str):
        for child in self.children:
            if child.name == name and isinstance(child, Directory):
                return child
        return None

    def up(self):
        return self.parent
