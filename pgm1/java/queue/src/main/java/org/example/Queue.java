package org.example;
import java.util.List;

public class Queue<T> {
    private List<T> list;

    public Queue(List<T> list) {
        if (list.size() > 0) { list.clear(); }
        this.list = list;
    }

    public void add(T t) {
        list.add(t);
    }

    public T get() {
        return list.get(0);
    }

    public T remove() {
        return list.remove(0);
    }

    public int size() {
        return list.size();
    }

    public void clear() {
        list.clear();
    }

    public void print() {
        System.out.println(list);
    }

    public void changeImpl(List<T> newList) {
        newList.clear();
        newList.addAll(list);
        list = newList;
    }
}
