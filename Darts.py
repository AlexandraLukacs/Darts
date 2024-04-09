#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random

class Darts():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        # self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        #stopper óra
        self.ido = StopWatch()

    def csipog(self):
            self.ev3.speaker.play_file("laser.wav")
    
    def csipog2(self):
            self.ev3.speaker.play_file("uh-oh.wav")

    def darts1(self):
        # Kör alakú céltábla
        # Kijelző méretei:0-177*0-122 bal belső sarok (0,0)
        # képernyő törlése
        self.ev3.screen.clear()
        # Körünk
        self.ev3.screen.draw_circle(90, 60, 50, fill=True, color=Color.BLACK)
        
        # 10 véletlen lövés
        db = 0
        for loves in range(0, 10, 1):
            x= random.randint(0, 177)
            y= random.randint(0, 127)

            if (90-x)**2+(60-y)**2<=50**2:
                # Talált
                self.ev3.screen.draw_circle(x, y, 2, fill=True, color=Color.WHITE)
                db += 1
                self.csipog()
            else:
                # Nem talált
                self.ev3.screen.draw_circle(x, y, 2, fill=True, color=Color.BLACK)
                self.csipog2()
            wait(300)
        # Találatok számának kiiratása
        szoveg = "Találat: " + str(db) + "."
        self.ev3.screen.draw_text(80, 100, szoveg, text_color=Color.WHITE, background_color=Color.BLACK)

        wait(5000)

    def darts2a(self):
        # Animáljuk a golyó mozgását, a. letörlés módszerrel
        # Tábla kirajzolása
        # bal szélére véletlenszerűen megjelenik a golyó
        r= 5
        y= random.randint(0+r, 127-r)
        # golyó mozgatása
        for x in range(0,177+r+1,1):
            # Céltábla kiírása
            self.ev3.screen.draw_box(172, 40, 177, 80, fill=True, color=Color.BLACK)
            # Kirajzoljuk a kört
            self.ev3.screen.draw_circle(x, y, r, fill=True, color=Color.BLACK)
            wait(30)
            # Letörlöm
            self.ev3.screen.clear()

        wait(5000)

    def darts2b(self):
        # Animáljuk a golyó mozgását, b. letörlés módszerrel
        # Tábla kirajzolása
        self.ev3.screen.draw_box(172, 40, 177, 80, fill=True, color=Color.BLACK)
        # bal szélére véletlenszerűen megjelenik a golyó
        r= 5
        y= random.randint(0+r, 127-r)
        # golyó mozgatása
        for x in range(0,177+r+1,1):
            # Kirajzoljuk a kört
            self.ev3.screen.draw_circle(x, y, r, fill=True, color=Color.BLACK)
            wait(30)
            # Eltakarom egy másik körrel
            self.ev3.screen.draw_circle(x, y, r, fill=True, color=Color.WHITE)

        wait(5000)

    def darts3(self):
        # Animáljuk a golyó mozgását, a. letörlés módszerrel
        # Tábla kirajzolása
        self.ev3.screen.draw_box(172, 40, 177, 80, fill=True, color=Color.BLACK)
        # bal szélére véletlenszerűen megjelenik a golyó
        r= 5
        y= random.randint(0+r, 127-r)
        yiranya= random.randint(-1,1)
        # golyó mozgatása
        for x in range(0,177+r+1,1):
            # Minden 8. lépésben változzon y kordináta
            if x%8 == 0:
                # y kordináta változási iránya
                y += yiranya
            # Kirajzoljuk a kört
            self.ev3.screen.draw_circle(x, y, r, fill=True, color=Color.BLACK)
            wait(30)
            # Eltakarom egy másik körrel
            self.ev3.screen.draw_circle(x, y, r, fill=True, color=Color.WHITE)

        wait(5000)