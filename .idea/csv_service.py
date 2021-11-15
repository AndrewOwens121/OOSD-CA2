import csv

class CSVService:
    def __init__(self,filename):
        self.filename = filename
        self.header = []
        self.data = []

    def read_data(self):
        with open(self.filename, "w") as csvfile:
            readCSV = csv.reader(csvfile, delimiter = ',')
            self.header = next(readCSV)
            for row in readCSV:
                self.data.append(row)

    def write_data(self,data=[]):
        with open(self.filename,"w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            self.data = data
            #csv_writer.writerow(self.header)
            csv_writer.writerows(self.data)