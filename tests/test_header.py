import pytest

from stylepy import h1, h2

def test_h1():
    expected = """
========================================
Test Heading1
========================================"""
    
    # Call the function and capture its output
    actual = h1("Test Heading1", returnValue=True)
    
    # Assert that the function returns the expected value
    assert actual == expected


def test_h2():
    expected = """
-----------------------------------
Test Heading2
-----------------------------------"""
    
    # Call the function and capture its output
    actual = h2("Test Heading2", returnValue=True)
    
    # Assert that the function returns the expected value
    assert actual == expected