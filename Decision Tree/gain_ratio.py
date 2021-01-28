import math

# attribute_names = ["a", "b", "c", "d", "label"]

# dataset = [
#     (1, 2, 3, 4, 0),
#     (1, 2, 3, 4, 0),
#     (1, 2, 3, 4, 0),
#     (1, 2, 3, 4, 0),
#     (1, 2, 3, 4, 1),
# ]


attribute_names = ["age", "income", "label"]

dataset = [
    (0, 2, 0),
    (0, 2, 0),
    (1, 2, 1),
    (2, 1, 1),
    (2, 0, 1),
    (2, 0, 0),
    (1, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
    (2, 1, 1),
    (0, 1, 1),
    (1, 1, 1),
    (1, 2, 1),
    (2, 1, 0),
]


def get_feature(index): return [x[index] for x in dataset]


labels = get_feature(-1)


def get_entropy(pi):
    if pi == 0:
        return pi
    return -pi*math.log(pi, 2)


def get_probability(label, lst):
    return sum([1 for ele in lst if ele == label]) / len(lst)


def get_info(attribute):
    unique_labels = set(attribute)
    info = 0
    for unique_label in unique_labels:
        prob = get_probability(unique_label, labels)
        info += get_entropy(prob)
    return -info


def get_info_root(y, n):
    total = y+n
    return get_entropy(y/total) + get_entropy(n/total)


def get_attribute_info(attribute):
    unique_labels = set(attribute)
    return get_info_root(*[attribute.count(unique_label)
                           for unique_label in unique_labels])


def main():
    dataset_info = get_attribute_info(labels)
    print(f"Dataset Info : {dataset_info}")
    gain_ratios = []
    for i, attribute_name in enumerate(attribute_names):
        if(i+1 == len(attribute_names)):
            break
        attribute_col = get_feature(i)
        unique_classes = set(attribute_col)

        info = 0
        split_info = 0
        for unique_class in unique_classes:
            total_cnt = 0
            pos_cnt = 0
            for attr, label in zip(attribute_col, labels):
                if attr == unique_class:
                    total_cnt += 1
                    pos_cnt += label
            split_info += get_entropy(total_cnt/len(labels))
            info += total_cnt/len(labels) * \
                get_info_root(pos_cnt, total_cnt-pos_cnt)

        gain_ratio = (dataset_info-info)/split_info
        print(f"Gain Ratio for {attribute_name} : {gain_ratio}")
        gain_ratios.append(gain_ratio)

    print("==============================")
    for name, gain in zip(attribute_names[:-1], gain_ratios):
        print(f"{name}: {gain}")


if __name__ == '__main__':
    main()
