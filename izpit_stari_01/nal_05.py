"""
- calculate the date that is n(input) days away from date1(input)
- print out today's date
- exit the program
"""

import datetime


class Nal05:
    def __init__(self, date1=input("Enter first date"), n=input("Enter number of days")):
        self.date1 = date1
        self.n = n

    def days_from_date1(self):
        date1_lst = self.date1.split(" ")
        date_plus_n = datetime.date(int(date1_lst[0]), int(date1_lst[1]), int(date1_lst[2]))
        for i in range(int(self.n)):
            date_plus_n += datetime.timedelta(days=1)
        print(date_plus_n)

    @staticmethod
    def todays_date():
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

x = Nal05()
x.days_from_date1()
x.todays_date()
