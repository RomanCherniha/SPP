from read_csv import CSVReader
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from cube import Cube

SHAPE_CLASSES = {
    "triangle": Triangle,
    "rectangle": Rectangle,
    "square": Square,
    "cube": Cube
}

class Main:
    def __init__(self, file_path):
        self.file_path = file_path
        self.csv_reader = CSVReader(self.file_path)

    def process_shapes(self):
        shapes_data = self.csv_reader.read_csv()

        for shape_name, sides in shapes_data:
            shape_class = SHAPE_CLASSES.get(shape_name.lower())

            if shape_class:
                shape = shape_class(sides)
                shape.log()
            else:
                print(f"Unknown shape: {shape_name}")

if __name__ == "__main__":
    processor = Main("shapes.csv")
    processor.process_shapes()
