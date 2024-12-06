import sys
from collections import defaultdict

def parse_input():
    rules = []
    updates = []
    rules_done = False
    for line in sys.stdin:
        if line == '\n':
            rules_done = True
            continue
        if not rules_done:
            rules.append([int(num) for num in line.strip('\r\n').split('|')])
        else:
            updates.append([int(num) for num in line.strip('\r\n').split(',')])
    return rules, updates

def compute_rules(rules):
    table = defaultdict(list)
    for before, after in rules:
        table[after].append(before)
    return table

def check_update(update, rules):
    update_set = set(update)
    visited = set()
    for value in update:
        required = rules[value]
        for r in required:
            if r in update_set and r not in visited:
                return False
        visited.add(value)
    return True

def main():
    rules, updates = parse_input()
    rules = compute_rules(rules)
    res = 0
    for update in updates:
        if check_update(update, rules):
            res += update[len(update) // 2]
    print(res)

# python 01.py < input > output
if __name__ == '__main__':
    main()