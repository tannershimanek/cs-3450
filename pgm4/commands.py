from abc import ABC, abstractmethod


class Command(ABC):
    """Command interface. All commands must implement this interface."""

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class AddCommand(Command):
    """Command to add a key-value pair to a database."""

    def __init__(self, database, key, value):
        self.database = database
        self.key = key
        self.value = value

    def execute(self):
        if self.key not in self.database.data:
            self.database.add(self.key, self.value)
        else:
            raise Exception('Key already in database')

    def undo(self):
        if self.key in self.database.data:
            self.database.remove(self.key)
        else:
            raise Exception('Key not in database')

    def get_name(self):
        return 'AddCommand'


class UpdateCommand(Command):
    """Command to update a key-value pair in a database."""

    def __init__(self, database, key, value):
        self.database = database
        self.key = key
        self.value = value
        self.previous_value = None

    def execute(self):
        if self.key in self.database.data:
            self.previous_value = self.database.get(self.key)
            self.database.update(self.key, self.value)
        else:
            raise Exception('Key not in database')

    def undo(self):
        if self.key in self.database.data:
            self.database.update(self.key, self.previous_value)
        else:
            raise Exception('Key not in database')

    def get_name(self):
        return 'UpdateCommand'


class RemoveCommand(Command):
    """Command to remove a key-value pair from a database."""

    def __init__(self, database, key):
        self.database = database
        self.key = key
        self.value = None

    def execute(self):
        if self.key in self.database.data:
            self.value = self.database.get(self.key)
            self.database.remove(self.key)
        else:
            raise Exception('Key not in database')

    def undo(self):
        if self.key not in self.database.data:
            self.database.add(self.key, self.value)
        else:
            raise Exception('Key already in database')

    def get_name(self):
        return 'RemoveCommand'


class MacroCommand(Command):
    """Command to execute a series of commands."""

    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute(self):
        print('Beginning a macro')
        for command in self.commands:
            command.execute()
        print('Ending a macro\n')

    def undo(self):
        print('Begin Undoing a macro\n')
        for command in reversed(self.commands):
            command.undo()
            print(f'Undid {command.get_name()}')
            command.database.display()
        print('End Undoing a macro')

    def get_name(self):
        return 'MacroCommand'


class Invoker:
    """Invoker class that executes commands."""

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        if self.command is not None:
            self.command.execute()
        else:
            raise Exception('No command set')

    def undo_command(self):
        if self.command is not None:
            if self.command.get_name() != 'MacroCommand':
                print(f'Undid {self.command.get_name()}')
            self.command.undo()
            if self.command.get_name() != 'MacroCommand':
                self.command.database.display()
        else:
            raise Exception('No command set')
