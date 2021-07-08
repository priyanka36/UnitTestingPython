from loguru import logger

logger.info(f"This is tamplate")
logger.add("logs/information.log",level ="INFO",rotation="10MB")
def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def divide(x, y):

    return x / y


def subtract(x, y):
    return x - y

b= add(3,4)

print(b)