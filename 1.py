USE_SAMPLE = False
if USE_SAMPLE:
    data = """3   4
4   3
2   5
1   3
3   9
3   3"""
else:
    with open('d1a.txt') as f:
        data = f.read()

left = []
right = []
for line in data.splitlines():
    x = line.split('   ')
    print('foo:' + str(x) )
    left.append(int(x[0]))
    right.append(int(x[1]))

# Part 1 
left.sort()
right.sort()

dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])

print(dist)

# Part 2

right_occurences = {}
for num in right:
    if num not in right_occurences:
        right_occurences[num] = 0
    right_occurences[num] += 1

score = 0
for num in left:
    if num in right_occurences:
        score += num * right_occurences[num]

print(score)




