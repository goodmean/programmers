n, m = map(int, input().split())

answer = []   
breaking = True

for i in range(n, 0, -1):
	if n % i == 0 and m % i == 0:
		answer.append(i)
		break
          
for j in range(1, m+1):
	for k in range(1, n+1):
		if n * j == m * k:
			answer.append(n*j)
			breaking = False
			break
	if breaking == False:
		break
            
print(answer)
