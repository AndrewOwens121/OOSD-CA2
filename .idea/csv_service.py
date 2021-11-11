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

    # def calculate_averages(self):
    #     self.header.append("Avg Grade")
    #     for item in self.data:
    #         g1 = int(item[3])
    #         g2 = int(item[4])
    #         g3 = int(item[5])
    #         avg = round((g1+g2+g3)/3,2)
    #         print(f"{item[1]}, has an average of {avg}")
    #         item.append(avg)

    def write_data(self):
        with open(self.filename,"w") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(self.header)
            csv_writer.writerows(self.data)