import random

class Task1:
    def __init__(self):
        weekdays = ['Mon','Tue','Wed','Thu','Fri']
        letters = ['A','B','C','D','E','F']

        self.table = {}
        self.buses = set()
        
        for i in range(0,len(weekdays)):
            for x in range(0,len(weekdays)):
                self.table[f'{weekdays[i]}{x+1}'] = {}
                for f in range(0,len(letters)):
                    self.table[f'{weekdays[i]}{x+1}'][f'Bus{letters[f]}'] = 0
                    self.buses.add(f'Bus{letters[f]}')

        self.get_vals()
        

    def get_vals(self):
        f = [random.randint(-10,10) for i in range(0,150)]
        count = 0
        for i in self.table:
            for x in self.table[i]:
                self.table[i][x] = f[count]
                count += 1

    def display_table(self):
        print('Bus  Day  Time')
        for day in self.table:
            for bus in self.table[day]:
                print(f'{bus}  {day}  {self.table[day][bus]}')

class Task2(Task1):
    def __init__(self):
        Task1.__init__(self)
        self.days = []
        
        for i in self.table:
            self.days.append(self.table[i])
        
        
    def get_late_arrivals(self):
        info = {}
        
        for bus in self.buses:
            late = 0
            for day in self.days:             
                if day[bus] < 0:
                    late += 1
            info[bus] = late
    
        return info

    def avg_of_mins_late(self,ignore_on_time=False):
        info = {}

        for bus in self.buses:
            mins = 0
            repeats = 0
            for day in self.days:
                if ignore_on_time:
                    if day[bus] < 0:
                        mins += day[bus]
                else:             
                    mins += day[bus]
                repeats += 1
            info[bus] = mins/repeats

        return info

    def highest_late_days(self):
        info = self.get_late_arrivals()
        
        biggest = ['',0]
        for bus in info:
            if info[bus] > biggest[1]:
                biggest[1] = info[bus]
                biggest[0] = bus

        indexes = [i for i,x in enumerate(info.values()) if x==biggest[1]]
        if len(indexes) > 1:
            for i in range(1,len(indexes)):
                biggest.insert(0,list(info.keys())[indexes[i]])  
        return biggest

class Task3(Task1):
    def __init__(self):
        Task1.__init__(self)
        self.Buses = []
        
        days = self.table.keys()
        print(days)
        print('')
        d = input('Type here one of the days that you see above to see info about it -> ')

        
        try:
            self.day = self.table[d]              
        except:
            print('ENTER A VALID VALUE!!')
            d = input('Type here one of the days to see info about it -> ')
            self.day = self.table[d]

    def late_busses(self):
        count = 0
        for bus in self.day:
            if self.day[bus] < 0:
                self.Buses.append([bus,self.day[bus]])
                count += 1

        return count
    
    def display_late_busses(self):
        for bus in self.Buses:
            print(f'{bus[0]} was late {bus[1]*-1} min')
            print('')


    

    
