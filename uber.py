import argparse

parser = argparse.ArgumentParser(description="Hola")
parser.add_argument("--load_fix_element", help="Crea una ubicación fija")

args = parser.parse_args()

def a(b):
    print(b)

if args.load_fix_element:
    a(args.load_fix_element)
