import Insect_Class as i

def main():
    mosquito = i.Insect()
    housefly = i.Insect()

    print("We are going to see how far the insect can fly")
    mosquito.fly()
    housefly.fly()

    print("This is how far it flew: ",mosquito.getflight())
    print("this is how far the housefly flew",housefly.getflight())














main()