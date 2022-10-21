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
    if a>=b and b>=c:
         x1=b
    if b>=a and a>=c:
         x1=a
    if a>=c and c>=b:
         x1=c
    if c>=a and a>=b:
         x1=a
    if b>=c and c>=a:
         x1=c
    if c>=b and b>=a:
         x1=b
    return x1
print(main(23,32,31))    