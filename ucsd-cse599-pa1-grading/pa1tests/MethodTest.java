package cse599pa1student;

import static org.junit.Assert.*;
import org.junit.*;

import java.util.Arrays;

public class MethodTest {
	final int timeLimit = 10000;

	@Test(timeout = timeLimit)
	public void testAddTwoInts(){
		int result = SomeClass.addTwoInts(5, 3);
		assertEquals(result, 8);
	}

	@Test(timeout = timeLimit)
	public void testMultiplyTwoInts(){
		int result = SomeClass.multiplyTwoInts(2, 2);
		assertEquals(result, 4);
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
