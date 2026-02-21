import logging
import os

import numpy as np
import pandas as pd
from dotenv import load_dotenv

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("./log/app.log")
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def add_func(x: int | float, y: int | float) -> int | float:
    return x + y


def show_data(df: pd.DataFrame) -> None:
    print(df)


def main() -> int:
    load_dotenv()
    passwd = os.getenv("PASSWORD")

    if passwd is None:
        logger.error("PASSWORD environment variable not set")
        raise EnvironmentError("PASSWORD environment variable not set")
    else:
        logger.info("Password loaded")

    df = pd.DataFrame(np.array(range(1, 10)).reshape(3, 3))

    data = {
        "Name": ["Martha", "Tim", "Rob", "Georgia"],
        "Maths": [87, 91, 97, 95],
        "Science": [83, 99, 84, 76],
    }
    df2 = pd.DataFrame(data)

    logger.info("Second dataframe created")
    logger.info(add_func(2, 3))
    logger.info(df)
    logger.info(df2)

    return 0


if __name__ == "__main__":
    main()
