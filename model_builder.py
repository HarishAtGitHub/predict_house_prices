import pandas
import sklearn
from sklearn.model_selection import train_test_split

""""**********************************************************************************"""
def main():
    # STEP 1 : LOAD THE DATA
    data = load_data()

    # STEP 2 : SPLIT THE DATA TO TRAINING AND TEST SET
    training_data, test_data = split(data, 0.8)

    # STEP 3: CHOOSE A model Mechanism. HERE LET'S CHOOSE LINEAR REGRESSION AND  SEE HOW IT WORKS
    model = choose_model()

    # STEP 4: CHOOSE FEATURES TO BE USED TO TRAIN THE MODEL
    features = choose_features()

    # STEP 5: FINALIZE THE OUTPUT VARIABLE
    output_variable = get_output_variable()

    # STEP 6: TRAIN THE MODEL WITH THE TRAINING SET AND WITH CHOSEN FEATURES
    trained_model = train_model(model, training_data, features, output_variable)

    # STEP 7: EVALUATE THE TRAINED MODEL
    #score = evaluate_model(model, test_data, features, output_variable)

    # STEP 8: Prediction
    ip = data[data['id']==5309101200]
    print('input')
    print(ip)
    print('**************************')
    prediction = predict(model, ip, features)
    print('prediction')
    print(prediction[0][0])
    print('**************************')
    print('actual')
    print(ip[[output_variable]].values[0][0])

    #print(score)

"""*************************************************************************************"""

"""
 UTIL FUNCTIONS
"""
def load_data():
    return pandas.read_csv("home_data.csv", header=0)

"""
   splits the data based on fraction given
   fraction here is a number between 1 to 10
"""
def split(data, fraction):
    return train_test_split(data, train_size=0.9)

def choose_model():
    from sklearn import linear_model
    return linear_model.LinearRegression()

def choose_features():
    features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']
    return features

def get_output_variable():
    output_variable = 'price'
    return output_variable

def evaluate_model(model, data, features, output_variable):
    size = len(data)
    test_input = data[features]
    expected_output = data[output_variable].values.reshape(size, 1)
    return model.score(test_input, expected_output)

def train_model(model, data, features, output_variable):
    size = len(data)
    actual_input = data[features]
    actual_output = data[output_variable].values.reshape(size, 1)
    trained_model = model.fit(actual_input, actual_output)
    return trained_model

def predict(model, data, features):
    return model.predict(data[features])

if __name__ == "__main__":
    main()