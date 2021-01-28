import itertools

# FORMAT  (root_element, [(set, support), (set, support), (set, support)])
data = [
    ("p", [({"f", "c", "a", "m"}, 2), ({"c", "b"}, 1)]),
    ("m", [({"f", "c", "a"}, 2), ({"f", "c", "a", "b"}, 1)]),
]


def get_common_elements(set_list):
    return set.intersection(*set_list)


def get_support_count(support_list):
    return sum(support_list)


def findsubsets(lst):
    return list(itertools.permutations(lst))



def findAllsubsets(set_):
    size = len(set_)
    all_subsets = []
    while size > 0:
        all_subsets += findsubsets(set_, size)
        size -= 1
    return all_subsets


def parse_data(pattern_bases):
    set_list, support_list = [], []

    for pattern_base in pattern_bases:
        set_list.append(pattern_base[0])
        support_list.append(pattern_base[1])
    return set_list, support_list


def main():

    for example in data:
        root, pattern_bases = example
        set_list, support_list = parse_data(pattern_bases)

        common_elements = get_common_elements(set_list)
        support_count = get_support_count(support_list)

        frequent_pattern_set = common_elements
        allSubsets = findAllsubsets(frequent_pattern_set)
        frequent_pattern_set.add(root)

        print(f"ROOT: {root}")
        print(f"Frequent Set : {frequent_pattern_set}")
        print(f"Support  : {support_count}")

        print("All frequent patters")
        for allSubset in allSubsets:
            allSubset.add(root)
            print(f"{allSubset}")


if __name__ == '__main__':
    main()
