def solve(ans, str, output, i):
    # Base case: if we've considered all characters in the input string
    if i >= len(str):
        if len(output) > 0:
            ans.append(output)
        return

    # Exclude the current character and move to the next
    solve(ans, str, output, i + 1)
    
    # Include the current character and move to the next
    output += str[i]
    solve(ans, str, output, i + 1)
    
    # Backtrack to remove the current character for the next calls
    output = output[:-1]

def subsequences(str):
    ans = []
    output = ""
    solve(ans, str, output, 0)
    return ans

# Example usage:
input_str = "abc"
print(subsequences(input_str))

#output
['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
