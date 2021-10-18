"""
Write the Fizz Buzz Game:
    Inputs:
        - size of the game
    Outputs:
        - List of Answers
"""

# Pseudocode:
# - Count From 1 to size + 1
# - For each Item in index dictionary
# - If current number is divisible by provided fizz add fizz
# - If current number is divisible by provided buzz add buzz
# - Add the new string to the output list

def Fizz_Buzz(size, fizz, buzz):
    out = [];
    for i in range (1, size + 1):
        value = "";
        if(i % fizz == 0):
                value += "fizz";
        if(i % buzz == 0):
                value += "buzz";
        if value == "":
            value = str(i);
        out.append(value);
    return out;

# Big O if n is size:
# - O(n)

#Test:
result = Fizz_Buzz(30,3,5)
print(",\n".join(result))
