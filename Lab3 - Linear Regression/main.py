import matplotlib.pyplot as plt

dataset_x = [[2.7810836],
             [1.465489372],
             [3.396561688],
             [1.38807019],
             [3.06407232],
             [7.627531214],
             [5.332441248],
             [6.922596716],
             [8.675418651],
             [7.673756466]]

dataset_y = [2, 1, 3, 2, 3, 6, 4, 4, 8, 6]


def get_covar():
    y_avg = sum(dataset_y)/len(dataset_y)

    x_avg = []
    for col in range(len(dataset_x[0])):
        avg = sum([x[col] for x in dataset_x])/len(dataset_x)
        x_avg.append(avg)

    total_sum = []

    for col in range(len(dataset_x[0])):
        temp_sum = 0
        for xi, yi in zip(dataset_x, dataset_y):
            temp_sum += (xi[col] - x_avg[col]) * (yi-y_avg)
        total_sum.append(temp_sum)

    return total_sum


def get_var():
    x_avg = []
    for col in range(len(dataset_x[0])):
        avg = sum([x[col] for x in dataset_x])/len(dataset_x)
        x_avg.append(avg)

    temp_sum = 0
    for xi in dataset_x:
        temp_sum += (sum([x - x_a for x, x_a in zip(xi, x_avg)])**2)
    return temp_sum


def get_alpha(beta):
    y_avg = sum(dataset_y)/len(dataset_y)

    x_avg = []
    for col in range(len(dataset_x[0])):
        avg = sum([x[col] for x in dataset_x])/len(dataset_x)
        x_avg.append(avg)

    temp_sum = sum([w*x_a for w, x_a in zip(beta, x_avg)])

    return y_avg - temp_sum


def get_beta():
    var = get_var()
    result = []

    for w in get_covar():
        result.append(w/var)

    return result


def get_input():
    input_data = []

    for i in range(len(dataset_x[0])):
        x = float(input(f"Enter x{i+1} = "))
        input_data.append(x)

    return input_data


def plot_line(alpha,beta):
    x_test = [[x] for x in range(10)]
    y_test = [ ]
    for x in x_test:
        temp_sum_test =  0
        for xi,wi in zip(x, beta):
            temp_sum_test += xi*wi
        y_test.append(alpha+temp_sum_test)
        
    plt.scatter(dataset_x, dataset_y,  color='black')
    plt.plot(x_test, y_test, color='blue', linewidth=2)
    plt.title('Best fit Linear Regression',fontsize=24)

    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

def main():
    input_x = get_input()

    beta = get_beta()
    alpha = get_alpha(beta)

    temp_sum = 0
    for x, w in zip(input_x, beta):
        temp_sum += w*x

    prediction = alpha + temp_sum
    print(f"Final Prediction is : {prediction} ")

    plot_line(alpha, beta)


if __name__ == "__main__":
    main()
