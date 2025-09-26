# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    row = 0
    result = ""
    while row < n:
        if row == 0 or row == n - 1:   
            result += "*" * n
        else:
            result += "*" + " " * (n - 2) + "*"
        result += "\n"
        row += 1
    return result.rstrip("\n")

# 1
# 12
# 123
# 1234
def number_pattern(n):
    row = 1
    result = ""
    while row <= n:
        col = 1
        while col <= row:
            result += str(col)
            col += 1
        result += "\n"
        row += 1
    return result.rstrip("\n")

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    num = 1
    expression = ""

    while num <= n:
        total += num
        expression += str(num)
        if num < n:   # add "+" between numbers
            expression += " + "
        num += 1
    print("Sum = "f"{expression} = {total}")
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    row = 1
    result = ""
    while row <= n:
        spaces = " " * (n - row)
        stars = "*" * (2 * row - 1)
        result += spaces + stars + "\n"
        row += 1
    return result.rstrip("\n")


# Test functions

if __name__ == "__main__":
    
    #Test 1
    n = int(input("Enter a number: "))
    print(hollow_square(n))
    
    #Test2
    n = int(input("Enter a number: "))
    print(number_pattern(n))
    

    #Test 3
    n = int(input("Enter a number: "))
    sum_of_natural_numbers(n)

    #Test 4
    n = int(input("Enter a number: "))
    print(centered_star_pyramid(n))