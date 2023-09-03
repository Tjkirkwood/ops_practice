

class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def __lt__(self, other):
        return self.length * self.width < other.lenght * other.width
    
    def __nul__(self,number):
        self.length = number
        self.width = number

    def __repr__(self):
        return f""
    
