"""
perform a single operation given a string
ex. "3 + 2"
outcome: 5.0
"""


import sys

#: get rid of all spaces
var = sys.argv[1]
var = var.replace(" ", "")

#: declare strings to save two different numbers to
first = ""
second = ""

#: saves number in "first" string
#: cuts off after reaching non-digit
#: saves next char as operator
for i, d in enumerate(var):
	if d.isdigit():
		first += d
	else:
		operator = d
		position = i
		break

#: saves number in "second" string
for i, n in enumerate(var[position:]):
	if n.isdigit():
		second += n

#: converts strings to floats
fn = float(first)
sn = float(second)


#: prints outcome depending on operation
 
if operator == "+":
	print(fn + sn)

elif operator == "-":
	print(fn - sn)

elif operator == "*":
	print(fn * sn)

elif operator == "/":
	print(fn / sn)

else:
	print("Invalid Entry")
