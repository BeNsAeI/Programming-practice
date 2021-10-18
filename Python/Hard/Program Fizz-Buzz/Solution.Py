"""
Write the Fizz Buzz Game:
    Inputs:
        - size of the game, fizz index, buzz index
    Outputs:
        - List of Answers
"""

# Pseudocode:
# - Count From 1 to size + 1
# - For each Item in index dictionary
# - If current number is divisible by the dictionary value, replace it with index
# - Add the new string to the output list

def Fizz_Buzz(size, index_dictionary):
    out = [];
    for i in range (1, size + 1):
        value = "";
        for index in index_dictionary:
            if(i % index_dictionary[index] == 0):
                value += index;
        if value == "":
            value = str(i);
        out.append(value);
    return out;

# Big O if n is size and m is number of fizz and buzz variants:
# - O(n * m)

#Test:
result = Fizz_Buzz(30, {"fizz":3,"buzz":5})
print(",\n".join(result))
