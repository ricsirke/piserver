class ThreadX(Thread):
    def __init__(self):
        self.continue = True

    def run(self, loop):
        while (self.continue):
            loop

    def stop(self):
        self.continue = False