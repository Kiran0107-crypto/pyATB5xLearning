def find_all_longest_LCS(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)

    # DP table with 0-based indexing, size len_string1 x len_string2
    """
    Creates a 2D list (or matrix) called dp that represents the Dynamic Programming (DP) table for storing 
    the lengths of the Longest Common Subsequence (LCS) at different points of comparison 
    between two strings. Here's a detailed breakdown of how it works:
    
    What Does It Do?
Structure:

[[0] * (len_string2) creates a row of len_string2 zeros.
for _ in range(len_string1) repeats this row len_string1 times, resulting in a matrix of dimensions len_string1 x len_string2.
Purpose:

Each cell in the dp table, dp[i][j], stores the length of the LCS of the substrings:
string1[0:i+1] (i.e., the first i+1 characters of string1)
string2[0:j+1] (i.e., the first j+1 characters of string2).
0-based indexing:

The matrix aligns directly with the indices of the strings (string1 and string2), which are also 0-based.
For example:
dp[0][0] corresponds to comparing the first character of both strings.
dp[1][2] corresponds to comparing the first two characters of string1 with the first three characters of string2.
Initialization:

All cells are initialized to 0 because initially, the LCS length for any pair of substrings is 0.
    """

    dp = [[0] * (len_string2) for _ in range(len_string1)]

    # Fill DP Table
    for i in range(len_string1):
        for j in range(len_string2):
            if string1[i] == string2[j]:
                dp[i][j] = (dp[i - 1][j - 1] + 1) if i > 0 and j > 0 else 1
            else:
                dp[i][j] = max(dp[i - 1][j] if i > 0 else 0, dp[i][j - 1] if j > 0 else 0)

    # Backtrack to find all LCS with the maximum length
    def backtrack(i, j):
        if i < 0 or j < 0:
            return {""}

        if string1[i] == string2[j]:
            subsequences = backtrack(i - 1, j - 1)
            return {sub + string1[i] for sub in subsequences}
        else:
            subsequences = set()
            if i > 0 and dp[i - 1][j] == dp[i][j]:
                subsequences.update(backtrack(i - 1, j))
            if j > 0 and dp[i][j - 1] == dp[i][j]:
                subsequences.update(backtrack(i, j - 1))
            return subsequences

    # Find the LCS length (bottom-right cell of the DP table)
    max_length = dp[len_string1 - 1][len_string2 - 1] if len_string1 > 0 and len_string2 > 0 else 0
    # Start backtracking from the bottom-right of the DP table
    all_lcs = backtrack(len_string1 - 1, len_string2 - 1)
    return max_length, all_lcs


# Input strings
string1 = input("Enter 1st String:\n")
string2 = input("Enter 2nd String:\n")

# Compute all LCS
length, all_lcs = find_all_longest_LCS(string1, string2)

# Print results
print(f"Length of LCS: {length}")
print("All Longest Common Subsequences:")
for lcs in sorted(all_lcs):  # Sort for better readability
    print(lcs)

"""
1.DP Initialization: The DP table is now len_string1 x len_string2, aligned directly with string indices.
Boundary Conditions:
2.If i == 0 or j == 0, comparisons involving dp[i-1][j] or dp[i][j-1] default to 0.
Similarly, if i == 0 or j == 0 during backtracking, it stops.
3.Character Comparison:
Directly compares string1[i] and string2[j] without any offset adjustments.

"""