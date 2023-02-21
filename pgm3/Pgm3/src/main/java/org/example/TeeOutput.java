package org.example;

import java.io.IOException;
import java.io.Writer;

//class TeeOutput implements Output {
//    private Output output1;
//    private Output output2;
//
//    public TeeOutput(Output output1, Output output2) {
//        this.output1 = output1;
//        this.output2 = output2;
//    }
//
//    public void write(Object o) {
//        output1.write(o);
//        output2.write(o);
//    }
//
//    public void writeString(String s) {
//        output1.writeString(s);
//        output2.writeString(s);
//    }
//}

class TeeOutput implements Output {
    private Output wrapped;
    private Writer otherOutput;

    public TeeOutput(Output wrapped, Writer otherOutput) {
        this.wrapped = wrapped;
        this.otherOutput = otherOutput;
    }

    public void write(Object o) {
        writeString(o.toString());
    }

    public void writeString(String s) {
        this.wrapped.write(s);
        try {
            otherOutput.write(s);
        }
        catch (IOException ex) {
            throw new RuntimeException(ex);
        }
    }
 }