"""
Create a Time class and initialize it with hours and minutes.
1. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
2. Make a method displayTime which should print the time.
3. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
"""

class Time:
    def __init__(self,hours=None,minutes=None):
        self.hours=hours
        self.minutes=minutes

    def addTime(self,time1,time2):
        self.hours=time1.hours+time2.hours+int((time1.minutes+time2.minutes)/60)
        self.minutes=(time1.minutes+time2.minutes)%60
    def displayTime(self):
        print("Time=",str(self.hours)+"H:"+str(self.minutes)+"M")
    def displayMinute(self):
        totalMinute=(self.hours*60)+self.minutes
        print("Total Minute:",totalMinute)
        


time1=Time(1,45)
time2=Time(3,150)
time3=Time()
time3.addTime(time1,time2)
time3.displayTime()
time3.displayMinute()
