import task

def main():
    #Task1 and Task2 (Task2 inherits Task 1 thats why it isnt initialized)
    task2 = task.Task2()

    task2.display_table()
    
    late_arrivals = task2.get_late_arrivals()
    average_min_late = task2.avg_of_mins_late()
    highest_late_days = task2.highest_late_days()
    average_min_late_late_days = task2.avg_of_mins_late(ignore_on_time=True)

    print(f'number of late arrivals -> {late_arrivals}\n')
    print(f'the average number of minutes late for each bus route -> {average_min_late}\n')
    print(f'the bus route with the highest number of days on which it was late -> {highest_late_days}\n')
    print(f'the average number of minutes late for each bus route, using only data from days on which it was -> {average_min_late_late_days}\n')

    #Task 3 which inherits from Task 1 aswell
    while True:
        task3 = task.Task3()
        print(f'number of late busses on this day ->{task3.late_busses()}\n\n')
        task3.display_late_busses()

        choice = input('Want info about another day?[y/n]')
        if choice == 'y':
            continue
        else:
            break
            
    f = input('Press any key to exit')

if __name__ == '__main__':
    main()
