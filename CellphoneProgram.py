import CellphoneClass

def main():

    phone_manufacture = input('Enter the Phone Manufacturer: ')
    
    phone_model = input("Enter the Phone Model: ")

    phone_price = float(input("Enter the Phone Price: "))

    phone = CellphoneClass.Phone(phone_manufacture,phone_model,phone_price)

    phone_manufacture.set_manufact(phone    )

    phone_model.set_model(phone_model)

    phone_price.set_retail_price(phone_price)


    print(phone_model.get_model())


















main()