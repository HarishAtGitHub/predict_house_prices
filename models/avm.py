import pandas
import sklearn
from sklearn.model_selection import train_test_split


class AVM:
    def __init__(self):
        # STEP 1 : LOAD THE DATA
        data = AVM.__load_data()
        self.d = AVM.__load_data()

        # STEP 2 : SPLIT THE DATA TO TRAINING AND TEST SET
        training_data, test_data = AVM.__split(data, 0.8)

        # STEP 3: CHOOSE A model Mechanism. HERE LET'S CHOOSE LINEAR REGRESSION AND  SEE HOW IT WORKS
        self.__model = AVM.__choose_model()

        # STEP 4: CHOOSE FEATURES TO BE USED TO TRAIN THE MODEL
        self.__features = AVM.__choose_features()

        # STEP 5: FINALIZE THE OUTPUT VARIABLE
        self.__output_variable = AVM.__get_output_variable()

        # STEP 6: TRAIN THE MODEL WITH THE TRAINING SET AND WITH CHOSEN FEATURES
        self.__trained_model = AVM.__train_model(self.__model, training_data, self.__features, self.__output_variable)

    def __predict(self, data):
        return self.__model.predict(data)[0][0]

    @classmethod
    def __get_df(cls, input):
        df = pandas.DataFrame([[input['bedrooms'],
                               input['bathrooms'],
                               input['sqft_living'],
                               input['sqft_lot'],
                               input['floors'],
                               input['zipcode']]],
                              columns=['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode'])
        return df

    def get_price(self, input):
        data = AVM.__get_df(input)
        return self.__predict(data)

    @classmethod
    def __load_data(cls):
        return pandas.read_csv("home_data.csv", header=0)

    @classmethod
    def __split(cls, data, fraction):
        return train_test_split(data, train_size=0.9)

    @classmethod
    def __choose_model(cls):
        from sklearn import linear_model
        return linear_model.LinearRegression()

    @classmethod
    def __choose_features(cls):
        features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']
        return features

    @classmethod
    def __get_output_variable(cls):
        output_variable = 'price'
        return output_variable

    @classmethod
    def __evaluate_model(cls, model, data, features, output_variable):
        size = len(data)
        test_input = data[features]
        expected_output = data[output_variable].values.reshape(size, 1)
        return model.score(test_input, expected_output)

    @classmethod
    def __train_model(cls, model, data, features, output_variable):
        size = len(data)
        actual_input = data[features]
        actual_output = data[output_variable].values.reshape(size, 1)
        trained_model = model.fit(actual_input, actual_output)
        return trained_model