package cse12pa6grading.grader;

import java.util.List;

class Grade {
	public Grade(String output, List<GradePart> tests) {
		super();
		this.output = output;
		this.tests = tests;
	}

	String output;
	List<GradePart> tests;
}
