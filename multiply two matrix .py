A=[[3,7,8],
[2,5,4],
[3,5,9]]

B=[[6,7,8],
[3,5,1],
[7,0,5]]

result=[[0,0,0],
[0,0,0],
[0,0,0]]

for i in range(len(A)):
    for j in range (len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k] *B[k][j]
for i in result:
    print(i)