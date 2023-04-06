from composite import Directory, File


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
