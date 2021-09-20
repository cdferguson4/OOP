import Insect_Class as i

def main():
    mosquito = i.Insect(2,4)
    housefly = i.Insect(3,5)

    print("We are going to see how far the insect can fly")
    mosquito.fly()
    housefly.fly()

    print("This is how far the mosquito flew: ",mosquito.getflight())
    print("this is how far the housefly flew",housefly.getflight())















main()