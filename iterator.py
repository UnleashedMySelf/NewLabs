class CustomRange:

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __getitem__(self, item):
        if item >= len(self):
            raise IndexError("CustomRange index out of range")
        return self.low + item

    def __len__(self):
        return self.high - self.low


cr = CustomRange(0, 7)
for i in cr:
    print(i)