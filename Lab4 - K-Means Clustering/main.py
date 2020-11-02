import random
import matplotlib.pyplot as plt

K = 5
NUMBER_OF_ITERATION = 10
DELTA = 0.0001

dataset = [
    [15, 39],
    [15, 81],
    [16, 6],
    [16, 77],
    [17, 40],
    [120, 79],
    [126, 28],
    [126, 74],
    [137, 18],
]


def cluster_assignment(X, mu):
    C = []
    for i in range(len(X)):
        distance_array = []
        for centroid in range(len(mu)):
            temp_arr = []
            for x1, x2 in zip(X[i], mu[centroid]):
                temp_arr.append(abs(x1-x2))
            distance = sum(temp_arr)
            distance_array.append(distance)
        C.append(distance_array.index(min(distance_array)))
    return C


def centroid_recalculation(X, C, NUMBER_OF_CENTROID):
    mu_new = []
    for k in range(NUMBER_OF_CENTROID):
        new_loc = []
        all_points = []
        for i in range(len(X)):
            if C[i] == k:
                all_points.append(X[i])

        for col in range(len(dataset[0])):
            temp_sum = 0
            for point in all_points:
                temp_sum += point[col]

            
            if len(all_points) == 0:
                new_loc.append(temp_sum/DELTA)
            else:    
                new_loc.append(temp_sum/len(all_points))

        mu_new.append(new_loc)
    return mu_new


def calculate_cost(X, C, mu):
    cost = 0
    for i in range(len(X)):
        temp_arr = []
        for x1, x2 in zip(X[i], mu[C[i]]):
            temp_arr.append(abs(x1-x2))
        cost += sum(temp_arr)
    return cost



def plot_clusters(X, C, NUMBER_OF_CENTROID):
    colors = ['red','blue','green','black', 'brown']

    for k in range(NUMBER_OF_CENTROID):
        for i in range(len(X)):
            if C[i] == k:
                plt.scatter(X[i][0], X[i][1], color=colors[k])

    plt.show()


def main():

    INITIAL_CENTEROIDS = random.choices(dataset, k=K)
    mu = INITIAL_CENTEROIDS
    J = []
    for i in range(NUMBER_OF_ITERATION):
        C = cluster_assignment(dataset, mu)
        mu_new = centroid_recalculation(dataset, C, K)

        J.append(calculate_cost(dataset, C, mu_new))

        if not i == 0:
            if J[i] == J[i-1]:
                break
        mu = mu_new
    
    plot_clusters(dataset, C, K)


if __name__ == "__main__":
    main()
