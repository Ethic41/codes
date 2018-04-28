import argparse
from math import factorial
"""
parser = argparse.ArgumentParser()
parser.add_argument("sqr", help="calculate the square of your specified num", type=int)
parser.add_argument("-v", "--verbose", help="increase verbosity level", action="store_true")
parser.add_argument("-f", "--fct", help="calculate factorial of a number", type=int)
args = parser.parse_args()
ans = args.sqr**2
if args.verbose:
    print("the square of {} is {}".format(args.sqr, ans))
else:
    print(ans)
if args.fct:
    print(factorial(args.fct))
"""

parser = argparse.ArgumentParser(description="Enter a number as the first argument...u will be amazed.")
parser.add_argument("-f", "--file", help="specify a file name", type=file, required=True)
parser.add_argument("-v", "--verbose", help="increase verbosity level", choices=[0,1,2], type=int)
parser.add_argument("sqr", help="calculate the square of the given number", type=int)
parser.add_argument("--fct", help="find the factorial of the given number", type=int)
parser.add_argument("-l", "--laugh", help="try this and see...")
args = parser.parse_args()
ans = args.sqr**2
if args.verbose >= 1:
    print("{} squared is {}".format(args.sqr, ans))
elif args.verbose >= 2:
    print("the square of {} was found to be {}".format(args.sqr, ans))
else:
    print(ans)
if args.fct:
    print(factorial(args.fct))
if args.laugh:
    print("heheheyyheye........wat else did you expect")
