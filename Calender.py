class Calender():
    Timing_slots_map = {
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,
        10: False,
        11: False,
        12: False,
        13: False,
        14: False,
        15: False,
        16: False,
        17: False,
        18: False,
        19: False,
        20: False,
        21: False,
        22: False,
        23: False,
        24: False
    }
    def __init__(self):
        pass

    def schedule(self, start: int, end: int):
        for i in range(start, end):
            if self.Timing_slots_map[i] == True:
                return False
            

        for i in range(start, end):
            self.Timing_slots_map[i] = True
        
        return True


calender = Calender() 

print(calender.schedule(start = 5,end = 10))
print(calender.schedule(start = 8, end = 13))
print(calender.schedule(start = 10,end =15))
print(calender.schedule(start = 10,end =15))
print(calender.schedule(start = 9,end =12))
print(calender.schedule(start = 13,end =15))
print(calender.schedule(start = 15,end =16))

