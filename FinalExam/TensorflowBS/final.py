"""
Michael Thompson
ECON 380
Final Script
"""
import csv
import numpy as np
from os.path import exists
from keras.models import Sequential
from keras.layers import Dense

import time

import matplotlib.pyplot as plt


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
        self._final_train = FinalScript.csv_file_open(Constants.Train)
        self._final_test = FinalScript.csv_file_open(Constants.Test)

        self._final_train.pop(0)
        self._final_test.pop(0)

        self.numberize_array(self._final_train, 1)
        self.numberize_array(self._final_test, -1)

        self._final_train = np.array(self._final_train)
        self._final_test = np.array(self._final_test)

    @staticmethod
    def csv_file_open(path):
        temp = []
        with open(path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                temp.append(row)

        return temp

    def keras_model(self, epochs, batch_size):
        x = self._final_train[:, 2:17]
        y = self._final_train[:, 1]

        self._model = Sequential()
        self._model.add(Dense(1000, input_dim=15, activation='relu'))
        self._model.add(Dense(1000, activation='relu'))
        self._model.add(Dense(1, activation='sigmoid'))

        self._model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self._model.fit(x, y, epochs=epochs, batch_size=batch_size)

        _, accuracy = self._model.evaluate(x, y)
        print('Accuracy: %.2f' % (accuracy * 100))

        # x = self._final_test[:, 1:16]

        self._predictions = self._model.predict(x)

        for i in range(0, len(self._predictions)):
            self._predictions[i] = self._predictions[i] * 100.0



        n, bins, patches = plt.hist(x=self._predictions, bins='auto')
        maxfreq = n.max()
        plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
        plt.ylabel('Number of applicants')
        plt.xlabel('Probability of approval')
        plt.show()

        for i in range(0, len(self._predictions)):
            if self._predictions[i] < 8.469783866361006:
                self._predictions[i] = 0
            else:
                self._predictions[i] = 1

        self.write_results()

        sorted(self._predictions)
        return self._predictions[13581][0]

    def save_model(self):
        self._model.save('models/big_model' + str(time.time()))

    def column_prob(self, column):
        rewards = []
        results_dict = {}
        for row in self._final_train:
            if row[column] not in rewards:
                rewards.append(row[column])
                results_dict[str(row[column]) + '_no'] = 0
                results_dict[str(row[column]) + '_yes'] = 0

            if row[1] == 'No':
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

    def write_results(self):
        if not exists(Constants.Result):
            f = open(Constants.Result, 'w')
            f.close()

        with open(Constants.Result, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            i = 1.0
            writer.writerow(['Customer Number', 'Offer Accepted'])
            for row in self._predictions:
                writer.writerow([i, row])
                i += 1.0


if __name__ == "__main__":
    final = FinalScript()
    results = []

    start_time = time.time()
    end_time = start_time
    print("STARTING")
    results.append(final.keras_model(50, 50))
    end_time = time.time()


    """
    print("FINAL MODEL")

    results = final.keras_model(400, 1)
    final.save_model()

    with open('test2.txt', 'w', newline='') as f:
        for result in results:
            f.write(str(result) + "\n")
        f.write(str(sum(results) / len(results)))
        """
