import random
import time
import uuid
from utils.utils import log_print


class Producer:
    """
    Generate a random sale transaction every 1-3 seconds
    """

    def __init__(self, buffer):
        self.start_flag = False
        self.buffer = buffer

    def start(self):
        log_print("Starting producer...")
        self.start_flag = True
        while self.start_flag:
            second_interval = random.randint(1, 3)
            time.sleep(second_interval)
            self.generate_random_sale()

    def generate_random_sale(self):
        """
        Generates random sale transaction
        """
        id = uuid.uuid4()
        product = random.choice(["apple", "banana", "strawberry", "grape", "pineapple"])
        amount = random.randint(1, 10)
        sale = Sale(id, product, amount)
        log_print(f"Generating random sale: {sale}")
        self.buffer.push(sale)


class Sale:
    def __init__(self, id, product, amount):
        self.id = id
        self.product = product
        self.amount = amount

    def __str__(self):
        return f"Sale(ID: {self.id}, Product: {self.product}, Amount: {self.amount})"
