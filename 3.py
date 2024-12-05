import re

def process_string(s):
    result = 0
    x = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", s)
    is_enabled = True
    for match in x:
        if match == 'do()':
            is_enabled = True
        elif match == "don't()":
            is_enabled = False
        else:
            if is_enabled:
                nums = list(map(int, match[4:-1].split(',')))
                result += nums[0]*nums[1]
    print(result)

with open('d3a.txt') as f:
    process_string(f.read())

#process_string('mul(1,2) mul(22,34) mux(3, 4)')
process_string("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")

