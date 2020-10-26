import math


dataset_x = [[2.7810836,2.550537003],
	[1.465489372,2.362125076],
	[3.396561688,4.400293529],
	[1.38807019,1.850220317],
	[3.06407232,3.005305973],
	[7.627531214,2.759262235],
	[5.332441248,2.088626775],
	[6.922596716,1.77106367],
	[8.675418651,-0.242068655],
	[7.673756466,3.508563011]]

dataset_y = [0,0,0,0,0,1,1,1,1,1]

def euclidean_distance(p1, p2):
    assert len(p1) == len(p2)

    squared_sum = 0
    for x1,x2 in zip(p1,p2):
        squared_sum += (x1-x2)**2

    mean_squared_sum = squared_sum / len(p1)
    
    return math.sqrt(mean_squared_sum)


def find_closest_k(total_distances,K):
    total_distances = sorted(total_distances)
    k_distances = total_distances[:K]
    
    return k_distances


def find_prediction(closest_k):
    class_labels = set(dataset_y)
    class_labels_count = {}
    for label in class_labels:
        class_labels_count[label] = 0


    for data in closest_k:
        class_labels_count[data[1]] +=1
    
    return max(class_labels_count, key=class_labels_count.get) 



def find_total_distance(input_x):
    total_distance = []
    for i, x in enumerate(dataset_x):
        distance = euclidean_distance(x,input_x)
        label = dataset_y[i]
        total_distance.append((distance, label))
    
    return total_distance


def get_input():
    input_data = []
    K = int(input("Enter the value of K :- "))

    for i in range(len(dataset_x[0])):
        x = float(input(f"Enter x{i+1} = "))
        input_data.append(x)

    return K, input_data



def main():
    K, input_x = get_input()
    total_distance = find_total_distance(input_x)
    closest_k = find_closest_k(total_distance,K)
    prediction = find_prediction(closest_k)
    print(f"Final Prediction is : {prediction} ")

    
if __name__ == "__main__":
    main()


        