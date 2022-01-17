from my_redis import r 

class user:

    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone
        



class trip:
    
    def __init__(self,initial,destination,price,passangers):
        self.initial = initial
        self.destination = destination
        self.price = price
        self.passangers = passangers
       


class tour :

    def __init__(self,leader,passangers,duration,about):
        self.leadr = leader
        self.duration = duration
        self.about = about
        self.passangers = passangers
    
