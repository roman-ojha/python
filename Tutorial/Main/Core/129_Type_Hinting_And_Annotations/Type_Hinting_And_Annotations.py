"""
    -> Here we will going to use typing module to add type hint & annotations in python
    *) Typing: https://docs.python.org/3/library/typing.html
        -> here by adding typing will not going to change the functionality of you make code it will not help to hint and annotate on you python code
        -> you can say just like typescript
        -> It kind of is for documentation purposes
"""

# here 'x' is int
from typing import List, Dict, Set, Optional, Any, Sequence, Tuple, Callable, TypeVar
x = 1
# here 'x' is string
x = "roman"
# we can do this because it is dynamically type

# but we can add type annotation and hint to this variable by:
y: str = 1  # here we can see '1' is and int but we are annotating it as str but we would not get an error because this is just of hinting and documenting
name: str = "roman"

"""
    *) Static code Analysis
        -> we will use package called 'mypy': https://pypi.org/project/mypy/
        -> This tool will look at you python code and Examine a type annotation & see if you have mismatch you types
        -> pip install mypy
        -> to check error run command:
            -> mypy .\<file_name>.py
        *) python default types:
            -> int
            -> float
            -> bool
            -> str
            -> set
            -> dict
            -> list
"""

# Function Annotation ========


def add_numbers(a: int, b: int, c: int) -> int:  # return int
    return a + b + c


a_num = add_numbers(1, 2, 3)


# Void return type ========
def print_hello() -> None:
    print("hello world")


# from typing import List
# List type ========
l: list[int] = []
ll: list[list[int]] = []
lll: List[List[int]] = [[1, 2], [2, 3]]  # imported List type
print(l)

# Dictionary type ========
d: dict[str, str] = {"name": "roman"}
dd: Dict[str, str] = {"name": "roman"}

# Set type ========
s: set[str] = {'a', 'b'}
ss: Set[str] = {'a', 'b'}

# Custom types ========
# here 'Vector' is the custom type that we create which is the equivalent to 'List[float]'
Vector = List[float]
Vectors = List[Vector]


def foo(vs: Vectors) -> Vector:
    print(vs)
    return vs[1]


# with Optional parameter types ========
# here we just have to  specify that 'output' parameter is optional
def foo2(output: Optional[bool] = False):
    pass


# Any type ========
def foo3(output: Any):  # so 'Any' specify that this 'output' parameter actually accept anything
    pass


# Sequence ========
# So if you want to specify any thing that is sequence like 'list', 'tuple' etc.. & 'str' is also a sequence
# 'set' is not a sequence because we can't indexed
def foo4(seq: Sequence[int], seq2: Optional[Sequence[str]] = None):
    # So this 'seq' accept sequence of 'int' type
    pass


foo4((1, 2, 3, 4))
foo4([1, 2, 3, 4, 5], seq2="roman")

# Tuple type ========
t: tuple = (1, 2, 3, 4, "hello")
# Default inside of a tuple
# and we need to specify every type inside the tuple
tt: Tuple[int, int, str] = (1, 2, "roman")


# Callable type
# callable type if you want to accept function as a parameter
# Callable[[<parameters_type>],<return_type>]
def add(x: int, y: int, z: Optional[str] = None) -> int:
    if z != None:
        print(z)
        return x+y
    else:
        return x+y


def foo5(func: Callable[[int, int, Optional[str]], int]):
    print(func(1, 2, "roman"))


foo5(add)


def foo6() -> Callable[[int, int], int]:
    def add(x: int, y: int) -> int:
        return x+y
    return add


foo6()(1, 2)


def foo7() -> Callable[[int, int], int]:
    return lambda x, y: x+y


foo7()(1, 2)


# TypeVar ========
T = TypeVar('T')  # here we are defining generic type, where we don't know what it's type going to be but we will going to call it 'T', so that I can consistently reference it throughout to the program


# here we are taking 'List[T]' type it means that we don't know that type that we will get
# like it 'T' could be 'int', 'float', 'str' doesn't matter but it has to be consistent and all the list data should be of that specific type
def get_item(lst: List[T], index: int) -> T:
    return lst[index]


get_item([1, 2, 3, 4, 5], 0)
