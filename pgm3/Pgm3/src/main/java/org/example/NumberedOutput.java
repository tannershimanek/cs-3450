package org.example;

import java.io.IOException;
import java.io.Writer;

public class NumberedOutput implements Output {

    protected Output stream;
    private int lineNumber = 1;
    public NumberedOutput(Output stream) {
        this.stream = stream;
    }

    @Override
    public void write(Object o) {
        String numberedLine = String.format("%5d: ", lineNumber++);
        String parsedLine = numberedLine + o.toString();
        writeString(parsedLine);
    }

    @Override
    public void writeString(String s) {
        stream.write(s);
    }


//    private int lineNumber = 1;
//    public NumberedOutput(Writer stream) {
//        super(stream);
//    }
//
//    @Override
//    public void write(Object o) {
//        String numberedLine = String.format("%d: ", lineNumber++);
//        String parsedLine = numberedLine + o.toString();
//        writeString(parsedLine);
//    }

}
