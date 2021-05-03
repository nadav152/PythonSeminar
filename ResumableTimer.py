from datetime import datetime
import time

class ResumableTimer:

    def __init__(self):
        self.start_time = None
        self.paused_time = None
        self.paused = False

    def start(self):
        self.start_time = time.time()

    def pause(self):
        self.paused_time = time.time()
        self.paused = True

    def resume(self):
        if self.paused:
            pause_time = time.time() - self.paused_time
            self.start_time = self.start_time + pause_time
            self.paused = False

    def get(self):
        if self.paused:
            return self.paused_time - self.start_time
        else:
            return time.time() - self.start_time
