"""
Michael Thompson
ECON 380
Final Script
"""
import csv
import numpy as np
import pandas as pd
from os.path import exists
from os.path import abspath

from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.gaussian_process import GaussianProcessRegressor

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import TheilSenRegressor

from sklearn.neural_network import MLPRegressor

from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor

from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split


class Constants:
    No = 0.0
    Yes = 1.0

    AirMiles = 1.0
    Points = 2.0
    CashBack = 3.0

    Letter = 1.0
    Postcard = 2.0

    Low = 1.0
    Medium = 2.0
    High = 3.0

    Train = 'final_train.csv'
    Test = 'final_test.csv'
    Result = 'final_results.csv'


class FinalScript:
    def __init__(self):
        self._final_train = pd.read_csv(Constants.Train)
        FinalScript.numberize_train_array(self._final_train)
        imputer = SimpleImputer(strategy='median')
        x = imputer.fit_transform(self._final_train)

        self._final_train = pd.DataFrame(x, columns=self._final_train.columns, index=self._final_train.index)
        self._final_train = self._final_train.drop("Customer Number", axis=1)

        self._final_test = pd.read_csv(Constants.Test)
        FinalScript.numberize_test_array(self._final_test)
        imputer = SimpleImputer(strategy='median')
        x = imputer.fit_transform(self._final_test)

        self._final_test = pd.DataFrame(x, columns=self._final_test.columns, index=self._final_test.index)
        self._final_number = self._final_test["Customer Number"].copy()
        self._final_test = self._final_test.drop("Customer Number", axis=1)

        self._final_train_features = self._final_train.copy()
        self._final_train_labels = self._final_train_features["Offer Accepted"].copy()
        self._final_train_features = self._final_train_features.drop("Offer Accepted", axis=1)

        np.random.seed(380)
        train_features, test_features = train_test_split(self._final_train,
                                                         test_size=0.2, random_state=380)
        self._train_features = train_features
        self._test_features = test_features

        self._train_label = self._train_features["Offer Accepted"].copy()
        self._train_features = self._train_features.drop("Offer Accepted", axis=1)

        self._test_label = self._test_features["Offer Accepted"].copy()
        self._test_features = self._test_features.drop("Offer Accepted", axis=1)

        self._best_regression = None

        self._predictions = []

    def run_best_regression(self):
        if self._best_regression is not None:
            print("Running Best Found Regression")
            results = FinalScript.regression_check(
                self._best_regression,
                self._final_train_features, self._final_train_labels,
                self._final_test)

            results = np.where(results == -0.0, 0.0, results)
            FinalScript.write_results(results, self._final_number)
        else:
            return 0

    @staticmethod
    def write_results(results, numbers):
        if not exists(Constants.Result):
            f = open(Constants.Result, 'w')
            f.close()

        with open(Constants.Result, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            i = 0
            writer.writerow(['Customer Number', 'Offer Accepted'])
            for row in results:
                writer.writerow([numbers[i], row])
                i += 1
            print("RESULTS WRITTEN TO: " + abspath(Constants.Result))

    def test_all_regression(self):
        # Test all different regression types
        results = []

        # Ensemble Methods
        results.append(
            FinalScript.regression_check(
                AdaBoostRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))

        results.append(
            FinalScript.regression_check(
                BaggingRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))

        results.append(
            FinalScript.regression_check(
                ExtraTreesRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))
        results.append(
            FinalScript.regression_check(
                GradientBoostingRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))
        results.append(
            FinalScript.regression_check(
                RandomForestRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))

        # Gaussian Process
        results.append(
            FinalScript.regression_check(
                GaussianProcessRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))

        # Linear Models
        results.append(
            FinalScript.regression_check(
                LinearRegression,
                self._train_features, self._train_label,
                self._test_features, self._test_label))

        results.append(
            FinalScript.regression_check(
                TheilSenRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))

        # Neural Network
        results.append(
            FinalScript.regression_check(
                MLPRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))

        # Decision Trees
        results.append(
            FinalScript.regression_check(
                DecisionTreeRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))

        results.append(
            FinalScript.regression_check(
                ExtraTreeRegressor,
                self._train_features, self._train_label,
                self._test_features, self._test_label))

        results = sorted(results, key=lambda x: x[1])
        print("ORDER OF REGESSION, BEST FIRST")
        for row in results:
            print(row[0].__name__ + ",\t" + str(row[1]))
        print()
        self._best_regression = results[0][0]
        return results

    @staticmethod
    def mse_error_check(label, predict):
        mse_test = mean_squared_error(label, predict)
        print("MEAN SQUARED ERROR: " + str(mse_test))

        return mse_test

    @staticmethod
    def number_error_check(label, predict):
        j = 0
        i = 0
        for row in label:
            if predict[i] == row:
                j += 1
            i += 1
        print("CORRECT: " + str(j) + "\tOUT OF: " + str(len(label)))

    @staticmethod
    def regression_check(Regressor, train_features, train_label, test_features, test_label=None):
        print(Regressor.__name__)
        regressor = Regressor()
        regressor.fit(train_features, train_label)

        print("Train Data")
        regressor_predict = regressor.predict(train_features)
        FinalScript.mse_error_check(train_label, regressor_predict)
        regressor_predict = regressor_predict.round(decimals=0)
        FinalScript.number_error_check(train_label, regressor_predict)

        # Test Data
        regressor_predict = regressor.predict(test_features)

        if test_label is not None:
            print("Test Data")
            result = FinalScript.mse_error_check(test_label, regressor_predict)
            regressor_predict = regressor_predict.round(decimals=0)
            FinalScript.number_error_check(test_label, regressor_predict)
            print("\n")
            return Regressor, result
        else:
            regressor_predict = regressor_predict.round(decimals=0)
            return regressor_predict

    @staticmethod
    def csv_file_open(path):
        temp = []
        with open(path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                temp.append(row)

        return temp

    @staticmethod
    def numberize_train_array(array):
        array['Offer Accepted'] = array['Offer Accepted'].replace({'No': Constants.No,
                                                                   'Yes': Constants.Yes})

        array['Reward'] = array['Reward'].replace({'Air Miles': Constants.AirMiles,
                                                   'Points': Constants.Points,
                                                   'Cash Back': Constants.CashBack})

        array['Mailer Type'] = array['Mailer Type'].replace({'Letter': Constants.Letter,
                                                             'Postcard': Constants.Postcard})

        array['Income Level'] = array['Income Level'].replace({'Low': Constants.Low,
                                                               'Medium': Constants.Medium,
                                                               'High': Constants.High})

        array['Overdraft Protection'] = array['Overdraft Protection'].replace({'No': Constants.No,
                                                                               'Yes': Constants.Yes})

        array['Credit Rating'] = array['Credit Rating'].replace({'Low': Constants.Low,
                                                                 'Medium': Constants.Medium,
                                                                 'High': Constants.High})

        array['Own Your Home'] = array['Own Your Home'].replace({'No': Constants.No,
                                                                 'Yes': Constants.Yes})

        return array

    @staticmethod
    def numberize_test_array(array):
        array['Reward'] = array['Reward'].replace({'Air Miles': Constants.AirMiles,
                                                   'Points': Constants.Points,
                                                   'Cash Back': Constants.CashBack})

        array['Mailer Type'] = array['Mailer Type'].replace({'Letter': Constants.Letter,
                                                             'Postcard': Constants.Postcard})

        array['Income Level'] = array['Income Level'].replace({'Low': Constants.Low,
                                                               'Medium': Constants.Medium,
                                                               'High': Constants.High})

        array['Overdraft Protection'] = array['Overdraft Protection'].replace({'No': Constants.No,
                                                                               'Yes': Constants.Yes})

        array['Credit Rating'] = array['Credit Rating'].replace({'Low': Constants.Low,
                                                                 'Medium': Constants.Medium,
                                                                 'High': Constants.High})

        array['Own Your Home'] = array['Own Your Home'].replace({'No': Constants.No,
                                                                 'Yes': Constants.Yes})

        return array


if __name__ == "__main__":
    final = FinalScript()
    final.test_all_regression()
    final.run_best_regression()
