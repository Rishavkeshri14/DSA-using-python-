class Solution:
    def knows(self, M, a, b):
        """
        Helper function to determine if person 'a' knows person 'b'.
        """
        return M[a][b] == 1

    def celebrity(self, M):
        """
        Function to find if there is a celebrity in the party or not.
        :param M: 2D list where M[i][j] = 1 means person i knows person j
        :return: index of the celebrity or -1 if there is no celebrity
        """
        n = len(M)
        stack = []

        # Step 1: Push all elements into the stack
        for i in range(n):
            stack.append(i)

        # Step 2: Get two elements and compare them
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()

            # If 'a' knows 'b', 'a' cannot be a celebrity
            if self.knows(M, a, b):
                stack.append(b)
            else:
                stack.append(a)

        # Step 3: Single element in stack is a potential celebrity
        if not stack:
            return -1
        
        ans = stack.pop()

        # Verify that 'ans' is a celebrity
        zero_count = sum(M[ans][i] == 0 for i in range(n))

        # If not all zeros in the row of 'ans', 'ans' cannot be a celebrity
        if zero_count != n:
            return -1

        one_count = sum(M[i][ans] == 1 for i in range(n))

        # If not exactly n-1 ones in the column of 'ans', 'ans' cannot be a celebrity
        if one_count != n - 1:
            return -1

        return ans


# Example usage
if __name__ == "__main__":
    # Test case: Number of people at the party
    n = 4
    # Adjacency matrix where M[i][j] = 1 means i knows j
    M = [
        [0, 0, 1, 0],  # Person 0 knows person 2
        [0, 0, 1, 0],  # Person 1 knows person 2
        [0, 0, 0, 0],  # Person 2 knows no one (potential celebrity)
        [0, 0, 1, 0]   # Person 3 knows person 2
    ]
    
    solution = Solution()
    celebrity_index = solution.celebrity(M)
    print("The celebrity index is:", celebrity_index)  # Output: 2
