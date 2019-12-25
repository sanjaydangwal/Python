class Time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __lt__(self,other):
        return (self.hour < other.hour) or (self.minute < other.minute) or (self.second < other.second)
    def __str__(self):
        return f"hour : {self.hour} \nminute : {self.minute} \nsecond : {self.second}"

t1 = Time(12,34,23)
t2 = Time(13,34,2)
if(t1<t2):
    print(t1)
else:
    print(t2)