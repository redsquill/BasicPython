"""x = [0, 1, 2, 3, 4, 5]"""
x = list(range(10))
print(x)
y = list(range(30, 51))
print(y)
z = list(range(1, 101, 1))
print(z)
p = list(range(20, 0, -1))
print(p)
q = [10, 6, 11, 13, 26, 70, 4, 10]
print(q[2])

sum = 0
i = 0
while i < len(q):

    sum += q[i]
    i += 1

print(sum)
avg = sum / len(q)
print(f'Total number of item in the list is: {len(q)}')
print(f'thev average is: {avg}')
q.append(100)
q.append(200)
print(q)
q.extend([90, 25, 80, 20, 70])
print(q)
q.insert(-1, 500)
print(q)
del q[-1]
print(q)
q.pop()
print(q)
q.remove(200)
print(q)
q.sort()
print(q)
q.sort(reverse=True)
print(q)
print(q[0:3])
print(q[:3])
print(q[3:])
print(q[3:7])
print(q[-1])
print(q[-2])
print(q[:])
