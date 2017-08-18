
This is a basic test script written in Python 3.6 to cover GitHub API v.3 requests for commit functionality. The official documentation for which can be found under https://developer.github.com/v3/git/commits/ page.

# Introduction.
This script is intended to test that all required parameters(fields) can be successfully retrieved from the last commit from GitHub commits API endpoint. The approach is to check one(latest) commit and it's field and get total number of commits by current user. To make this possible, at first, test script receives authorization token from Github server to pass OAuth v.2 authorization. This is done based on application key and secret key from Github application created by ikostiuk user. 
This test requires additional development and refactoring in order to fully cover commit functionality and be easy-readable and maintainable.

# Setup
To run the test on your machine you need to make sure that:
1. Python 3 is properly installed on your PC. (https://www.python.org/downloads/). Check by typing 'python -v' in terminal.
2. Pip installer is installed on the machine. https://pip.pypa.io/en/stable/installing/
3. Requests and Unittest python modules are installed. Rune 'pip install requests', 'pip install requests' commands for this.

# Test run
To launch test and verify Github Commit feature download GitHubTest.py file to particular folder. 
Navigate to folder with GitHubTest.py file in the terminal and run next command there:

python -m unittest GitHubTest.py
