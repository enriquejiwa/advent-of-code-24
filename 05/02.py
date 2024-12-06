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

def fix_update(update: list[int], rules: dict[int, list[int]]):
    update_set = set(update)
    visited = set()
    incorrect = False
    i = 0
    while i < len(update):
        traded = False
        value = update[i]
        required = rules[value]
        for r in required:
            if r in update_set and r not in visited:
                incorrect = True
                r_index = update.index(r)
                update[r_index], update[i] = update[i], update[r_index]
                traded = True
                break
        if not traded:
            visited.add(value)
            i += 1
    return update[len(update) // 2] if incorrect else 0

def main():
    rules, updates = parse_input()
    rules = compute_rules(rules)
    res = 0
    for update in updates:
        res += fix_update(update, rules)
    print(res)

# python 02.py < input > output
if __name__ == '__main__':
    main()