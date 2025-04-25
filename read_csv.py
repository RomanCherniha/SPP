import csv

class CSVReader:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def read_csv(self):
        shapes = []

        with open(self.file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  

            for row in reader:
                if not row or len(row) < 2:  
                    continue

                shape = row[0]
                sides = [int(side) for side in row[1:] if side.isdigit()]  
                shapes.append((shape, sides))
        return shapes