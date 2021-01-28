import itertools


# dataset = [
#     ("T1", {"I1", "I2", "I5"}),
#     ("T2", {"I2", "I4"}),
#     ("T3", {"I2", "I3"}),
#     ("T4", {"I1", "I2", "I4"}),
#     ("T5", {"I1", "I3"}),
#     ("T6", {"I2", "I3"}),
#     ("T7", {"I1", "I3"}),
#     ("T8", {"I1", "I2", "I3", "I5"}),
#     ("T9", {"I1", "I2", "I3"}),
# ]


dataset = [
    (100, {1, 3, 4}),
    (200, {2, 3, 5}),
    (300, {1, 2, 3, 5}),
    (400, {2, 5}),
]


# dataset = [
#     (1, {"Bread", "Milk"}),
#     (2, {"Bread", "Diaper", "Beer", "Eggs"}),
#     (3, {"Milk", "Diaper", "Beer", "Coke"}),
#     (4, {"Bread", "Milk", "Diaper", "Beer"}),
#     (5, {"Bread", "Milk", "Diaper", "Coke"}),
# ]


# dataset = [
#     (100, {"F", "A", 'D', "B"}),
#     (200, {"D", "A", 'C', 'E', 'B'}),
#     (300, {"C", "A", 'B', 'E'}),
#     (400, {"B", "A", 'D'}),
# ]


def get_support_count(items):
    cnt = 0
    for tid, item in dataset:
        if item.issuperset(items):
            cnt += 1

    return cnt


def get_support(items):
    return get_support_count(items)/len(dataset)


def findsubsets(s, n):
    return list(map(set, itertools.combinations(s, n)))


def is_sub_list(sub_list, lst):

    for element in sub_list:
        if element in lst:
            continue
        else:
            return False
    return True


def get_candidates(frequest_itemset, K):
    candidate_set = []
    for item_i in frequest_itemset:
        for item_j in frequest_itemset:

            generated_set = item_i.union(item_j)
            subsets = findsubsets(generated_set, K-1)
            
            if len(generated_set) == K and is_sub_list(subsets, frequest_itemset):
                candidate_set.append(generated_set)

    return tuple(candidate_set)


def find_frequent_itemsets(min_sup):
    frequest_itemsets = []  # list of tuple of set
    candidate_itemsets = []  # list of tuple of set

    one_itemset = set()
    for tid, item in dataset:
        one_itemset.update(item)

    candidate_itemset = tuple([{item} for item in one_itemset])
    print("=================================")
    print("Frequent Itemsets")
    print("=================================")

    print(f"K=1")
    print("Candidate Itemsets")
    [print("Items : " + str(candidate_item) + " Support: " +
           str(get_support_count(candidate_item))) for candidate_item in candidate_itemset]

    K_frequest_itemets = [
        one_item for one_item in candidate_itemset if get_support_count(one_item) >= min_sup]
    frequest_itemsets.append(
        tuple(K_frequest_itemets))

    print("Frequent Itemsets")
    [print("Items : " + str(frequest_itemset) + " Support: " +
           str(get_support_count(frequest_itemset))) for frequest_itemset in K_frequest_itemets]

    for K in range(1, len(dataset)):
        candidate_itemset = get_candidates(frequest_itemsets[K-1], K=K+1)

        print(f"K={K+1}")
        print("Candidate Itemsets")
        [print("Items : " + str(candidate_item) + " Support: " +
               str(get_support_count(candidate_item))) for candidate_item in candidate_itemset]

        K_frequest_itemets = []
        for candidate_item in candidate_itemset:
            if get_support_count(candidate_item) >= min_sup:
                if candidate_item not in K_frequest_itemets:
                    K_frequest_itemets.append(candidate_item)

        print("Frequent Itemsets")
        [print("Items : " + str(K_frequest_itemet) + " Support: " +
               str(get_support_count(K_frequest_itemet))) for K_frequest_itemet in K_frequest_itemets]

        if len(K_frequest_itemets) == 0:
            break

        frequest_itemsets.append(tuple(K_frequest_itemets))

    output_frequent_itemsets = []
    for frequest_itemset in frequest_itemsets:
        output_frequent_itemsets += list(frequest_itemset)

    return output_frequent_itemsets


def get_rules(frequest_itemset, min_confidence):
    rules = []
    processed = []

    to_process = [frequest_itemset]
    while to_process:
        whole_set = to_process.pop(0)
        rule_len = len(whole_set) - 1

        sub_sets = findsubsets(whole_set, rule_len)

        for sub_set in sub_sets:
            if sub_set in processed:
                continue
            processed.append(sub_set)
            if sub_set and (x:= frequest_itemset - sub_set):
                confidence = get_support_count(
                    frequest_itemset) / get_support_count(sub_set) * 100
                support = get_support_count(
                    frequest_itemset) / len(dataset) * 100
                if confidence >= min_confidence:
                    rules.append((sub_set, x, confidence, support))
                    to_process.append(sub_set)
    return rules


def main():
    min_sup = float(input("Enter Minimun Support : "))
    min_confidence = float(input("Enter Minimun confidence for Rules : "))
    frequest_itemsets = find_frequent_itemsets(min_sup)

    print("Frequest Itemsets :- ")
    print("\nSET   :  SUPPORT ")

    for frequest_itemset in frequest_itemsets:
        print(f"{frequest_itemset} : {get_support_count(frequest_itemset)}")

    print("\nRULES\n")
    for frequest_itemset in frequest_itemsets:
        print("==========================")
        rules = get_rules(frequest_itemset, min_confidence)
        if not rules:
            print(f"No rules for {frequest_itemset} -")
            continue
        print(f"Rules for {frequest_itemset} -")

        for rule_x, rule_y, confidence, support in rules:
            if rule_y == set():
                rule_y = "{}"
            print(
                f"{rule_x} -> {rule_y}  Confidence : {confidence} Support : {support}")
    print("==========================")


if __name__ == "__main__":
    main()
