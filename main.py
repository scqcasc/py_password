from password import Password
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', '-l', type=int, default=8)
    args = parser.parse_args()

    p = Password(length=args.length)
    print(p.get())



