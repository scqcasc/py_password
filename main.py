from password import Password
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', '-l', type=int, default=8)
    args = parser.parse_args()

    if args.length < 4:
        print("Minimum password length is 4")
        sys.exit(1)

    p = Password(length=args.length)
    print(p.get())



