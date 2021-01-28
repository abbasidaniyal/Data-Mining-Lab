import math

# attribute_names = ["a", "b", "c", "d", "label"]

# dataset = [
#     (1, 2, 3, 4, 0),
#     (1, 2, 3, 4, 0),
#     (1, 2, 3, 4, 0),
#     (1, 2, 3, 4, 0),
#     (1, 2, 3, 4, 1),
# ]


# attribute_names = ["age", "income", "label"]

# dataset = [
#     (0, 2, 0),
#     (0, 2, 0),
#     (1, 2, 1),
#     (2, 1, 1),
#     (2, 0, 1),
#     (2, 0, 0),
#     (1, 0, 1),
#     (0, 1, 0),
#     (0, 0, 1),
#     (2, 1, 1),
#     (0, 1, 1),
#     (1, 1, 1),
#     (1, 2, 1),
#     (2, 1, 0),
# ]


attribute_names = ["A", "B", "Class"]

dataset = [
    (1, 0, 1),
    (1, 1, 1),
    (1, 1, 1),
    (1, 0, 2),
    (1, 1, 1),
    (0, 0, 2),
    (0, 0, 2),
    (0, 0, 2),
    (1, 1, 2),
    (0, 1, 1),
]


def get_feature(index): return [x[index] for x in dataset]


labels = get_feature(-1)


def get_probability(label, lst):
    return sum([1 for ele in lst if ele == label]) / len(lst)


def get_attribute_gini(attribute):
    unique_labels = set(attribute)
    return 1 - sum([(attribute.count(unique_label) / len(attribute))**2 for unique_label in unique_labels])


def main():
    dataset_gini = get_attribute_gini(labels)
    print(f"Dataset Info : {dataset_gini}")
    ginis = []
    for i, attribute_name in enumerate(attribute_names):
        if(i+1 == len(attribute_names)):
            break
        attribute_col = get_feature(i)
        unique_classes = set(attribute_col)

        gini = 0
        for unique_class in unique_classes:
            split_dataset = []
            for attr, label in zip(attribute_col, labels):
                if attr == unique_class:
                    split_dataset.append(label)

            gini += (len(split_dataset) / len(labels)) * \
                get_attribute_gini(split_dataset)

        print(f"Gini for {attribute_name} : {gini}")

        ginis.append(gini)

    print("==============================")
    for name, gini in zip(attribute_names[:-1], ginis):
        print(f"{name}: {gini}")


if __name__ == '__main__':
    main()
