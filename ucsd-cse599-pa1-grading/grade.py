import fnmatch
import os
import json
from subprocess import call, check_output
import subprocess
from helper_methods import check_files_exist, output_score

####################################################################################################
# GET CORRECT PATHS
####################################################################################################

# get correct paths for javac and java
JAVA_PATH= 'java'
JAVAC_PATH= 'javac'

# get correct path for student submission
if(os.path.isdir('/autograder/results')):
    STUDENT_PATH = '/autograder/submission/' # AUTOGRADER_SUBMISSION_PATH
else:
    STUDENT_PATH = '../../submission/' # LOCAL_SUBMISSION_PATH

# remove any student .class files
if os.path.isdir(STUDENT_PATH):
    for file in os.listdir(STUDENT_PATH):
        if fnmatch.fnmatch(file, '*.class'):
            call(['rm', STUDENT_PATH + '/' + file])

BASE_CLASSPATH='.:lib/gson-2.8.2.jar:lib/hamcrest-core-1.3.jar:lib/junit-4.12.jar'
REFIMP = './pa1-implementation/'

####################################################################################################
# CHECK TO SEE IF ALL STUDENT FILES REQUIRED FOR PA1 EXIST
####################################################################################################

# All paths in student submission to confirm all exist.
REQUIRED_FILES = ['SomeClass.java']
missing_files = check_files_exist(STUDENT_PATH, REQUIRED_FILES)
all_tests = missing_files

####################################################################################################
# START TESTING
####################################################################################################


def copy_files_to_student_submission(file_names):
    for file in file_names:
        call(['cp', os.path.join(REFIMP, file), STUDENT_PATH])


# Check that student code compiles successfully
def compile_test(classpath, files_to_compile):
    javac_command = [JAVAC_PATH, '-cp', classpath]
    javac_command.extend(files_to_compile)
    call_output = open('stderr', 'w')
    exit_code = call(javac_command, stdout=call_output, stderr=call_output)
    print("Exit code from compiling %s: %d" % (files_to_compile, exit_code))

    if exit_code == 0:
        return {}
    else:
        studentCompileError = open('stderr').read()
        return studentCompileError


# Run tests on student code
def run(RUNNER, RUNNERCLASS, files_to_copy, files_to_compile):
    classpath = STUDENT_PATH + ':' + BASE_CLASSPATH
    call(["cp", os.path.join('./json-graders/' + RUNNER), STUDENT_PATH])
    copy_files_to_student_submission(files_to_copy)
    files_to_compile.append(STUDENT_PATH + RUNNER)
    compile_result = compile_test(classpath, files_to_compile)

    if type(compile_result) == str:
        return compile_result
    else:
        check_output([JAVA_PATH, '-cp', classpath, RUNNERCLASS, './out_tests.json'])
        f = open('./out_tests.json','r')
        results_str = f.read()
        f.close()
        return json.loads(results_str)


# Get JSON output of autograder tests
def get_student_output(test_failures, test_points, test_location):
    student_results = []
    if type(test_failures) == str:
        student_results.append({
            'score': 0,
            'name': 'Compile Error (%s)' % test_location,
            'output': 'Your implementation failed to compile with the following message:\n\n' + test_failures,
        })
    else:
        for (name, pts) in test_points.iteritems():
            name += ('(%s)' % test_location)
            if not(name in test_failures):
                student_results.append({
                    'score': pts,
                    'name': name + ' [Passed]',
                    'output': 'Passed this test!'
                })
            else:
                failure_msg = test_failures[name]
                if 'No X11 DISPLAY variable was set' in failure_msg:
                    failure_msg = 'Please remove any calls to the explore or play method from this method'
                student_results.append({
                    'score': 0,
                    'name': name + ' [Failed]',
                    'output': 'Failed this test with the following message: \n\n' + failure_msg
                })
    student_results = sorted(student_results, key=lambda k: k['name'])
    return student_results


####################################################################################################
# Test student SomeClass method implementations
####################################################################################################

some_class_points = {
    'testAddTwoInts': 1,
    'testMultiplyTwoInts': 1,
    'testSumIntArray': 1,
    'testConcatStringArray': 1
}

some_class_failures = run(
    'JSONRunner.java',
    'JSONRunner',
    ['SomeClassTester.java', 'RefSomeClass.java'],
    [STUDENT_PATH + 'SomeClass.java', STUDENT_PATH + 'RefSomeClass.java', STUDENT_PATH + 'SomeClassTester.java'])
some_class_output = get_student_output(some_class_failures, some_class_points, 'SomeClassTester')
all_tests += some_class_output

################################################################################################
# Print results.json
################################################################################################

total_score = {
    'output': ('Grading Summary:\n \n'
               + " Ensure that you've submitted all required files and that"
               + " your code compiles to receive credit. The autograder has run 1 test on"
               + " each of your 4 methods. If you fail one of the 4 method tests below,"
               + " the output message will show the comparison between the expected output"
               + " and the output generated by your method."
               + "\n \n Autograding [4 points] \n"
               + " (1 point) for passing each method test"
               + "\n \n Manual Grading [2 points] \n"
               + " Commenting and style: your methods must have proper headers and files"
               + " must have consistent indentation."),
    'tests': all_tests
}
output_score(total_score)
