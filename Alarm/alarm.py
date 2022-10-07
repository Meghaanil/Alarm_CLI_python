# from playsound import playsound

import time


# user should follow this format =  HH:MM:SS
# this function validates if this format is Ok or not.

def validate_time(tiMe):
    if len(tiMe) != 8:
        return "Invalid time format! Please try again..."
    else:
        try:
            if int(tiMe[0:2]) > 24:
                return "Invalid HOUR format! Please try again..."
            elif int(tiMe[3:5]) > 59:
                return "Invalid MINUTE format! Please try again..."
            elif int(tiMe[6:]) > 59:
                return "Invalid SECOND format! Please try again..."
            else:
                return "Ok"
        except ValueError:
            print('Invalid format or input')


while True:
    alarm_time = input("Enter time in 'HH:MM:SS' format: ")

    validate = validate_time(alarm_time.lower())

    if validate != "Ok":
        if validate is None:
            print('Try Again ...')
        else:
            print(validate)
    else:
        print()
        print(f"Setting alarm for:  {alarm_time} ...")
        break


# a dictionary to store HH, MM and in order to compare them with
# the current time
alarm_dict = {'alarm_hour': alarm_time[0:2], 'alarm_min': alarm_time[3:5], 'alarm_sec': alarm_time[6:]}


while True:
    # loop through current time to compare with the alarm time

    current_time = time.ctime()
    now = current_time[11:19]
    now_dict = {'hour': now[0:2], 'min': now[3:5], 'sec': now[6:]}

    if alarm_dict['alarm_hour'] == now_dict['hour']:
        if alarm_dict['alarm_min'] == now_dict['min']:
            if alarm_dict['alarm_sec'] == now_dict['sec']:
                print()
                print('Wake Up buddy! Time is up!!!\n')
                # play sound
                break
            else:
                continue
        else:
            continue
    else:
        continue