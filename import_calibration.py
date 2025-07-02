import csv
import numpy as np

class FestoStateCalibrations:
    def __init__(self, csv_file_location):
        
        self.festo_states = np.empty(12)
        self.calibration_file_name = np.empty(1)

        with open(csv_file_location, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            next(csv_reader)  # Skip the header row
            
            for row in csv_reader:
                #print(row[0:12])   
                self.festo_states = np.vstack((self.festo_states, row[0:12]))
                self.calibration_file_name = np.vstack((self.calibration_file_name, row[12:13]))

            self.festo_states = np.delete(self.festo_states, (0), axis=0)
            self.calibration_file_name = np.delete(self.calibration_file_name, (0), axis=0)
    


if __name__ == "__main__":

    A_Win = 'TemperatureFit\calibration_file_table.csv'
    A_Lin = 'TemperatureFit/calibration_file_table.csv'

    Calibrations = FestoStateCalibrations(A_Lin)

    print(Calibrations.festo_states)
    print(Calibrations.calibration_file_name)

    test_list = [1,0,0,0,1,0,0,0,0,0,1,0]

