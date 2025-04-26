# COMP 5710 Term Project
Cameron Kasprzak
Youssef Mousallam
Adrian Rushing

## Activities
All source files, commit history, changelogs, output files as well as additional information contained in README’s can be found on the team GitHub repository here: https://github.com/ImYoussef/FailSafe-SQA2025-AUBURN/tree/main

### Execution of Git Hooks
The following artifacts are designed to provide evidence of successful integration and validation of requirement “4a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. (10%)”. As the pre-commit hook is a client-side hook, the contents of it are not stored on the Team’s Repository per standard Git practice. Instead the pre-commit hook file is simply uploaded in a separate folder labeled “hooks”  

### Execution of Fuzzing

## Screenshots and Logs
This section of the report contains screenshots and snippets of log files that demonstrates the team members successfully integrated and validated all the requirements found here: https://github.com/ImYoussef/FailSafe-SQA2025-AUBURN/tree/main/Screenshots 

## Fuzzed Methods
### constructHelmString() - *Cameron Kapsrzak*
The *constructHelmString()* method in *graphtaint.py* takes a tuple as an input and creates variables based on the values of the input. I was able to fuzz the method by inputting values that were not tuple objects. The function would crash when it tried to address the values in the 'tuple' that does not exist. To prevent this crashing, I created a check that would exit the function with a message if the input was not a tuple object.

## Lessons Learned
The knowledge gained from the lesson workshops has been immensely beneficial. It includes learning to identify security misconfigurations in Kubernetes configuration files using existing tolls, employing the ‘bandit’ command for generating reports on security vulnerabilities, and implementing Git Hooks to initiate static analysis on widely used repositories. Additionally, the project enhanced my understanding of running Docker images and utilizing Vault for substituting hard-coded passwords with more secure options.

## Group Individuals Efforts
**Cameron Kasprzak** - Created pre-commit hook, fuzz.py, and 1 method fuzzer, worked on github action
**Youssef Mousallam** - Created repository, added 2 python methods to fuzz, created report
**Adrian Rushing** - Created 2 python methods to fuzz with screenshots, worked on github action
    
