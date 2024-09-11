# Function to simulate reaching home using recursion
def reach_home(src, dest):
    # Print the current source and destination
    print(f"source: {src}, destination: {dest}")

    # Base case: if source and destination are the same
    if src == dest:
        print("Pahuch gya!")  # Means "Reached home" in Hindi
        return
    
    # Processing step: move one step forward
    src += 1

    # Recursive call: move closer to the destination
    reach_home(src, dest)

# Example usage
if __name__ == "__main__":
    destination = 10
    source = 1

    # Call the reach_home function to start the process
    reach_home(source, destination)
