from database import Database
from _queue import Queue
from commands import AddCommand, UpdateCommand, RemoveCommand, MacroCommand, Invoker


def read_file(fname: str) -> str:
    """Reads file and returns data as a string."""
    f = open(fname, 'r')
    data = f.read()
    f.close()
    return data


def get_commands(data: str) -> list:
    """Gets commands from data and returns a list of commands."""
    commands = data.splitlines()
    return commands


def parse_commands(lines: list) -> tuple:
    """Parses commands and returns a queue of commands and a dictionary of databases."""
    command_queue = Queue()
    macro_stack = []
    databases = {}

    for line in lines:
        cmds = line.split(' ')
        cmd = cmds[0]

        if cmd == 'B':
            macro = MacroCommand()
            macro_stack.append(macro)
        elif cmd == 'E':
            if macro_stack:
                macro = macro_stack.pop()
                if macro_stack:
                    macro_stack[-1].add_command(macro)
                else:
                    command_queue.enqueue(macro)
        else:
            db_id = cmds[1]
            key = cmds[2]

            if cmd == 'A' or cmd == 'U':
                value = " ".join(cmds[3:])
            else:
                value = None

            if db_id not in databases:
                if cmd != 'U':
                    databases[db_id] = Database(db_id)
                else:
                    continue

            if cmd == 'A':
                command = AddCommand(databases[db_id], key, value)
            elif cmd == 'U':
                command = UpdateCommand(databases[db_id], key, value)
            elif cmd == 'R':
                command = RemoveCommand(databases[db_id], key)

            if macro_stack:
                macro_stack[-1].add_command(command)
            else:
                command_queue.enqueue(command)

    return command_queue, databases


def client(command_queue: Queue, databases: dict) -> None:
    """Simulates a client that executes commands."""
    invoker = Invoker()
    command_history = []

    for _ in command_queue:
        invoker.set_command(command_queue.peek())
        invoker.execute_command()
        command_history.append(command_queue.dequeue())

    print('Contents of Databases:')

    for db in databases.values():
        db.display(True)

    for _ in command_history[::-1]:
        invoker.set_command(command_history.pop())
        invoker.undo_command()

    print('Contents of Databases:')

    for db in databases.values():
        db.display(True)


def main() -> None:
    """Main driver function."""
    data = read_file(filename)
    commands = get_commands(data)
    command_queue, databases = parse_commands(commands)
    client(command_queue, databases)


if __name__ == '__main__':
    filename = 'commands.txt'
    main()
