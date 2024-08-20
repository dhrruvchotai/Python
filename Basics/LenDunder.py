class Demo:

    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)

v1 = Demo([2,13,342,42])
print(len(v1))