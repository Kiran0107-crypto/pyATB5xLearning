def LCS(string1, string2):
    len_string1 = len(string1)
    print(len_string1)
    len_string2 = len(string2)
    print(len_string2)
    # DP table to store lengths of LCS
    dp = [[0] * (len_string1 + 1) for _ in range(len_string2 + 1)]
    #print(dp)
    # Fill DP Table
    for i in range(1, len_string1+1):
        for j in range(1, len_string2+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i - 1][j - 1]+1
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

    # Reconstructing the LCS from the dp table
    LCS = []
    i, j = len_string1, len_string2
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            LCS.append(string1[i - 1])
            i = i - 1
            j = j - 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i = i - 1
        else:
            j = j - 1
    # Reverse to get the correct LCS string
    LCS.reverse()
    return dp[len_string1][len_string2], ''.join(LCS)


String1 = input("Enter 1st String:\n")
String2 = input("Enter 2nd String:\n")

length, lcs_string = LCS(String1, String2)
print(f"Length of LCS:{length}")
print(f"Longest Common Subsequence:{lcs_string}")
