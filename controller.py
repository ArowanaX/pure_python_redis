
import json
from my_redis import r



def save_user(self,phone):
    r.set(f"{phone}",self)



def make_trip(self):
    id= input("id:\n")
    r.set(f"trip.{id}",self)
    print("saved...!")
    return




def make_tour(self):
    id= input("id:\n")
    r.set(f"tour.{id}",self)
    print("saved...!")
    return



def AddUserToTrip(User,tr_ch):
    T=r.get(f"trip.{tr_ch}")
    T=json.loads(T)
    T["passangers"].append(User)
    T=json.dumps(T)
    r.set(f"trip.{tr_ch}",T)

    
    

def AddUserToTour(User,to_ch):
    T=r.get(f"tour.{to_ch}")
    T=json.loads(T)
    T["passangers"].append(User)
    T=json.dumps(T)
    r.set(f"tour.{to_ch}",T)