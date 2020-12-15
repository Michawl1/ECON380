"""
Michael Thompson
ECON 380
Final Script
"""
import csv
import numpy as np
from numpy import loadtxt


from keras.models import Sequential
from keras.layers import Dense

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


class FinalScript:
    def __init__(self):
        self._final_train = FinalScript.csv_file_open('final_train.csv')
        self._final_test = FinalScript.csv_file_open('final_test.csv')

        self._final_train.pop(0)
        self._final_test.pop(0)

        self.numberize_array(self._final_train, 1)
        self.numberize_array(self._final_test, -1)

        self._final_train = np.array(self._final_train)
        self._final_test = np.array(self._final_test)

        x = self._final_train[:, 2:17]
        y = self._final_train[:, 1]

        self._model = Sequential()
        self._model.add(Dense(20, input_dim=15, activation='relu'))
        self._model.add(Dense(15, activation='relu'))
        self._model.add(Dense(1, activation='sigmoid'))

        self._model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self._model.fit(x, y, epochs=500, batch_size=14399)

        _, accuracy = self._model.evaluate(x, y)
        print('Accuracy: %.2f' % (accuracy * 100))

        x = self._final_test[:, 1:16]

        predictions = self._model.predict_classes(x)
        for row in predictions:
            print(row)
            i += 1



    @staticmethod
    def csv_file_open(path):
        temp = []
        with open(path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                temp.append(row)

        return temp

    def column_prob(self, column):
        rewards = []
        results_dict = {}
        for row in self._final_train:
            if row[column] not in rewards:
                rewards.append(row[column])
                results_dict[str(row[column]) + '_no'] = 0
                results_dict[str(row[column]) + '_yes'] = 0

            if row['Offer Accepted'] == 'No':
                results_dict[str(row[column]) + '_no'] += 1
            else:
                results_dict[str(row[column]) + '_yes'] += 1

        return results_dict

    def numberize_array(self, array, offerIndex):
        for i in range(0, len(array)):
            for j in range(0, len(array[i])):
                if array[i][j] == 'No':
                    array[i][j] = Constants.No
                elif array[i][j] == 'Yes':
                    array[i][j] = Constants.Yes
                elif array[i][j] == 'Air Miles':
                    array[i][j] = Constants.AirMiles
                elif array[i][j] == 'Points':
                    array[i][j] = Constants.Points
                elif array[i][j] == 'Cash Back':
                    array[i][j] = Constants.CashBack
                elif array[i][j] == 'Letter':
                    array[i][j] = Constants.Letter
                elif array[i][j] == 'Postcard':
                    array[i][j] = Constants.Postcard
                elif array[i][j] == 'Low':
                    array[i][j] = Constants.Low
                elif array[i][j] == 'Medium':
                    array[i][j] = Constants.Medium
                elif array[i][j] == 'High':
                    array[i][j] = Constants.High
                elif array[i][j] == '':
                    array[i][j] = 0
                else:
                    array[i][j] = float(array[i][j])

                if j == offerIndex:
                    array[i][j] = int(array[i][j])


if __name__ == "__main__":
    final = FinalScript()
