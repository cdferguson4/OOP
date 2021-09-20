from datetime import date

class Student:
    def __init__(self,id,name,dob,classification):
        self.__studentid = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ''



    def get_age(self):
        return self.__age
    
    def get_registration(self):
        return self.__register

    def register(self):
        if self.__classification == "Seniors":
            self.__register = "11/1 Thru 11/3"
        else:
            if self.__classification == "Juniors":
                self.__register = "11/4 Thru 11/6"
            else:
                if self.__classification == "Sophmores":
                    self.__register = "11/7 Thru 11/9"
                else:
                    if self.__classification == "Freshman":
                        self.__register = "11/10 Thru 11/12"
                    else:
                        self.__register = "Classification not Found"
    def calc_age(self):
        t = date.today()
        bday = self.__dob.split('/')
        age = t.year -  int(bday[2])
        self.__age = age       