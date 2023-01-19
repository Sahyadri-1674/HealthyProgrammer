from pygame import mixer 
from datetime import datetime
from time import time
# mixer.init()
# mixer.music.load("Water.mp3")
# mixer.music.load("Eyes.mp3")
# mixer.music.load("PhysicalExercise.mp3")

# Entrytime = time(9,00,00)
# Exittime = time(17,00,00)
# print(Entrytime)
# print(Exittime)

# water_glass_count = 0
# present_time = datetime.now()
# while  present_time< Exittime:
    # global water_glass_count
    # print("Hello")


def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break

def log_record(msg):
    f = open("HealthyProgrammer.txt","a")
    f.write(f"{msg} {datetime.now()}\n") 
        
if __name__=="__main__":
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    waterSec = 24 * 60
    exSec = 40 * 60  
    eyesSec = 15 * 60

    while True:
        if time() - init_water > waterSec:
            print("Time to Drink Water.Enter 'drank' to stop the reminder.")
            musiconloop('water.mp3','drank')
            init_water = time()
            log_record('Drank Water at')
        if time() - init_eyes > eyesSec:
            print("Give Relaxation to Eyes.Enter 'done' to stop the reminder.")
            musiconloop('Eyes.mp3','done')
            init_eyes = time()
            log_record('Eyes Relaxed at')
        if time() - init_exercise >exSec:
            print("Do some physical Exercise.Enter 'done' to stop the reminder.")
            musiconloop('PhysicalExercise.mp3','done')
            init_exercise = time()
            log_record('Exercise done at')        