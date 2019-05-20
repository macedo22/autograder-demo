# Grader for pa1
Adapted from Joseph Politz, 2018

`json-graders/`
  `JSONRunner.java`
  
    This file runs the test suite in [insert test file] and prints the
    results in JSON format to standard out. The results map from test header to
    test output. For example:

    {'testAddTwoInts(SomeClassTester)':
     'expected:<6> but was:<11>',

     'testMultiplyTwoInts(SomeClassTester)':
     'expected:<12> but was:<8>'}

    Here the key may be longer than the message, and uniquely identifies
    the test method that was run. 

`pa1-implementation`
  
  This directory holds any reference implementation files

`grade`

  The entrypoint for the grader (called from `../run_autograder`). Calls `grade.py`.

`grade.py`

  This is where the real action happens. 

  The general layout proceeds as follows: check that all required student files
  were submitted, compile and run tests on student code, and generate the JSON
  output for Gradescope.

  `JSONRunner.java` will run `SomeClassTester.java` and emit the results for each 
  of tests in JSON, and then `grade.py` assigns scoring to generate the final
  report to be output in Gradescope.
