set1 = set([11, 12, 13, 14, 15])
print(set1)

set2 = {1, 2, 3, 4}
set3 = {3, 5, 8}

print(set2.intersection(set3))
print(set2.difference(set3))
print(set2.pop())

listA = [1, 2, 3, 7]
listB = [1,3,8]

fst1 = frozenset(listA)
fst2 = frozenset(listB)
print(fst1)