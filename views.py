import json
from controller import AddUserToTour, AddUserToTrip, make_tour, make_trip, save_user
from my_redis import r


print("wellcome...!")



while True:
    u_choice=input("u==>for add passenger\ntr==>for add trip\nto==>for add tour\nshow_tr==> for show certian trip\nshow_to===>for show certain tour\nq==>for exit\n")

    if u_choice=="u":
        name = input("name :")
        age = input("age: ")
        phone = input("phone: ")
        if r.exists(f"user {phone}"):
            print("this phone number is exist...!")
            continue
        else:
            U={"name":name,"age":age,"phone":phone}
            person = json.dumps(U)
            save_user(person,phone)
            ch = input("tr/to?\n")
            if ch=="tr":
                print(r.keys())
                tr_ch=input("choice id of one trip:\n")
                AddUserToTrip(phone,tr_ch)
                print("sucsses...!")
                continue


            elif ch=="to":
                print(r.keys())
                to_ch=input("choice id of one tour:\n")
                AddUserToTour(phone,to_ch)
                print("sucsses...!")
                continue


            else:
                print("invalid input...!")
                continue


    elif u_choice=="tr":
        initial = input("initial:\n")
        destination = input("destination:\n")
        price = input("price:\n")
        passangers = []

        Tr={"initial":initial,"destination":destination,"price":price,"passangers":passangers}
        Trip = json.dumps(Tr)
        make_trip(Trip)
        continue


    elif u_choice=="to":
        leader = input("leader:\n")
        durtions = input("durtions:\n")
        about = input("about:\n")
        passangers = []

        To = {"leader":leader,"passangers":passangers,"durtions":durtions,"about":about}
        Tour = json.dumps(To)
        make_tour(Tour)
        continue


    elif u_choice=="q":
        break

    elif u_choice=="show_tr":
        id= input("id:\n")
        print(r.get(f"trip.{id}"))



    elif u_choice=="show_to":
        id= input("id:\n")
        print(r.get(f"tour.{id}"))



    else:
        print("invalid input...!")
        continue







