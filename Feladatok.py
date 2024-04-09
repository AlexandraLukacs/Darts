#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():

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
            self.ev3.speaker.beep()

    def csipog2(self):
            self.ev3.speaker.play_file("snake_hiss.wav")

    def scanner(self):
        # 2.	A robotképernyőn szeretném ha megjelenne a függőleges vonalak a mintának megfelelően. (scanner)
        # Fényviszonyok:
        # fekete vonal: 10
        # szürke azstal: 74
        # asztalról le: 0
        # félig asztalról le: 15
        self.robot.drive(100,0)
        self.ido.reset()
        hol = 0
        while self.ido.time() < 3000:
            if self.cs.reflection() <(74+10)/2:
                self.ev3.screen.draw_line(hol, 0, hol, 127)
            hol += 1
            wait(3000/178)
        self.robot.stop(Stop.BRAKE)
        wait(10000)

    def elsoa1(self):
        #a.	induljon el a robot álljon meg a vonal után
        # nem lát feketét addig megy
        while self.cs.reflection() >(74+10)/2-20:
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)
        # addig megy amíg feketét lát
        while self.cs.reflection() <(74+10)/2-10:
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)

    def elsoa2(self):
        # a.	induljon el a robot álljon meg a vonal után
        vege = False
        fekete = False
        self.robot.drive(100,0)
        while not vege:
            if self.cs.reflection() < (74+10)/2-20:
                fekete = True
            if fekete and self.cs.reflection() > (74+10)/2-10:
                vege = True
        self.robot.stop(Stop.BRAKE)

    def hanyvonal(self, db, seb, hatar):
        for vonalakSzama in range(db):
            vege = False
            fekete = False
            self.robot.drive(seb,0)
            while not vege:
                if self.cs.reflection() < hatar:
                    fekete = True
                if fekete and self.cs.reflection() > hatar+10:
                    vege = True
            self.robot.stop(Stop.BRAKE)

    def elsob(self):
        #b.	Készíts egy eljárást aminek paraméterül megadjuk hány vonal van, milyen sebeséggel menjen, és hol van a ragasztás határértéke. Az eljárás segítségével járd be a vonalakat.
        hatar = (74+10)/2-20
        self.hanyvonal(5, 100, hatar)
    
    def elsoc(self):
        # c.Ugyanaz mint a b feladat csak hátrafele
        hatar = (74+10)/2-20
        self.hanyvonal(5, -100, hatar)

    def elsod(self):
        #d.	Mérjétek meg milyen széles a csík idővel. Tároljátok egy listába el.
        hosszok = []
        self.robot.drive(100,0)
        for vonalakSzama in range(5):
            vege = False
            fekete = False
            self.robot.drive(100,0)
            while not vege:
                if self.cs.reflection() < (74+10)/2-20 and not fekete:
                    fekete = True
                    self.ido.reset()
                if fekete and self.cs.reflection() > (74+10)/2-10:
                    vege = True
                    hossz = self.ido.time()
                    hosszok.append(hossz)
            self.robot.stop(Stop.BRAKE)
            print(hossz)
        print(hosszok)
        return hosszok

    def elsoe(self):
        # e.	Annyit csipogjon ahányadik helyen van az egy vastagabb.
        hosszok= self.elsod()

        # hosszok kiírása
        # képernyő törlése
        self.ev3.screen.clear()
        for index in range(len(hosszok)):
            ev3.screen.print(hosszok[index])
        wait(5000)

        # Annyit csipogjon ahányadik helyen van az egy vastagabb.

        maxi=0
        mini=0
        for index in range(len(hosszok)):
            if hosszok[index]>hosszok[maxi]:
                maxi = index
            if hosszok[index]<hosszok[mini]:
                maxi = index
        # legnagyobb helyen lévőt
        for index in range(maxi+1):
            self.ev3.speaker.beep()
            wait(100)

    def elsof(self):
        # f.	A vonalak hosszát csipogja vissza
        hosszok= self.elsod()

        # hosszok kiírása
        # képernyő törlése
        self.ev3.screen.clear()
        for index in range(len(hosszok)):
            self.ev3.screen.print(hosszok[index])
        wait(5000)

        maxi=0
        mini=0
        for index in range(len(hosszok)):
            if hosszok[index]>hosszok[maxi]:
                maxi = index
            if hosszok[index]<hosszok[mini]:
                maxi = index

        # vonalak hosszát csipogja vissza
        kozepertek = (hosszok[mini]+hosszok[maxi])/2
        for index in range(len(hosszok)):
            if hosszok[index]<kozepertek:
                self.ev3.speaker.beep(440,100)
                wait(100)
            else:
                self.ev3.speaker.beep(440,200)
                wait(100)
        wait(100)