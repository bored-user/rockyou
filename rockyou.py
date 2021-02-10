import itertools
import re

def rockyou(minimum: int = 4, maximum: int = 16, chars: list = ['*', '.', '?', '@', '#', '$', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], constraints: None=None):
    if constraints:
        chars = list(filter(lambda c: re.search(constraints, c), chars))

    for i in range(minimum, maximum + 1):
        for c in itertools.product(chars, repeat=i):
            yield c