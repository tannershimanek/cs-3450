from iterator import MyArray, FilterIterator, ReverseIterator


def example_1(array: MyArray):
    """FilterIterator that returns even integers."""
    print("Example 1: Filter even integers")
    iterator_1 = array.get_iterator()
    filter_iterator_1 = FilterIterator(
        iterator_1, lambda x: isinstance(x, int) and x % 2 == 0)
    filter_iterator_1.first()
    while not filter_iterator_1.is_done():
        print('  ', filter_iterator_1.current())
        filter_iterator_1.next()


def example_2(array: MyArray):
    """FilterIterator filtering results from another FilterIterator."""
    print("\nExample 2: filtering results from another FilterIterator")
    iterator_2 = array.get_iterator()
    filter_iterator_2 = FilterIterator(
        iterator_2, lambda x: isinstance(x, int))
    filter_iterator_2_2 = FilterIterator(
        filter_iterator_2, lambda x: x % 2 == 0)
    filter_iterator_2_2.first()
    while not filter_iterator_2_2.is_done():
        print('  ', filter_iterator_2_2.current())
        filter_iterator_2_2.next()


def example_3(array: MyArray):
    """FilterIterator that filters out everything."""
    print("\nExample 3: Filter everything")
    iterator_3 = array.get_iterator()
    filter_iterator_3 = FilterIterator(iterator_3, lambda x: False)
    filter_iterator_3.first()
    while not filter_iterator_3.is_done():
        print('  ', filter_iterator_3.current())
        filter_iterator_3.next()


def example_4(array: MyArray):
    """ReverseIterator."""
    print("\nExample 4: Reverse order")
    iterator_4 = array.get_iterator()
    reverse_iterator_1 = ReverseIterator(iterator_4)
    reverse_iterator_1.first()
    while not reverse_iterator_1.is_done():
        print('  ', reverse_iterator_1.current())
        reverse_iterator_1.next()


def example_5(array: MyArray):
    """ReverseIterator that takes a FilterIterator."""
    print("\nExample 5: Reverse order after filtering")
    iterator_5 = array.get_iterator()
    filter_iterator_4 = FilterIterator(
        iterator_5, lambda x: isinstance(x, int) and x % 2 == 0)
    reverse_iterator_2 = ReverseIterator(filter_iterator_4)
    reverse_iterator_2.first()
    while not reverse_iterator_2.is_done():
        print('  ', reverse_iterator_2.current())
        reverse_iterator_2.next()


def main():
    my_array = MyArray(6)
    my_array.add(0)
    my_array.add('one')
    my_array.add(2)
    my_array.add('three')
    my_array.add(4)
    my_array.add('five')

    # Example 1: FilterIterator that returns even integers
    example_1(my_array)
    # Example 2: FilterIterator filtering results from another FilterIterator
    example_2(my_array)
    # Example 3: FilterIterator that filters out everything
    example_3(my_array)
    # Example 4: ReverseIterator
    example_4(my_array)
    # Example 5: ReverseIterator that takes a FilterIterator
    example_5(my_array)


if __name__ == "__main__":
    main()
