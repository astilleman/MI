##
# Is the given list of values sorted?
def is_sorted(values):
    return all(values[i] <= values[i+1] for i in range(0, len(values)-1))

##
# Is list1 a permutation of list 2?
def is_permutation(list1, list2):
    return len(list1) == len(list2) and all(list1.count(x) == list2.count(x) for x in list1)

##
# Is value <= every numer is lst?
def lte_all(value, lst):
    return all(value <= x for x in lst)

##
# Is value >= every number in lst?
def gte_all(value, lst):
    return all(value >= x for x in lst)

##
# Is every number in list1 <= every number in list2
def all_lte_all(list1, list2):
    return all(lte_all(x, list2) for x in list1)
