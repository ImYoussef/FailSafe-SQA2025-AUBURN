# COMP 5710 Term Project

Cameron Kasprzak
Youssef Mousallam
Adrian Rushing

## Activities

All source files, commit history, changelogs, output files as well as additional information contained in README’s can be found on the team GitHub repository here: https://github.com/ImYoussef/FailSafe-SQA2025-AUBURN/tree/main

### Execution of Git Hooks

The following artifacts are designed to provide evidence of successful integration and validation of requirement “4a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. (10%)”. As the pre-commit hook is a client-side hook, the contents of it are not stored on the Team’s Repository per standard Git practice. Instead the pre-commit hook file is simply uploaded in a separate folder labeled “hooks”

### Execution of Fuzzing

To automatically execute the fuzzing, we created a GitHub action 'fuzz.yml' which automatically installs required packages and runns the *fuzz.py* file. The results of this can be found here: https://github.com/ImYoussef/FailSafe-SQA2025-AUBURN/actions

## Screenshots and Logs

This section of the report contains screenshots and snippets of log files that demonstrates the team members successfully integrated and validated all the requirements found here: https://github.com/ImYoussef/FailSafe-SQA2025-AUBURN/tree/main/Screenshots

## Fuzzed Methods

### scanUserNameFuzzer() - _Adrian Rushing_

The scanUserNameFuzzer() method in scanner.py looks through an array of user names to see if they are valid. If they meet a series of conditions then they are appended to a list of hard-coded unames to be output at the end of the method. The function would crash when val_list was none, so to prevent because that object is not iterable.

### checkIfValidK8SYamlFuzzer() - _Adrian Rushing_

The checkIfValidK8SYamlFuzzer() method in parser.py takes in a file path to a kubernetes yaml and checks if it is valid. Thhis failed when the file did not exist, so to make it resistant to this I added a series of checks to ensure it was a string for a path and that it was a file that existed.

### constructHelmString() - _Cameron Kapsrzak_

The _constructHelmString()_ method in _graphtaint.py_ takes a tuple as an input and creates variables based on the values of the input. I was able to fuzz the method by inputting values that were not tuple objects. The function would crash when it tried to address the values in the 'tuple' that does not exist. To prevent this crashing, I created a check that would exit the function with a message if the input was not a tuple object.

### checkIfWeirdYAML() - _Cameron Kasprzak_ & _Youssef Mousallam_

The _checkIfWeirdYAML()_ method in _parser.py_ iterates through a list of yaml scripts and checks them against a known list of 'weird paths'. To fuzz the file we provided inputs that were not in a list format, and the method crashed when it tried to iterate through non-list variables. TO prevent this crashing, I created a check that would exit the function with a message if the input was not a list object.

## Lessons Learned

The knowledge gained from the lesson workshops has been immensely beneficial. It includes learning to identify security misconfigurations in Kubernetes configuration files using existing tolls, employing the ‘bandit’ command for generating reports on security vulnerabilities, and implementing Git Hooks to initiate static analysis on widely used repositories. Additionally, the project enhanced my understanding of running Docker images and utilizing Vault for substituting hard-coded passwords with more secure options.

## Group Individuals Efforts

**Cameron Kasprzak** - Created pre-commit hook, fuzz.py, and 1 method fuzzer, worked on github action
**Youssef Mousallam** - Created repository, added 2 python methods to fuzz, created report
**Adrian Rushing** - Created 2 python methods to fuzz with screenshots, worked on github action
