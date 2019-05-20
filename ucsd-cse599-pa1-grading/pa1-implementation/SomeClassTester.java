import static org.junit.Assert.*;
import org.junit.*;
import java.util.Arrays;

public class SomeClassTester {
    final int timeLimit = 30000;

    @Test(timeout = timeLimit)
    public void testAddTwoInts(){
        int studentResult = SomeClass.addTwoInts(5, 3);
        int refResult = RefSomeClass.addTwoInts(5, 3);
        assertEquals(refResult, studentResult);
    }

    @Test(timeout = timeLimit)
    public void testMultiplyTwoInts(){
        int studentResult = SomeClass.multiplyTwoInts(7, 2);
        int refResult = RefSomeClass.multiplyTwoInts(7, 2);
        assertEquals(refResult, studentResult);
    }

    @Test(timeout = timeLimit)
    public void testSumIntArray(){
        int[] arr = {1, 2, 3, 4};
        int studentResult = SomeClass.sumIntArray(arr);
        int refResult = RefSomeClass.sumIntArray(arr);
        assertEquals(refResult, studentResult);
    }

    @Test(timeout = timeLimit)
    public void testConcatStringArray(){
        String[] arr = {"Concat", "These", "Strings"};
        String studentResult = SomeClass.concatStringArray(arr);
        String refResult = RefSomeClass.concatStringArray(arr);
        assertEquals(refResult, studentResult);
    }
}
