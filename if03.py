import re


def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and b>c:
         x1=b
    if b>a and a>c:
         x1=a
    if a>c and c>b:
         x1=c
    return x1
print(main(4,9,1))