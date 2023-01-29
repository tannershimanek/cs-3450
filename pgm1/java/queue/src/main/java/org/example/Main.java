package org.example;
import java.util.ArrayList;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        // Do ints
        Queue<Integer> q = new Queue<>(new ArrayList<>());
        q.add(91);
        q.add(92);
        LinkedList<Integer> alist = new LinkedList<>();
        alist.add(93);
        q.changeImpl(alist);
        q.add(94);
        q.add(95);
        displayAndEmptyQueue(q);

        // Do strings
        ArrayList<String> a = new ArrayList<>();
        a.add("Discard Me");
        Queue<String> q2 = new Queue<>(a);
        q2.add("91");
        q2.add("92");
        LinkedList<String> alist2 = new LinkedList<>();
        alist2.add("93");
        q2.changeImpl(alist2);
        q2.add("94");
        q2.add("95");
        displayAndEmptyQueue(q2);
    }

    public static void displayAndEmptyQueue(Queue q) {
        q.print();
        q.clear();
    }
}