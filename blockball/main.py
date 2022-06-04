from blockball import *

# Hier setzen wir einige Variablen auf Anfangswerte
BILDSCHIRM_BREITE = 600
BILDSCHIRM_HOEHE = 600
BILDSCHIRM_TITEL = "Hüpfendes Reckteck"

RECHTECK_BREITE = 90
RECHTECK_HOEHE = 10
JA = True
NEIN = False
FALSCH = False
WAHR = True

class Rechteck:

    def __init__(self, breite, höhe, mitte_x, mitte_y, farbe, diff_x, diff_y):
        self.breite = breite
        self.höhe = höhe
        self.farbe = farbe
        self.mitte_x = mitte_x
        self.mitte_y = mitte_y
        self.diff_x = diff_x
        self.diff_y = diff_y

    def zeichne_dich(self):
        zeichne_gefülltes_rechteck(self.mitte_x, self.mitte_y,
                                   self.breite, self.höhe,
                                   self.farbe)

boxen=[ Rechteck(breite=90,höhe=10,mitte_x=444,mitte_y=123,farbe=(0,0,255), diff_x=110, diff_y=130),
        Rechteck(breite=90,höhe=10,mitte_x=55,mitte_y=123,farbe=(0,0,255), diff_x=110, diff_y=130),
        Rechteck(breite=90,höhe=10,mitte_x=554,mitte_y=148,farbe=(0,0,137), diff_x=110, diff_y=100),
        Rechteck(breite=90,höhe=10,mitte_x=404,mitte_y=123,farbe=(22,77,255), diff_x=110, diff_y=130),
        Rechteck(breite=90,höhe=10,mitte_x=204,mitte_y=123,farbe=(0,0,25), diff_x=110, diff_y=130),
        Rechteck(breite=90,höhe=10,mitte_x=288,mitte_y=478,farbe=(111,0,255), diff_x=200, diff_y=130),
        Rechteck(breite=90,höhe=10,mitte_x=343,mitte_y=123,farbe=(4,97,28), diff_x=110, diff_y=13),
        Rechteck(breite=90,höhe=10,mitte_x=46,mitte_y=166,farbe=(66,2,255), diff_x=110, diff_y=130),
        Rechteck(breite=90,höhe=10,mitte_x=114,mitte_y=122,farbe=(44,0,5), diff_x=110, diff_y=130),
        Rechteck(breite=10,höhe=90,mitte_x=204,mitte_y=123,farbe=(0,0,205), diff_x=-310, diff_y=330),
        Rechteck(breite=90,höhe=10,mitte_x=204,mitte_y=333,farbe=(0,0,255), diff_x=110, diff_y=130),
        Rechteck(breite=90,höhe=10,mitte_x=444,mitte_y=123,farbe=(66,7,25), diff_x=110, diff_y=130)]

def zeichne_bild(sekunden_seit_letzem_aufruf):
    # Starte den Zeichner, das muss am Anfang einmal passieren
    beginne_bild()
    for box in boxen:
        box.zeichne_dich()

        box.mitte_x += box.diff_x * sekunden_seit_letzem_aufruf
        box.mitte_y += box.diff_y * sekunden_seit_letzem_aufruf

        # Berühren wir den rechten Rand ?
        if box.mitte_x < RECHTECK_BREITE // 2 \
                or box.mitte_x > BILDSCHIRM_BREITE - RECHTECK_BREITE // 2:
            box.diff_x *= -1
        # Berühren wir den linken Rand ?
        if box.mitte_y < RECHTECK_HOEHE // 2 \
                or box.mitte_y > BILDSCHIRM_HOEHE - RECHTECK_HOEHE // 2:
            box.diff_y *= -1


def start():
    öffne_fenster(BILDSCHIRM_BREITE, BILDSCHIRM_HOEHE, BILDSCHIRM_TITEL)
    setz_hintergrund_farbe((255,255,255))
    mach_wiederholt(zeichne_bild, 1 / 60)
    leg_los()


if __name__ == "__main__":
    start()