# autograder-demo

**See Joe Politz's setup recommendations: https://github.com/ucsd-cse12-w17/pa-grading**

To run this autograder locally:

1) Clone this repository and create a local directory named `submission` in
   the same directory that this cloned repository exists.
2) Put sample student submission files within this `submission` directory. This
   file structure imitates the file structure Gradescope uses.
3) To execute, run `bash ucsd-cse599-pa1-grading/grade` from within the top
   directory of this repository.

`run_autograder`

  Entry point for the autograder on Gradescope. This is set up to clone this 
  repository and call `ucsd-cse599-pa1-grading/grade`. This is a file
  *required* by the autograder to run. Every time the autograder is run on a
  student submission on Gradescope, a new AWS instance is created and the repo
  is cloned again. This allows the autograder to essentially update in real
  time if new commits are made to this repository.
  
`setup.sh`

  Installs dependencies. This is a file *required* by the autograder to run.

`build-for-gradescope.sh`

  A helper script for creating the zip file required for configuring the
  autograder on Gradescope. Takes the path to a private id_rsa ssh key and zips
  it along with `setup.sh`, `config`, and `run_autograder` into `pa.zip`.
