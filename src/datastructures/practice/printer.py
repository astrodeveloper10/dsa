from src.datastructures.implementations.queue_impl import QueueImpl

class Printer:
    def __init__(self):
        self.queue = QueueImpl()

    def queue_print_job(self, document):
        self.queue.enqueue(document)

    def run(self):
        while self.queue.read():
            self.print_document(self.queue.dequeue())

    def print_document(self, document):
        print(document)


printer = Printer()
printer.queue_print_job("Document 1")
printer.queue_print_job("Document 2")
printer.queue_print_job("Document 3")

printer.run()