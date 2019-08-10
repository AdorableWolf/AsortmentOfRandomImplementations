"""The following code returns True if a multiset S of positive integers could be divided into 
two subsets such that each of the two subsets have the same sum. 
Dynamic programming approach was ultilizd to solev the problem---thus giving a running time complexity of O(sum*n), 
where sum is the total of all elements in S and n the length of S."""

def findPatition(S):
    n = len(S)
    sum = 0
    for i in S:
        sum += i
    
    if sum%2 != 0:
        return False

    table = [[True for i in range(n + 1)] for i in range((sum // 2) + 1)]
    
    for i in range(n + 1):
        table[0][i] = True

    for i in range(1, (sum//2 + 1)):
        table[i][0] = False
    

    for i in range(1, (sum//2 + 1)):
        for j in range(1, n + 1):
            table[i][j] = table[i][j - 1]

            if i >= S[j - 1]:
                table[i][j] = table[i][j] or table[i - S[j- 1]][j - 1]
        
    return(table[(sum//2)][n])

#Driver code.
S = [15, 5, 20, 10, 35]
print(findPatition(S))