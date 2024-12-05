USE_SAMPLE = False
if USE_SAMPLE:
    data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
else:
    with open('d2a.txt') as f:
        data = f.read()

# Part 1
num_safe = 0
for line in data.splitlines():
    num_line = list(map(int, line.split(' ')))
    is_increasing = False
    if num_line[1] > num_line[0]:
        is_increasing = True

    is_safe = True
    for i in range(len(num_line)-1):
        first = num_line[i]
        second = num_line[i+1]
        if is_increasing:
            if second != first + 1 and second != first + 2 and second != first + 3:
                is_safe = False
                break
        else:
            if second != first - 1 and second != first - 2 and second != first - 3:
                is_safe = False
                break

    if is_safe:
        num_safe += 1


num_safe = 0
for line in data.splitlines():
    num_line = list(map(int, line.split(' ')))
    
    found_safe = False
    for removed_index in range(len(num_line)):
        funky_num_line = num_line[:removed_index] + num_line[removed_index+1:]
        print(funky_num_line)

        is_increasing = False
        if funky_num_line[1] > funky_num_line[0]:
            is_increasing = True
        
        is_safe = True
        for i in range(len(funky_num_line)-1):
            first = funky_num_line[i]
            second = funky_num_line[i+1]
            if is_increasing:
                if second != first + 1 and second != first + 2 and second != first + 3:
                    is_safe = False
                    break
            else:
                if second != first - 1 and second != first - 2 and second != first - 3:
                    is_safe = False
                    break

        if is_safe:
            found_safe = True
            break

    if found_safe:
        num_safe += 1

print(num_safe)