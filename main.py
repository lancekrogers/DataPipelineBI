from buffer.buffer import Buffer
from consumer.consumer import Consumer
from producer.producer import Producer
from utils.utils import log_print
import threading
import logging


def setup():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    log_print("Setting up data pipeline")

    buffer = Buffer()
    consumer = Consumer(buffer, 1)
    producer = Producer(buffer)
    return consumer, producer


def run(consumer, producer):
    log_print("Running data pipeline")

    # Start a producer and consumer thread
    producer_thread = threading.Thread(target=producer.start)
    consumer_thread = threading.Thread(target=consumer.start)

    # Start the producer and consumer
    producer_thread.start()
    consumer_thread.start()

    # Wait for both threads to finish
    producer_thread.join()
    consumer_thread.join()


if __name__ == "__main__":
    consumer, producer = setup()
    run(consumer, producer)
