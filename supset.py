
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}
is_superset_itself = set1.issuperset(set1)
is_superset_other = set1.issuperset(set2)
print("Is set1 a superset of itself?", is_superset_itself)
print("Is set1 a superset of set2?", is_superset_other)
