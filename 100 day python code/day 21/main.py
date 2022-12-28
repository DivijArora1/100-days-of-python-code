class Animal:
    def __init__(self) -> None:
        self.num_eyes  = 2

    def breathe(self):
        print("inhale,exhale")    

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
    def breathe(self):
        super().breathe()
        print("Under water")    
    def swim(self):
        print("moving in water")         

nemo = Fish()        
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

#list slicing
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[2:5])# c d e
print(piano_keys[2:])#c to g
print(piano_keys[:5])#a to e
print(piano_keys[2:5:2])#c e
print(piano_keys[::2])#a c e g 
print(piano_keys[::-1]) #reverse list
# simmilarly works for tupples

