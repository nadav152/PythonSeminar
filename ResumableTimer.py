import time


class ResumeAbleTimer:

    def __init__(self):
        self.start_time = None
        self.paused_time = None
        self.paused = False

    def start(self):
        """"
        set start timer to curr time
        """
        self.start_time = time.time()

    def pause(self):
        """"
        save curr time when pause
        """
        self.paused_time = time.time()
        self.paused = True

    def resume(self):
        """"
        calculate the time when the timer paused and resume countdown
        """
        if self.paused:
            pause_time = time.time() - self.paused_time
            self.start_time = self.start_time + pause_time
            self.paused = False

    def get(self):
        """"
        return timer countdown
        """
        if self.paused:
            return self.paused_time - self.start_time
        else:
            return time.time() - self.start_time
