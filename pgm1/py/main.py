import Implementation


def main():
    arr = Implementation.DynamicArray()
    arr.add(1)
    arr.add(2)
    print(arr.__str__())
    print(arr.size())
    print(arr.get())
    arr.remove(1)
    print(arr.__str__())


if __name__ == "__main__":
    main()
