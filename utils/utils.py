class Utils():

    def __init__(self):
        self._name = 'utils'

    def add(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('The input argument should be Integer')
        
        return a+b

    def minus(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('The input argument should be Integer')
        
        return a-b   

    def times(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('The input argument should be Integer')
        
        return a*b

    def divided(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('The input argument should be Integer')
        
        if b == 0:
            raise ValueError("The divided number can not be zero")

        return a/b