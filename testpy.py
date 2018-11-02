class Test:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __repr__(self):
        return self.first + self.last 

if __name__ == '__main__':
    de = Test('naveen', 'prashanth')
    print(de)
