package org.example;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.function.Predicate;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) throws IOException {

        // done - prompt user for file to read
        // create decorator chain and prompt use which decorators to apply
        // (note that the use can select multiple decorations to apply
        // if the user selects TeeOutput, prompt for a file name to direct the output to.
        // if the user selects FilterOutput, give the user choice of at least two predicates
        // to choose from

        // each decorator will decorate the line


        Scanner sc = new Scanner(System.in);
        System.out.println("Enter file name to read from: ");
        String read_file_name = sc.nextLine();

        System.out.println("Enter a file name to write to:" );
        String write_file_name = sc.nextLine();

        // todo: finish writing the ui


        Writer writer = new FileWriter(write_file_name);
        Output streamOutput = new StreamOutput(writer);

        // remember that we can put any output type in these classes
        Output bracketOutput = new BracketOutput(streamOutput);
        Output numberedOutput = new NumberedOutput(streamOutput);
        Output teeOutput = new TeeOutput(streamOutput, writer);

        // todo: write some interesting predicates for filter
        Predicate<Object> nonEmptyString = o -> !o.toString().isEmpty();
        Predicate<Object> includesClassSubstring = o -> o.toString().contains("class");
        Predicate<Object> containsDigit = o -> Pattern.matches(".*[0-9].*", o.toString());


        Output filterOutput = new FilterOutput(bracketOutput, containsDigit);


        BufferedReader inputReader = new BufferedReader(new FileReader(read_file_name));
        String line = inputReader.readLine();


        while (line != null) {
            System.out.println(line);
            filterOutput.write(line); // write to file
            line = inputReader.readLine(); // read next line
        }

        inputReader.close();
        writer.close(); // close the file we write to

    }

}
