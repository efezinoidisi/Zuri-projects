class Student:
    # [assignment] Skeleton class. Add your code here
    #   
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self,name):
        name = name
        return print("You've changed your name from",self.name,"to",name)
    
    def change_age(self,age):
        age = age
        return print("You've changed your age from",self.age," to",age)
        
    def add_track(self,tracks):
        tracks = self.tracks.append(tracks)
        return print("You've added a new track",self.tracks)
    
    def get_score(self):
        return print("Your Score is",self.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()