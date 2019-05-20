# Grader for pa1
Adapted from Joseph Politz, 2018

`json-graders/JSONRunner.java`
  
    This file runs the test suite in [insert test file] and prints the
    results in JSON format to standard out. The results map from test header to
    test output. For example:

    {'testAddTwoInts(SomeClassTester)':
     'expected:<6> but was:<11>',

     'testMultiplyTwoInts(SomeClassTester)':
     'expected:<12> but was:<8>'}

    Here the key may be longer than the message, and uniquely identifies
    the test method that was run. This file is copied over (in grade.py)
    into the local student ../../submission directory or
    /autograder/submission on Gradescope.

`pa1-implementation/`
  
  This directory holds any testing and reference implementation files

- `SomeClassTester.java`

  Contains JUnit tests on student methods they implement in the class `SomeClass`

- `RefSomeClass.java`

  Reference implementations of methods required of the students.
  For each test in `SomeClassTester.java`, a method from the student's submission
  is called, the corresponding reference method from this class is called, and
  the results are compared. This file is copied over (in `grade.py`) into the
  local student `../../submission` directory or `/autograder/submission`on Gradescope.

- `SomeClass.java`

  Solution for the assignment.
  
`grade`

  The entrypoint for the grader (called from `../run_autograder` on Gradescope). Calls `grade.py`.

`grade.py`

  This is where the real action happens. 

  The general layout proceeds as follows: check that all required student files
  were submitted, compile and run tests on student code, and generate the JSON
  output for Gradescope.

  `JSONRunner.java` will run `pa1-implementation/SomeClassTester.java` and emit the results for each 
  of tests in JSON, and then `grade.py` assigns scoring to generate the final
  report to be output in Gradescope. The JSON output is printed to the terminal when run locally,
  and written to `/autograder/results/results.json` when run on Gradescope.
