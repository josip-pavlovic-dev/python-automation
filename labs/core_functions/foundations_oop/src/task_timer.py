from datetime import datetime


class TaskTimer:
    def __init__(self, name: str):
        self.name = name
        self._start = None
        self._end = None

    def start(self):
        self._start = datetime.now()

    def stop(self):
        self._end = datetime.now()

    def elapsed_seconds(self):
        if self._start is None or self._end is None:
            return 0.0
        return (self._end - self._start).total_seconds()
