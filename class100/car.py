import os
import shutil
class Car(object):
    def __init__(self,brand,colour,brake,quality):
        self.brand=brand,
        self.colour=colour,
        self.brake=brake,
        self.quality=quality
    def start(self):
        print("Started")
    def stop(self):
        print("Stoped")
    def acceleration(self):
        print("Accelerating")
audi=Car("audi","blue","nice","excellent")
BMW=Car("BMW","black","good","extraordinary")
print(BMW.colour)
