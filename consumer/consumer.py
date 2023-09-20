import time
from utils.utils import log_print


class Consumer:
    """
    Consumes transactions from the buffer
    """

    transaction_processed = 0
    total_sales = 0
    product_sales = {
        "apple": 0,
        "banana": 0,
        "strawberry": 0,
        "grape": 0,
        "pineapple": 0,
    }

    def __init__(self, buffer, interval_seconds=10):
        self.buffer = buffer
        self.interval = interval_seconds

    def __str__(self):
        return f"ConsumerHistory(Total Sales: {self.total_sales}, Product Sales: {self.product_sales})"

    def start(self):
        """
        Start consumer
        """
        while True:
            time.sleep(self.interval)
            self.consume()

    def consume(self):
        """
        Keep track of total transactions, total sales and product sales
        """
        log_print("Consuming")
        latest = self.buffer.read_latest()
        if latest is not None:
            self.transaction_processed += 1
            self.total_sales += latest.amount
            self.product_sales[latest.product] += latest.amount
            log_print(self)
        else:
            log_print("Nothing to consume")
