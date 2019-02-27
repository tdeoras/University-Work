def lcs(Str1, Str2):
    m = len(Str1)
    n = len(Str2)
    M = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                M[i][j] = 0
            elif Str1[i-1] == Str2[j-1]:
                M[i][j] = M[i-1][j-1] + 1
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])

    length = M[m][n]
    

    #Refered from : https://www.geeksforgeeks.org/printing-longest-common-subsequence/
    result = [""] * (length+1)
    result[length] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if Str1[i-1] == Str2[j-1]:
            result[length-1] = Str1[i-1]
            i-=1
            j-=1
            length-=1

        elif M[i-1][j] > M[i][j-1]:
            i-=1
        else:
            j-=1

    print 'The length of Common Substring is ' + str(len(result) - 1)
    print 'The Substring is: ' + str(result[:-1])


#Test Case 1
A = "ABCBDAB"
B = "BDCABA"
lcs(A, B)

#Test Case 2
A = "10010101"
B = "010110110"
lcs(A,B)
