package org.example;
import java.util.ArrayList;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
//        Queue<String> queue = new Queue<>(new ArrayList<>());
//        queue.add("one");
//        queue.add("two");
//        queue.add("three");
//        System.out.println(queue.get());
//        System.out.println(queue.remove());
//        System.out.println(queue.size());
//        System.out.println(queue.get());
//        queue.clear();
//        System.out.println(queue.size());
//
//        Queue<String> queue2 = new Queue<>(new LinkedList<>());
//        queue2.add("one");
//        queue2.add("two");
//        queue2.add("three");
//        System.out.println(queue2.get());
//        System.out.println(queue2.remove());
//        System.out.println(queue2.size());
//        System.out.println(queue2.get());
//        queue2.clear();
//        System.out.println(queue2.size());

        Queue q = new Queue(new ArrayList());
        q.add(91);
        q.add(92);

        LinkedList alist = new LinkedList();
        alist.add(93);

        q.changeImpl(alist);
        q.add(94);
        q.add(95);

        displayAndEmptyQueue(q);

        // Do strings
//        ArrayList a = newArrayList();
//        a.add("Discard Me");
//        Queue q2 = new Queue(a);
//        q2.add("91");
//        q2.add("92");
//        LinkedList alist2 = new LinkedList();
//        alist2.add("93");
//        q2.changeImpl(alist2);
//        q2.add("94");
//        q2.add("95");
//        displayAndEmptyQueue(q2);
    }

    public static void displayAndEmptyQueue(Queue q) {
        q.print();
        q.clear();
    }
}