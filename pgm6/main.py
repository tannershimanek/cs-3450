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



def parse_file(filename: str) -> Directory:
    stack = []
    current_indent = 0
    previous_indent = -1

    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            current_indent = len(line) - len(line.lstrip())
            if line.endswith(":"):
                # Create a new directory
                name = line.strip(" :")
                new_dir = Directory(name)

                if stack:
                    stack[-1].add(new_dir)
                stack.append(new_dir)
            else:
                # Create a new file
                name = line.strip()
                new_file = File(name)
                stack[-1].add(new_file)

            # Check if the indent decreased, and pop directories accordingly
            if current_indent < previous_indent:
                for _ in range((previous_indent - current_indent) // 3):
                    stack.pop()
            previous_indent = current_indent
    return stack[0]


def start_prompt(current_dir):
    while True:
        command = input(f"{current_dir.name}> ").strip().lower().split(' ')
        action = command[0]
        args = command[1:]

        if action == 'list':
            print(current_dir.list())
        elif action == 'listall':
            print(current_dir.list_all())
        elif action == 'chdir':
            if args:
                new_dir = current_dir.change_dir(args[0])
                if new_dir:
                    current_dir = new_dir
                else:
                    print(f"Cannot find the directory '{args[0]}'.")
            else:
                print("Please provide a directory name.")
        elif action == 'up':
            parent = current_dir.up()
            if parent:
                current_dir = parent
            else:
                print("Already at the top directory.")
        elif action == 'count':
            print(current_dir.count_files())
        elif action == 'countall':
            print(current_dir.count_all_files())
        elif action == 'q':
            break
        else:
            print("Invalid command.")


def main():
    current_dir = parse_file("directory.dat")
    # current_dir = parse_file("MyProg6TESTdirectory.dat")
    start_prompt(current_dir)


if __name__ == "__main__":
    main()
