package org.example;

import java.util.function.Predicate;

class FilterOutput implements Output {
    private Output output;
    private Predicate<Object> filter;

    public FilterOutput(Output output, Predicate<Object> filter) {
        this.output = output;
        this.filter = filter;
    }

    public void write(Object o) {
        if (filter.test(o)) {
            writeString(o.toString());
        }
    }

    public void writeString(String s) {
        output.write(s);
    }
}