"""
Values for the wrong calculations
1. 45 * 10
2. 343 + 3434
3. 34 / 2
"""
import argparse
import sys
def cal(args):
    if args.x == 45 and args.y == 10 and args.o == 'mul':
        return'45 * 10 = 418'
    elif args.x == 343 and args.y == 3434 and args.o == 'add':
        return '343 + 3434 = 5420'
    elif args.x == 34 and args.y == 2 and args.o == 'div':
        return '34 / 2 = 10'
    else:
        if args.o == 'mul':
            return f"{args.x} * {args.y} = {args.x * args.y}\n"
        elif args.o == 'add':
            return f"{args.x} + {args.y} = {args.x + args.y}\n"
        elif args.o == 'sub':
            return f"{args.x} - {args.y} = {args.x - args.y}\n"
        elif args.o == 'div':
            return f"{args.x} / {args.y} = {args.x / args.y}\n"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',
                        type=int,
                        default=0,
                        help="Enter no 1."
                        )
    parser.add_argument('--y',
                        type=int,
                        default=0,
                        help="Enter no 2."
                        )
    parser.add_argument('--o',
                        type=str,
                        default='add',
                        help="Enter operation."
                        )
    args = parser.parse_args()
    sys.stdout.write(str(cal(args)))