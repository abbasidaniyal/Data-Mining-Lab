dataset = [
    (100, {1, 3, 4}),
    (200, {2, 3, 5}),
    (300, {1, 2, 3, 5}),
    (400, {2, 5}),
]

dataset = [
    (100, {"f", "a", "c", "d", "g", "i", "m", "p", }),
    (200, {"a", "b", "c", "f", "l", "m", "o", }),
    (300, {"b", "f", "h", "i", "o", }),
    (400, {"b", "c", "k", "s", "p", }),
    (500, {"a", "f", "c", "e", "l", "p", "m", "n", }),
]


def get_support_count(items):
    cnt = 0
    for tid, item in dataset:
        if item.issuperset(items):
            cnt += 1

    return cnt


def get_support(items):
    return get_support_count(items)/len(dataset)


def support_table(items):
    print("ITEM \t SUPPORT")
    for item in items:
        print(f"{item} -> \t {get_support_count(item)}")


def find_sorted_frequent_itemsets(min_sup):
    one_itemset = set()
    for tid, item in dataset:
        one_itemset.update(item)

    support_table(one_itemset)

    candidate_itemset = tuple([{item} for item in one_itemset])
    K_frequest_itemets = [
        one_item for one_item in candidate_itemset if get_support_count(one_item) >= min_sup]
    sorted_K_frequest_itemets = sorted(
        K_frequest_itemets, key=get_support_count, reverse=True)

    update_db_table = []
    for tid, item in dataset:
        transaction_items = [sorted_K_frequest_itemet for sorted_K_frequest_itemet in sorted_K_frequest_itemets if item.issuperset(
            sorted_K_frequest_itemet)]

        update_db_table.append((tid, tuple(transaction_items)))
        print(f"{tid} -> " + str(tuple(transaction_items)))

    # K_itemsets = []
    # K_frequent_itemsets


def main():
    min_sup = float(input("Enter Minimun Support : "))
    min_confidence = float(input("Enter Minimun confidence for Rules : "))
    frequest_itemsets = find_sorted_frequent_itemsets(min_sup)

    # print("Frequest Itemsets :- ")
    # print("\nSET   :  SUPPORT ")

    # for frequest_itemset in frequest_itemsets:
    #     print(f"{frequest_itemset} : {get_support_count(frequest_itemset)}")

    # print("\nRULES\n")
    # for frequest_itemset in frequest_itemsets:
    #     print("==========================")
    #     rules = get_rules(frequest_itemset, min_confidence)
    #     if not rules:
    #         print(f"No rules for {frequest_itemset} -")
    #         continue
    #     print(f"Rules for {frequest_itemset} -")

    #     for rule_x, rule_y, confidence, support in rules:
    #         if rule_y == set():
    #             rule_y = "{}"
    #         print(
    #             f"{rule_x} -> {rule_y}  Confidence : {confidence} Support : {support}")
    # print("==========================")


if __name__ == "__main__":
    main()
