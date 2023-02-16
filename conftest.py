#conftest.py

#Note:
#   this is .fixture 
#   conftest.py makes the .fixture available to many files

# package
import pytest

@pytest.fixture
def input_true():
    val = True

    return val