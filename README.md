# GitHub API /commit test
This is a basic test script written in Python 3.6 to cover commit request via GitHub API v.3. The official documentation for which is located on https://developer.github.com/v3/git/commits/ page.

## Introduction
This script is intended to test all required parameters(fields) for particular commit and verify that they can be successfully retrieved from the last GitHub commits made by user. The approach is to check one(latest) commit and its fields and get total number of commits provided by current user. To make this possible, at first, test script receives authorization token from Github server to pass OAuth v.2 authorization. This is done based on application key and secret key from Github application created by ikostiuk user. 
This test requires additional development and refactoring in order to fully cover /commit functionality and be easy-readable and maintainable. Also, test does not prepare new commit instance for itself, and relies on fact that there is at least one commit already pushed to repository. Generally, this is test for /commit endpoint, but not whole commit functionality.

## Setup
To run the test on your machine you need to make sure that:
- Python 3 is properly installed. Check by typing 'python -v' in terminal, and if not, visit https://www.python.org/downloads.
- `Pip` installer is installed on the machine. https://pip.pypa.io/en/stable/installing/
- `Requests` and `Unittest` python modules are installed. Run `pip install requests`, `pip install requests` commands for this.

## Test run
To launch test and verify Github Commit feature download `GitHubTest.py` file to particular folder. 
Navigate to folder with `GitHubTest.py` file in the terminal and run next command there:

*python -m unittest GitHubTest.py*

Make sure that python installation folder is added to environment variables so that command is accessible from you file location.

## Notes
As part of CI implementation wanted to add shell file to run command by schedule. But to support both MacOS and Windows decided to leave command as is, so that it will work on both platforms, while scheduling is yet another part provided on test run environment.

Regarding BDD approach, found Python libraries **Morelia** and **Behave** that can wrap existing unit tests to follow BDD, but that also required additional time to implement and test the flow.
