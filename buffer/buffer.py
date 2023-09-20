from utils.utils import log_print


class Buffer:
    """
    Buffer stores incoming sales transactions
    """

    queue = []

    def __init__(self, max_size=10):
        self.max_size = max_size

    def push(self, sale):
        self.clean()
        self.queue.append(sale)

    def read_latest(self):
        """
        Returns and removes the last transaction in the que
        """
        if self.queue:
            latest = self.queue[-1]
            self.queue.remove(latest)
            return latest
        else:
            log_print("No queue")
            return None

    def clean(self):
        """
        deletes the oldest record transaction so a new one can be added
        """
        if self.queue:
            self.queue.pop(0)
