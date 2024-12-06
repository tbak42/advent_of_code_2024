import itertools 

USE_SAMPLE = False
if USE_SAMPLE:
    data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
else:
    with open('d5a.txt') as f:
        data = f.read()
        
before_rules = {}
after_rules = {}
updates = []
for line in data.splitlines():
    if line.find('|') != -1:
        pages = list(map(int,line.split('|')))
        if pages[0] not in before_rules:
            before_rules[pages[0]] = []
        before_rules[pages[0]].append(pages[1])

        if pages[1] not in after_rules:
            after_rules[pages[1]] = []
        after_rules[pages[1]].append(pages[0])

    if line.find(',') != -1:
        updates.append(list(map(int,line.split(','))))

def test_update(update):
    # did_pass = True
    for before_index in range(len(update)):
        for after_index in range(len(update)):
            if before_index == after_index:
                continue

            before = update[before_index]
            after = update[after_index]

            if before_index < after_index:
                if before not in before_rules or after not in before_rules[before]:
                    # print('fail before {} {}'.format(before, after))
                    # did_pass = False
                    new_update = update[:]
                    new_update[before_index] = update[after_index]
                    new_update[after_index] = update[before_index]
                    return (False, new_update)

            if after_index < before_index:
                if after in after_rules and before in after_rules[after]:
                    # print('fail after {} {}'.format(before, after))
                    # did_pass = False
                    new_update = update[:]
                    new_update[before_index] = update[after_index]
                    new_update[after_index] = update[before_index]
                    return (False, new_update)

    # return did_pass
    return (True, update)


score = 0
foobar = 0
for update in updates:

    print(update)
    did_pass = test_update(update)[0]
    print(did_pass)
    
    # Part 1
    # if did_pass:
        # score += update[ int((len(update)-1) /2) ]

    # Part 2
    if not did_pass:

        while not did_pass:
            (did_pass, new_update) = test_update(update)
            if did_pass:
                score += update[ int((len(new_update)-1) /2) ]
                break
            update = new_update

        """
        update_perms = itertools.permutations(update)
        for update in update_perms:
            did_pass = test_update(update)
            if did_pass:
                score += update[ int((len(update)-1) /2) ]
                break
        """
print(score)
exit()


print(before_rules)
print(after_rules)
print(updates)

print(score)


