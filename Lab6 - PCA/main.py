
from numpy.linalg import eig
import matplotlib.pyplot as plt


# original_dataset = [
#     [1, 3],
#     [2, 5],
#     [3, 7],
#     [4, 9],
#     [5, 11],
# ]


original_dataset = [
    [73.847017017515, 241.893563180437],
    [68.7819040458903, 162.310472521300],
    [74.1101053917849, 212.7408555565],
    [71.7309784033377, 220.042470303077],
    [69.8817958611153, 206.349800623871],
    [67.2530156878065, 152.212155757083],
    [68.7850812516616, 183.927888604031],
    [68.3485155115879, 167.971110489509],
    [67.018949662883, 175.92944039571],
    [63.4564939783664, 156.399676387112],
    [71.1953822829745, 186.604925560358],
    [71.6408051192206, 213.741169489411],
    [64.7663291334055, 167.127461073476],
    [69.2830700967204, 189.446181386738],
]

feature_len = len(original_dataset[0])


def mean_normalization(dataset):
    normalized_dataset = []
    feature_mean = []
    for feature in range(feature_len):
        sum_feature = 0
        for example in dataset:
            sum_feature += example[feature]
        sum_feature = sum_feature/len(dataset)
        feature_mean.append(sum_feature)

    standard_dev = []
    for feature in range(feature_len):
        std_dev = 0
        for example in dataset:
            std_dev += (example[feature] - feature_mean[feature])**2

        std_dev = std_dev/len(dataset)
        standard_dev.append(std_dev)

    for example in dataset:
        normalized_example = []
        for feature in range(feature_len):
            normalized_example.append(
                (example[feature] - feature_mean[feature]) / standard_dev[feature])
        normalized_dataset.append(normalized_example)
    return normalized_dataset


dataset = mean_normalization(original_dataset)


def get_cov_matrix():
    cov_matrix = [[0 for _ in range(feature_len)] for _ in range(feature_len)]

    for example in dataset:
        for x in range(feature_len):
            for y in range(feature_len):
                cov_matrix[x][y] += example[x] * example[y]

    for x in range(feature_len):
        for y in range(feature_len):
            cov_matrix[x][y] = cov_matrix[x][y] / len(dataset)

    return cov_matrix


def get_reduced_dataset(dataset, eigen_vector, k):
    required_cols = []
    required_cols = [[row[k_i] for row in eigen_vector] for k_i in range(k)]

    final_dataset = []

    for example in dataset:
        feat = []
        for required_col in required_cols:
            val = 0
            for feature in range(feature_len):
                val += required_col[feature] * example[feature]
            feat.append(val)
        final_dataset.append(feat)

    return final_dataset


def plot(dataset):
    if len(dataset[0]) == 2:
        for i in dataset:
            plt.scatter(i[0], i[1], c='red')
        plt.show()
    elif len(dataset[0]) == 1:
        for i in dataset:
            plt.scatter(i[0], 0, c='blue')
        plt.show()
    else:
        return


def main():
    cov_matrix = get_cov_matrix()
    print(cov_matrix)

    eigen_value, eigen_vector = eig(cov_matrix)

    print("Eigen Values :", eigen_value)
    print("Eigen Vector :", )
    for row in eigen_vector:
        for col in row:
            print(col, end="\t")

        print()

    K = int(
        input(f"Enter number of required components : (Max: {len(dataset[0]) - 1}) "))

    reduced_dataset = get_reduced_dataset(original_dataset, eigen_vector, K)
    print("Reduced Dataset : ")
    for row in reduced_dataset:
        for col in row:
            print(col, end="\t")

        print()
    plot(original_dataset)
    plot(reduced_dataset)


if __name__ == "__main__":
    main()
