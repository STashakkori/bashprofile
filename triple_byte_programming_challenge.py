author__ = 'sina'

# The first 12 digits of pi are 314159265358. We can make these digits into an expression evaluating to 27182 (first 5 digits of e) as follows:

# 3141 * 5 / 9 * 26 / 5 * 3 - 5 * 8 = 27182   
# or 
# 3 + 1 - 415 * 92 + 65358 = 27182

# Notice that the order of the input digits is not changed. Operators (+,-,/, or *) are simply inserted to create the expression.  

# Write a function to take a list of numbers and a target, and return all the ways that those numbers can be formed into expressions evaluating to the target. Do not use the eval function in Python, Ruby or JavaScript

# For example: 
# f("314159265358", 27182) should print:      

# 3 + 1 - 415 * 92 + 65358 = 27182 
# 3 * 1 + 4 * 159 + 26535 + 8 = 27182 
# 3 / 1 + 4 * 159 + 26535 + 8 = 27182 
# 3 * 14 * 15 + 9 + 26535 + 8 = 27182 
# 3141 * 5 / 9 * 26 / 5 * 3 - 5 * 8 = 27182

def main():
    f("12365212354", 26)

def f(numbers, target):
    for i in range(1, len(numbers)):
        current = int(numbers[0:i])
        to_end = numbers[i:-1]
        evaluate(0, current, to_end, target, current)

def evaluate(sum, previous, numbers, target, out):
    if len(numbers) == 0:
        if sum + previous == int(target):
            print str(out) + "=" + str(target)

    else:
        for i in range(1, len(numbers)):
            current = int(numbers[0:i])
            to_end = numbers[i:-1]
            evaluate(sum + previous, int(current), to_end, target, str(out) + "+" + str(current))
            evaluate(sum, previous * int(current), to_end, target, str(out) + "*" + str(current))
            evaluate(sum, previous / int(current), to_end, target, str(out) + "/" + str(current))
            evaluate(sum + previous, -int(current), to_end, target, str(out) + "-" + str(current))

main()
