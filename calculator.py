print(
'''<=========================================================================>
Welcome to a Basic Calculator
This calculator is modelled after a basic shop calculator. This calculator
only supports basic mathemaetical operations: addition, subtraction,
division and multiplication.
In addition it performs the operation as soon as there is a sign change
and doesn't use BEDMAS"

NOTE:
The valid operator signs are : +, -, *, /
Use '=' to get the answer
please do not use a text as operand
Agter each operand pres enter

<=========================================================================>
'''
    )
firstval = input("first Value: ").strip()
calc = int(firstval)
while True:
    sign = input("sign (Use '=' to get your answer): ").strip()
    if sign == "=":
        break
    if sign not in "+-*/" or not sign:
        print("Invalid Sign!")
        continue
    other = int(input("Anaother value: ").strip())
    match sign:
        case "+":
            calc += other
        case "-":
            calc -= other
        case "*":
            calc *= other
        case "/":
            calc /= other

print()
print(calc)
