import csv
import numpy as np

class FestoStateCalibrations:
    def __init__(self, csv_file_location):
        
        self.festo_states = []
        self.calibration_file_name = []

        with open(csv_file_location, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            next(csv_reader)  # Skip the header row
            
            for row in csv_reader:
                #print(row[0:12])   
                self.festo_states.append(row[0:12])
                self.calibration_file_name.append(row[12:13])
            
            #print(self.festo_states[1])
            #print(self.calibration_file_name[1])
    


if __name__ == "__main__":

    A_Win = 'TemperatureFit\calibration_file_table.csv'
    A_Lin = 'TemperatureFit/calibration_file_table.csv'

    Calibrations = FestoStateCalibrations(A_Lin)

    print(Calibrations.calibration_file_name)

    test_list = [1,0,0,0,1,0,0,0,0,0,1,0]

