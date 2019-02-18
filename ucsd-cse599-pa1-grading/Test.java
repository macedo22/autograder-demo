package pa1tests;

import static org.junit.Assert.*;
import org.junit.*;

import java.util.Arrays;

public class LoaderTest {
	final int timeLimit = 60000;

	@Test(timeout = timeLimit)
	public void testAddTwoInts(){
		int result = SomeClass.addTwoInts(5, 3);
		assertEquals(result, 8);
	}

	@Test(timeout = timeLimit)
	public void testMultiplyTwoInts(){
		int result = SomeClass.multiplyTwoInts(-1, 7);
		assertEquals(result, -7);
	}

	@Test(timeout = timeLimit)
	public void testSumIntArray(){
		int[] arr = {1, 2, 3, 4};
		int result = SomeClass.sumIntArray(arr);
		assertEquals(result, 10);
	}

	@Test(timeout = timeLimit)
	public void testConcatStringArray(){
		String[] arr = {"Concat", "These", "Strings"};
		String result = SomeClass.concatStringArray(arr);
		assertEquals(result, "ConcatTheseStrings");
	}

}
