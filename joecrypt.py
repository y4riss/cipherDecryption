#! python3

# this program decrypt a cipher code using cipher rotations

import argparse
import sys
from art import get_ascii_art

if len(sys.argv) != 7:
    print(
        f" # USAGE : python {sys.argv[0]} -str yourString -n RotationNumber -d backward/forward"
    )
    exit()

get_ascii_art()

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-str", "--string", required=True, help="string to decrypt")
ap.add_argument("-n", "--rotation", required=True, help="rotation number")
ap.add_argument("-d", "--direction", required=True, help="direction : forward/backward")
args = vars(ap.parse_args())

str = args["string"]
n = args["rotation"]
opt = args["direction"]


if not n.isnumeric():
    print("## The rotation number must be an integer")
    exit()

n = int(n)

if opt != "forward" and opt != "backward":
    print(
        " please select your rotation direction ( forward for going forward / backward for going backwards ) "
    )
    exit()
elif opt == "backward":
    n += 24


str_decrypt = ""
for i in str:
    if i.isnumeric():
        str_decrypt += i
        continue

    upper = False
    character = i
    if i == i.upper():
        character = i.lower()
        upper = True

    ascii_value = ord(character) + abs(n)

    if ascii_value > 122:
        ascii_value -= 26

    if upper:
        c = chr(ascii_value).upper()
    else:
        c = chr(ascii_value)
    str_decrypt += c

print("############################################################# \n\n")
print("# initial string : " + str)
print(f"# rotation number used : {args['rotation']}")
print("# result : " + str_decrypt + "\n\n")
print("############################################################# \n\n")
