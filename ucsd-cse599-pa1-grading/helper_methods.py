import os
import json


def replaceStringInFile(path, filename, stringToReplace, stringReplacement):
    studentFile = open(path).read()

    # Replace string
    studentFileUpdated = studentFile.replace(stringToReplace, stringReplacement)

    # Write the file out again
    with open(path, 'w') as file:
        file.write(studentFileUpdated)

     # return the name of the file if it contains print statements
    if stringToReplace in studentFile:
        return filename + ', '
    return ''


def check_file_exists(submission_path, file_name):
    path = os.path.join(submission_path, file_name)
    if not(os.path.exists(path)):
        return file_name + ', '
    else:
        return ''


def check_files_exist(submission_path, files_array, additional_msg = ""):
    missing_files = ""
    for file in files_array:
        missing_files += check_file_exists(submission_path, file)

    # Update final output for missing files
    if len(missing_files) > 0:
        missing_files = "Missing files: " + missing_files[0:-2] + '\n\n' + additional_msg  # remove trailing comma and whitespace
    else:
        missing_files = 'All required files have been found.' + '\n\n' + additional_msg

    missing_files = [{
        'score': 0,
        'max': 0,
        'name': 'Checking for any MISSING FILES: if any files are missing, please'
                + ' confirm you have uploaded the correct files, with the correct'
                + ' file paths and names.',
        'output': missing_files
    }]

    return missing_files


def output_score(total_score):
    if(os.path.isdir('/autograder/results')):
        resultsjson = open('/autograder/results/results.json','w')
        resultsjson.write(json.dumps(total_score))
        resultsjson.close()
    else:
        print("local test")
    	print json.dumps(total_score, indent=4, sort_keys=True)
