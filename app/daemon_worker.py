import threading
import time

class DaemonWorker(threading.Thread):
    def __init__(self, interval=2):
        super().__init__()
        self.daemon = True
        self._running = threading.Event()
        self._running.set()
        self.interval = interval

    def run(self):
        while self._running.is_set():
            print("Daemon worker is working...")
            time.sleep(self.interval)

    def stop(self):
        self._running.clear()

    def set_interval(self, interval):
        if interval <= 0:
            raise ValueError("Interval must be a positive value")
        self.interval = interval

    def get_interval(self):
        return self.interval
