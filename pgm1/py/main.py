import Implementation
import Queue


def main():
    # Do ints
    print("Test 1:")
    LL = Implementation.LinkedList()
    DA = Implementation.DynamicArray()
    
    q = Queue.Queue(DA)
    q.add(91)
    q.add(92)
    LL.add(93)
    q.change_impl(LL)
    q.add(94)
    q.add(95)
    q.print_queue()
    q.clear()

    # Do strings
    print("Test 2:")
    l = Implementation.LinkedList()
    a = Implementation.DynamicArray()

    a.add("Discard Me")
    q2 = Queue.Queue(a)
    q2.add("91")
    q2.add("92")
    l.add("93")
    q2.change_impl(l)
    q2.add("94")
    q2.add("95")
    q2.print_queue()
    q2.clear()


if __name__ == "__main__":
    main()
