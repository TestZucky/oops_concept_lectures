class Demo:

    def __new__(cls, *args, **kwargs):
        print('calling new')
        return super().__new__(cls)

    def __init__(self, x):
        print('calling init')
        self.x = x

    def __del__(self):
        print('cleaning up')

    def __repr__(self):
        return f'x = {self.x}'



d = Demo(10)
print(d)