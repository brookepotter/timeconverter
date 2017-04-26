def time():
    sec = int( input ('Enter the number of seconds:'.strip())

    time = [] 

    if sec <= 60:
        minutes = sec // 60
        time.append(minutes)

       

    if sec (<= 3600):
        hours = sec // 3600
        time.append(hours)

        

    if sec <= 86400:
        days = sec // 86400
        time.append(days)



        print('The number of minutes is {0:.2f}'.format(time[0])) 
        print('The number of hours is {0:.2f}'.format(time[1]))
        print('The number of days is {0:.2f}'.format(time[2]))

    return 


# operator, symbol , flow control


 