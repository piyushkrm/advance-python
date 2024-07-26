'''
Python's typing module more advance type hints, such as list, tuple, dict and union.
You can import list, tuple and dict types from thr typing module like this
from tyhping import List, Tuple, Dict, Union
'''

from typing import List, Tuple, Dict, Union

# List of integers
Numbers: List[int] = [1, 2, 3, 7, 8, 9]
print(Numbers)

# Tuple of a string and integers
person: Tuple[str, int] = ("piyush", 18)
print(person)


# Dictionary with string keys and integer values
score: dict[str, int] = {"Piyush" : 18, "Abhinav" : 18}
print(score)


# Union type for variables that can hold multiple types
indentifier: Union[int, str] = "IPS18"
indentifier = 123456    #Also valid
print(indentifier)