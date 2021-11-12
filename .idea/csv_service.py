import csv

class CSVService:
    def __init__(self,filename):
        self.filename = filename
        self.header = []
        self.data = []

    def read_data(self):
        with open(self.filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter = ',')
            self.header = next(readCSV)
            for row in readCSV:
                self.data.append(row)

    def write_data(self):
        with open(self.filename,"w") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(self.header)
            csv_writer.writerows(self.data)