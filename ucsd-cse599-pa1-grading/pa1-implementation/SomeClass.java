import java.util.Arrays;

public class SomeClass {

    static int addTwoInts(int a, int b) {
        return a + b;
	}

    static int multiplyTwoInts(int a, int b) {
        return a * b;
    }

    static int sumIntArray(int[] arr){
        int sum = 0;
        for(int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        return sum;
    }

    static String concatStringArray(String[] arr) {
        int i = 0;
        String concatString = "";
        while(i < arr.length) {
            concatString += arr[i];
            i++;
        }
        return concatString;
    }
}
