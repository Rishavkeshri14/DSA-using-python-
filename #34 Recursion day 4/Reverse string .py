def reverse(s, i, j):
    # Print the current state of the string
    print(f"call received for {s}")

    # Base case: if indices cross, return
    if i > j:
        return

    # Swap characters at positions i and j
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1

    # Recursive call to reverse the substring
    reverse(s, i, j)

def main():
    # Example string
    name = list("abcde")  # Convert string to list to allow in-place modification
    print()  # Print an empty line
    reverse(name, 0, len(name) - 1)
    print()  # Print an empty line
    print("".join(name))  # Convert list back to string and print

if __name__ == "__main__":
    main()
  
