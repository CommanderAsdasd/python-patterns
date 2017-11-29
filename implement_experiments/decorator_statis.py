def foo(a: 'x', b: 5 + 6, c: list) -> max(2, 9):
    print(4)

foo(1, 2, (2, 4))

class TestDecorator(object):
    """docstring for TestDecorator"""
    def __init__(self, arg):
        super(TestDecorator, self).__init__()
        self.arg = arg
    @classmethod
    def print_static():
            print("No instance needed!")    


TestDecorator.print_static()