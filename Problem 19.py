# Problem 19: How many Sundays fell on the first of the month during the twentieth century?

# Solution: There are plenty of datetime packages in python that will do the heavy lifting for us, but the spirit of the problem is to go without those.

class date:
    def __init__(self):
        self.weekday = 1
        self.calendar = 1
        self.month = 1
        self.year = 1900
        self.weekdayDict = dict({1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"})
        self.monthDict = dict({1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 0: "December"})

    def identify(self): #Mostly for debugging purposes.
        print(f"Today is {self.weekdayDict[self.weekday]} the {self.calendar}th day of {self.monthDict[self.month]}, in the year {self.year}")
        return

    def checkLeap(self):
        if (self.year%4 ==0 and self.year%100 != 0) or self.year%400 == 0:
            return True
        else:
            return False

    def tomorrow(self):
        self.weekday = (self.weekday+1)%7
        if (self.month == 9 or self.month == 4 or self.month == 6 or self.month == 11) and self.calendar == 30:
            self.calendar = 1
            self.month = (self.month + 1)%12
        elif self.month == 2:
            if (self.checkLeap() and self.calendar == 29) or (not self.checkLeap() and self.calendar == 28):
                self.calendar = 1
                self.month = 3
            else:
                self.calendar += 1
        elif (self.month == 1 or self.month==3 or self.month==5 or self.month==7 or self.month==8 or self.month == 10) and self.calendar == 31:
            self.calendar =1
            self.month += 1
        elif self.month == 0 and self.calendar ==31:
            self.calendar = 1
            self.year += 1
            self.month += 1
        else:
            self.calendar += 1
        return

d = date()
#Now that we have an object that will track the date, the rest is straightforward.

# First fast forward to the first day of the 20th century.
while d.year == 1900:
    d.tomorrow()
    #d.identify()

#Then count the number of Sundays that fall on the first of the month
ans = 0
while d.year <2001:
    if d.calendar == 1 and d.weekday ==0:
        ans += 1
    d.tomorrow()

print(f"There were {ans} Sundays that fell on the first of the month")