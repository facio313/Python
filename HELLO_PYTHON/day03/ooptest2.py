from day03.ooptest import Animal

class Human(Animal):
    def __init__(self):
        print("생성자")
        self.age = 0
        self.language = 0
    
    def momstouch(self, stroke):
        self.language += stroke
    
    def __del__(self):
        print("소문자")
        
if __name__ == '__main__':
    hum = Human()
    
    print(hum.age)
    print(hum.language)
    
    hum.getOlder()
    hum.momstouch(7)
    
    print(hum.age)
    print(hum.language)