'''
The structure of our test files should typically mirror the structure of our main source directory.
Since this is a template, our tests directory will follow the same spartan structure.
'''

import pytest

import src.main as main

def test_main():
    '''
    This is an example for what a test might look like using pytest which is my personal preference. 
    '''

    assert main is not None

def test_main_pytest():
    '''
    Here is an example of how we would perform a similar test with pytest specific error handling.
    '''
    with pytest.raises(FileNotFoundError):
        with open("src/missing.py", 'r', encoding = "utf-8") as file:
            file.read()
