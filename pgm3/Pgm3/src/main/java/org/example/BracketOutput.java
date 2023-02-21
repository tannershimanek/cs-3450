package org.example;

import java.io.Writer;

public class BracketOutput implements Output {

    protected Output stream;
    public BracketOutput(Output stream) {
//        super(stream);
        this.stream = stream;

    }

    @Override
    public void write(Object o) {
        String s = "[" + o.toString() + "]\n";
        writeString(s);
    }

    @Override
    public void writeString(String s) {
        stream.write(s);
    }

}


//public class BracketOutput implements Output {
//
//    protected StreamOutput stream;
//    public BracketOutput(StreamOutput stream) {
////        super(stream);
//        this.stream = stream;
//
//    }
//
//    @Override
//    public void write(Object o) {
//        String s = "[" + o.toString() + "]\n";
//        writeString(s);
//    }
//
//    @Override
//    public void writeString(String s) {
//        stream.write(s);
//    }
//
//}
