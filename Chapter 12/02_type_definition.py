"""TYPES DEFINITIONS IN PYTHON

Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types. r"""


# Variable type hint
age : int = 21


# function type hints
def greeting(name: str, lastName: str) -> str :
    return f"Hello {name} {lastName}"


print(greeting("piyush", "Mishra"))