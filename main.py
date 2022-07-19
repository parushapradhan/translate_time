import time

current_time = time.localtime()

hour = int(time.strftime("%I", current_time))
minute = int(time.strftime("%M", current_time))

def translate_time(hour, minute):
    numbers = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen',
            'fourteen', 'fifteen', 'sixteen',
            'seventeen', 'eighteen', 'nineteen',
            'twenty', 'twenty one', 'twenty two',
            'twenty three', 'twenty four',
            'twenty five', 'twenty six', 'twenty seven',
            'twenty eight', 'twenty nine'];
    if minute <= 30:
        translated_hour = numbers[hour]
    else:
        if hour == 12:
            translated_hour = numbers[1]
        else:
            translated_hour = numbers[hour + 1]

    if (minute == 0):
        print(translated_hour, "o' clock");
 
    elif (minute == 1):
        print("one minute past", translated_hour);
 
    elif (minute == 59):
        print("one minute to", translated_hour);
 
    elif (minute == 15):
        print("quarter past", translated_hour);
 
    elif (minute == 30):
        print("half past", translated_hour);
 
    elif (minute == 45):
        print("quarter to", translated_hour);
 
    elif (minute <= 30):
        print(numbers[minute],"minutes past", translated_hour);
 
    elif (minute > 30):
        print(numbers[60 - minute], "minutes to", translated_hour);
 
translate_time(hour, minute);