class Xi:
    def __init__(self):
        self.index_look = 10
    
    def corona(self):
        self.index_look -= 1

class Trumph:
    def __init__(self):
        self.money = 2
        
    def youfire(self):
        self.money += 1
    
class Kim:
    def __init__(self):
        self.nuclear = 20
    
    def aoji(self):
        self.nuclear += 2

class ParkInSoo(Xi, Trumph, Kim):
    def __init__(self):
        Xi.__init__(self)
        Trumph.__init__(self)
        Kim.__init__(self)
        
if __name__ == '__main__':
    ins = ParkInSoo()
    
    print("index_look", ins.index_look)
    print("money", ins.money)
    print("nuclear", ins.nuclear)
    
    ins.corona()
    ins.youfire()
    ins.aoji()
    
    print("index_look", ins.index_look)
    print("money", ins.money)
    print("nuclear", ins.nuclear)