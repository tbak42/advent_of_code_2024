USE_SAMPLE = True
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
        
rules = []
updates = []
for line in data.splitlines():
    if line.find('|') != -1:
        rules.append(list(map(int,line.split('|'))))
    if line.find(',') != -1:
        updates.append(list(map(int,line.split(','))))

print(rules)
print(updates)


