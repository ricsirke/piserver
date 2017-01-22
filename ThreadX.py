import threading

class ThreadX(threading.Thread):
    def __init__(self):
        self.cont = True

    def run(self, loop):
        while self.cont:
            loop()

    def stop(self):
        self.cont = False