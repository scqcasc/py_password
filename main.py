from password import Password
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', '-l', type=int, default=8)
    args = parser.parse_args()

    p = Password(length=args.length)

    if args.length < 4:
        print("Minimum password length is 4")
        sys.exit(1)

    print(p.get())



