# logging with a real world example

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithmetic App")

def add(a,b):
    res = a+b
    logger.debug(f"Adding {a}+{b}={res}")
    return res


def substract(a,b):
    res = a+b
    logger.debug(f"Substracting {a}-{b}={res}")
    return res


def multiply(a,b):
    res = a+b
    logger.debug(f"Multiply {a}*{b}={res}")
    return res


def divide(a,b):
    try:
        res = a/b
        logger.debug(f"Dividing {a}/{b}={res}")

        return res
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    

add(10,15)
substract(15,10)
multiply(10,20)
divide(20,0)