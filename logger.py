import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")

class Logger:
    @staticmethod
    def log_shape(shape):
        from shape import SolidShape  

        if shape.is_valid():
            logging.info(f"{shape.shape} with sides {shape.sides}:")
            logging.info(f"Has area of {shape.area()}")
            logging.info(f"Has perimeter of {shape.perimeter()}")
            if isinstance(shape, SolidShape):
                logging.info(f"Has volume of {shape.volume()}")
        else:
            logging.warning(f"Invalid {shape.shape}")
