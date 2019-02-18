import fnmatch
import os
import json
from subprocess import call, check_output
import subprocess
from helper_methods import check_files_exist, get_jdk11_path, output_score

STUDENT_PKG = "cse599pa1student"

# TODO confirm tests

####################################################################################################
# GET CORRECT PATHS
####################################################################################################

# get correct paths for javac and java
jdk11_path = get_jdk11_path(["/home/sophia/", "/home/alex/" ])
JAVA_PATH= jdk11_path + "jdk-11/bin/java"
JAVAC_PATH= jdk11_path + "jdk-11/bin/javac"

# get correct path for student submission
if(os.path.isdir("/autograder/results")):
  STUDENT_PATH = "/autograder/submission/pa1-starter-w19/src/" # AUTOGRADER_SUBMISSION_PATH
else:
  STUDENT_PATH = "../../submission/pa1-starter-w19/src/" # LOCAL_SUBMISSION_PATH

# remove any student .class files
if os.path.isdir(STUDENT_PATH + "cse599pa1student"):
    for file in os.listdir(STUDENT_PATH + "cse599pa1student"):
        if fnmatch.fnmatch(file, '*.class'):
            call(["rm", STUDENT_PATH + "cse599pa1student/" + file])

# Remove src/ to get readme path
README_PATH = STUDENT_PATH[:-4]

BASE_CLASSPATH="src/:lib/gson-2.8.2.jar:lib/hamcrest-core-1.3.jar:lib/junit-4.12.jar"

####################################################################################################
# CHECK TO SEE IF ALL STUDENT FILES REQUIRED FOR PA6 EXIST
####################################################################################################

# All paths in student submission to confirm all exist.
REQUIRED_FILES = ["Someclass.java"]

missing_files = check_files_exist(README_PATH, STUDENT_PATH + STUDENT_PKG, REQUIRED_FILES)

####################################################################################################
# START TESTING
####################################################################################################
refTestSolverspath = os.path.join("./pa1tests/MethodTest.java")

RUNNER = os.path.join("src", "cse599pa1grading", "grader", "JSONRunner.java")
ALLJAVA = os.path.join("src", "cse599pa1grading", "grader", "*.java")
RUNNERCLASS = os.path.join("cse599pa1grading", "grader", "JSONRunner")

def test_on():
  impl_name = STUDENT_PATH
  impl_classpath = BASE_CLASSPATH + ":" + impl_name + "/"
  copy_dir = os.path.join(STUDENT_PATH, STUDENT_PKG)
  call(["cp",refTestSolverspath,copy_dir])
  out, err = subprocess.Popen(" ".join([JAVAC_PATH, "-cp", impl_classpath, ALLJAVA]),
                     stdout=subprocess.PIPE,
                     stdin=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     shell=True).communicate("")
  compiler_out = err
  if compiler_out != "": return compiler_out # Indicates some compile error

  out, err = subprocess.Popen(" ".join([JAVA_PATH, "-cp", impl_classpath, RUNNERCLASS, "./out_tests.json"]),
										 stdout=subprocess.PIPE,
										 stdin=subprocess.PIPE,
										 stderr=subprocess.PIPE,
										 shell=True).communicate("")
  run_err = err
  run_out = out
  results_str = run_out
  if run_err != "": return run_out + "\n" + run_err

  f = open("./out_tests.json","r")
  results_str = f.read()
  f.close()

  return json.loads(results_str)


####################################################################################################
# Test student implementations
####################################################################################################
test_points = {
  "testAddTwoInts": 1,
  "testMultiplyTwoInts": 1,
  "testSumIntArray": 1,
  "testConcatStringArray": 1,
}

imp_failures = test_on()
print(imp_failures)

if type(imp_failures) == str:
  total_score = {
    "score": 0,
    "output": "Your implementation failed to compile/run with the following message:\n\n" + imp_failures,
    'tests': missing_files
  }
else:
  imp_parts = []
  for (name, pts) in test_points.iteritems():
    name += "(cse599pa1student.MethodTest)"
    if not(name in imp_failures):
      imp_parts.append({
        'score': pts,
        'name': name,
        'output': 'Passed this test. [%s/%s]' % (pts, pts)
      })
    else:
      imp_parts.append({
        'score': 0,
        'name': name,
        'output': 'Failed this test. [%s/%s]\n%s' % (0, pts, imp_failures[name])
      })
  total_score = {
    'output': "Note that this just gives you success/failure information on several tests - passing all of these does NOT mean you get full credit on the assignment. These are a subset of the tests we'll use to grade your submission that help you get feedback on where you might be making a mistake.",
    'tests': missing_files + imp_parts
  }

################################################################################################
# Print results.json
################################################################################################
output_score(total_score)
