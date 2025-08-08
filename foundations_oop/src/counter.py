class Counter:
    def __init__(self, start=0):
        self.count = int(start)

    def inc(self, step=1):
        self.count += step
        return self.count

    def dec(self, step=1):
        self.count -= step
        return self.count
