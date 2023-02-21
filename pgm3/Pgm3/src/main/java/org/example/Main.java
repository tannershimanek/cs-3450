package org.example;

import java.io.*;
import java.util.*;
import java.util.function.Predicate;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) throws IOException {
        // file to read from should be 'decorator.dat'
        // file to write to should be 'output.txt'
        // however, if you leave the file names blank, the program will ask you for them.
        writeFile("", "");
    }

    public static void writeFile(String read_file_name, String write_file_name) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (Objects.equals(read_file_name, "") || Objects.equals(write_file_name, "")) {

            System.out.println("Enter file name to read from: ");
            read_file_name = sc.nextLine();

            System.out.println("Enter a file name to write to:" );
            write_file_name = sc.nextLine();
        }

        System.out.println("Select decorators to apply (separate by space): ");
        System.out.println("1. BracketOutput, 2. NumberedOutput, 3. TeeOutput, 4. FilterOutput");
        String options = sc.nextLine();


        String[] optionsArray = options.split(" ");

        Writer writer = new FileWriter(write_file_name);
        Output streamOutput = new StreamOutput(writer); // this is the base class that we will decorate

        String filterOption = "";
        boolean useFilterDecorator = useFilter(optionsArray);

        if (useFilterDecorator) {
            System.out.println("Select a filter to apply: ");
            System.out.println("1. nonEmptyString, 2. includesClassSubstring, 3. containsDigit, 4. containsCharA");
            filterOption = sc.nextLine();
            System.out.println(filterOption);
        }
        // reverse(optionsArray);
        Output output = decorate(streamOutput, optionsArray, writer, 0, filterOption);
        BufferedReader inputReader = new BufferedReader(new FileReader(read_file_name));
        String line = inputReader.readLine();


        while (line != null) {
            System.out.println(line);
            output.write(line); // write to file
            line = inputReader.readLine(); // read next line
        }

        inputReader.close();
        writer.close(); // close the file we write to
    }

    public static Output decorate(Output output, String[] optionArray, Writer writer, int count, String filterOption){
        if (count == optionArray.length) {
            return output;
        }

        return switch (optionArray[count]) {
            case "1" -> decorate(new BracketOutput(output), optionArray, writer, count + 1, filterOption);
            case "2" -> decorate(new NumberedOutput(output), optionArray, writer, count + 1, filterOption);
            case "3" -> decorate(new TeeOutput(output, writer), optionArray, writer, count + 1, filterOption);
            case "4" ->
                    switch (filterOption) {
                        case "1" -> decorate(new FilterOutput(output, nonEmptyString), optionArray, writer, count + 1, filterOption);
                        case "2" -> decorate(new FilterOutput(output, includesClassSubstring), optionArray, writer, count + 1, filterOption);
                        case "3" -> decorate(new FilterOutput(output, containsDigit), optionArray, writer, count + 1, filterOption);
                        case "4" -> decorate(new FilterOutput(output, containsCharA), optionArray, writer, count + 1, filterOption);
                        default -> output;
                    };
            default -> output;
        };

    }


    public static void reverse(String[] array) {
        int left = 0;
        int right = array.length - 1;
        while (left < right) {
            String temp = array[left];
            array[left] = array[right];
            array[right] = temp;
            left++;
            right--;
        }
    }

    public static boolean useFilter(String[] options) {
        for (String option : options) {
            if (option.equals("4")) {
                return true;
            }
        }
        return false;
    }

    public static Predicate<Object> nonEmptyString = o -> !o.toString().isEmpty();
    public static Predicate<Object> includesClassSubstring = o -> o.toString().contains("class");
    public static Predicate<Object> containsDigit = o -> Pattern.matches(".*[0-9].*", o.toString());
    public static Predicate<Object> containsCharA = o -> Pattern.matches(".*[aA].*", o.toString());
}
