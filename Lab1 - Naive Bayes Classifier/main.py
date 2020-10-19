
LABEL_COLUMN = "Play Golf"
DELTA = 0.000000001


# def read_data():
#     import csv
#     DATASET_PATH = "Dataset.csv"

#     file = open(DATASET_PATH)
#     reader = csv.reader(file)
#     headers = next(reader)
#     data = list(reader)
#     return data, headers

# data, headers = read_data()
 
data = [['Rainy', 'Hot', 'High', 'False', 'No'], ['Rainy', 'Hot', 'High', 'True', 'No'], ['Overcast', 'Hot', 'High', 'False', 'Yes'], ['Sunny', 'Mild', 'High', 'False', 'Yes'], ['Sunny', 'Cool', 'Normal', 'False', 'Yes'], ['Sunny', 'Cool', 'Normal', 'True', 'No'], ['Overcast', 'Cool', 'Normal', 'True', 'Yes'], ['Rainy', 'Mild', 'High', 'False', 'No'], ['Rainy', 'Cool', 'Normal', 'False', 'Yes'], ['Sunny', 'Mild', 'Normal', 'False', 'Yes'], ['Rainy', 'Mild', 'Normal', 'True', 'Yes'], ['Overcast', 'Mild', 'High', 'True', 'Yes'], ['Overcast', 'Hot', 'Normal', 'False', 'Yes'], ['Sunny', 'Mild', 'High', 'True', 'No']]
headers = ['Outlook ', 'Temp ', 'Humidity ', 'Windy ', 'Play Golf']

col_vector = {}
for header in headers:
    col_vector[header] = []

LABEL_COLUMN_INDEX = headers.index(LABEL_COLUMN)

for i, col in enumerate(col_vector.keys()):
    for row in data:
        col_vector[col].append(row[i])


PREDICTION_LABELS = list(set(col_vector[LABEL_COLUMN]))


def count_instances(data_list, query):
    return sum([1 for data in data_list if data == query])


def initial_probability():
    return {PREDICTION_LABEL: count_instances(col_vector[LABEL_COLUMN], PREDICTION_LABEL) / len(col_vector[LABEL_COLUMN]) for PREDICTION_LABEL in PREDICTION_LABELS}


def count_condition_instances(data_list, label, index, query):

    total_cnt = 0
    instance_cnt = 0

    for row in data:
        if row[LABEL_COLUMN_INDEX] == label:
            total_cnt += 1
            if row[index] == query:
                instance_cnt += 1

    if instance_cnt == 0 :
        return DELTA / total_cnt
    return instance_cnt / total_cnt


def get_features_probability(features, column):
    prob = {}
    for PREDICTION_LABEL in PREDICTION_LABELS:
        prob[PREDICTION_LABEL] =  count_condition_instances(data, PREDICTION_LABEL, headers.index(column), features[column])

    return prob

def prod_list(lst, pred):
    ans = 1
    for k, x in lst.items():
        ans *= x[pred]
    return ans


def predict(features):
    prior_probability = initial_probability()
    
    features_probability = {}
    for header in headers[:-1]:
        features_probability[header] = 0

    for col in features_probability.keys():
        features_probability[col] = get_features_probability(features, col)


    result = {}
        
    print("\n\nRESULT\n")    
    for PREDICTION_LABEL in PREDICTION_LABELS:
        probability = prior_probability[PREDICTION_LABEL] * prod_list(features_probability, PREDICTION_LABEL)
        result[PREDICTION_LABEL] = probability
        print(f"P({PREDICTION_LABEL} | {features}) = {probability}" ) 
    
        

    ans = result.values()
    ans_index = list(ans).index(max(ans))
    prediction = PREDICTION_LABELS[ans_index]
    statement = f"Final Prediction is {prediction}! "

    print(statement)


def get_input():
    print("\nNaive Bayes Classifier")
    print("By - Daniyal Abbasi (17BCS069)\n\n")
    features = {}
    for header in headers[:-1]:
        options = {index: value for index, value in enumerate(set(col_vector[header]))}
        features[header] = options[int(input(f"Choose {header} {options} \nChoice :- " ))]
    return features
    
if __name__ == "__main__":
    features = get_input()
    predict(features)
