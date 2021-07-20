from datetime import datetime

import vlc
p = vlc.MediaPlayer(r"C:\Users\frioss\Documents\Desarrollo\Proyectos_python\beginners_path\01.mp3")

alarm_time = input("Enter the time to alarm to be set: HH:MM:SS\n")
print(alarm_time)
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm...")

while True:
    now = datetime.now()
    print(now)
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if current_hour == alarm_hour:
            if alarm_minute == current_minute:
                if alarm_second == current_second:
                    print("Wake up, Neo!")
                    p.play()