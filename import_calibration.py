import csv

if __name__ == "__main__":

    with open('TemperatureFit\calibration_file_table.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
