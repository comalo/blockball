from blockball import *

# Hier setzen wir einige Variablen auf Anfangswerte
BILDSCHIRM_BREITE = 600
BILDSCHIRM_HOEHE = 600
BILDSCHIRM_TITEL = "Hüpfendes Reckteck"

RECHTECK_BREITE = 90
RECHTECK_HOEHE = 10


class Block:

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


    def aktualisiere(self, sekunden_seit_letztem_aufruf, spiel):
        self.mitte_x += self.diff_x * sekunden_seit_letztem_aufruf
        self.mitte_y += self.diff_y * sekunden_seit_letztem_aufruf
        # Berühren wir den rechten Rand ?
        if self.mitte_x < self.breite // 2 \
                or self.mitte_x > spiel.breite - self.breite // 2:
            self.diff_x *= -1
        # Berühren wir den linken Rand ?
        if self.mitte_y < self.höhe // 2 \
                or self.mitte_y > spiel.höhe - self.höhe // 2:
            self.diff_y *= -1


    def bei_tastendruck(self, welche_taste, taste_modifikator, spiel):
         pass

    def ist_anderer_rechts(self, anderer_block : 'Block'):
        ich_rechts = self.mitte_x + self.breite/2
        anderer_links = anderer_block.mitte_x - anderer_block.breite/2
        return anderer_links>ich_rechts

    def ist_anderer_links(self, anderer_block : 'Block'):
        ich_links = self.mitte_x - self.breite/2
        anderer_rechts = anderer_block.mitte_x + anderer_block.breite/2
        return anderer_rechts<ich_links
        
    def kollidiert_mit(self, anderer_block : 'Block'):
        rechts_x1 = self.mitte_x - self.breite/2


class Spieler(Block):

    def bei_tastendruck(self, welche_taste, taste_modifikator, spiel):
        if welche_taste == taste.MOTION_LEFT:
            self.diff_x = -50
        if welche_taste == taste.MOTION_RIGHT:
            self.diff_x = 50

        if welche_taste == taste.MOTION_UP:
            self.diff_y = abs(self.diff_y)
        if welche_taste == taste.MOTION_DOWN:
            self.diff_y = -abs(self.diff_y)



class Blockweg(Block):
    pass


dinge = [Block(breite=90, höhe=10, mitte_x=86, mitte_y=140, farbe=(0, 0, 255), diff_x=0, diff_y=0),
         Block(breite=90, höhe=10, mitte_x=387, mitte_y=229, farbe=(0, 0, 255), diff_x=0, diff_y=0),
         Block(breite=90, höhe=10, mitte_x=98, mitte_y=326, farbe=(0, 0, 137), diff_x=0, diff_y=0),
         Block(breite=90, höhe=10, mitte_x=401, mitte_y=67, farbe=(22, 77, 255), diff_x=0, diff_y=0),
         Block(breite=90, höhe=10, mitte_x=229, mitte_y=165, farbe=(0, 0, 25), diff_x=0, diff_y=0),
         Block(breite=90, höhe=10, mitte_x=185, mitte_y=418, farbe=(111, 0, 255), diff_x=0, diff_y=0),
         Block(breite=90, höhe=10, mitte_x=372, mitte_y=274, farbe=(4, 97, 28), diff_x=0, diff_y=0),
         Block(breite=90, höhe=10, mitte_x=168, mitte_y=256, farbe=(66, 2, 255), diff_x=0, diff_y=0),
         Block(breite=90, höhe=10, mitte_x=246, mitte_y=396, farbe=(44, 0, 5), diff_x=0, diff_y=0),
         Spieler(breite=10, höhe=10, mitte_x=20, mitte_y=160, farbe=(222, 222,9), diff_x=-0,diff_y=100),
        Block (breite=90, höhe=10, mitte_x=445, mitte_y=323, farbe=(255, 23, 205), diff_x=0, diff_y=0),
        Blockweg(breite=100, höhe=70, mitte_x=60, mitte_y=500, farbe=(107, 23, 5), diff_x=-0, diff_y=0),
         Blockweg(breite=100, höhe=70, mitte_x=141, mitte_y=500, farbe=(107, 60, 5), diff_x=-0, diff_y=0),
        Blockweg(breite=100, höhe=70, mitte_x=232, mitte_y=500, farbe=(107, 23, 5), diff_x=-0, diff_y=0),
         Blockweg(breite=100, höhe=70, mitte_x=333, mitte_y=500, farbe=(107, 60, 5), diff_x=-0, diff_y=0),
        Blockweg (breite=100, höhe=70, mitte_x=426, mitte_y=500, farbe=(107, 23, 5), diff_x=-0, diff_y=0)]

class Blockball(SpielFenster):

    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

    def am_anfang(self):
        self.set_update_rate(1.0 / 60)
        setz_hintergrund_farbe((255, 255, 255))
        self.sekunden_seit_letztem_aufruf = 0.0
        self.sekunden = 0

    def zeichne_bild(self):
        beginne_bild()
        for box in dinge:
            box.zeichne_dich()

    def aktualisiere(self, sekunden_seit_letztem_aufruf):
        self.sekunden_seit_letztem_aufruf = sekunden_seit_letztem_aufruf
        self.sekunden += sekunden_seit_letztem_aufruf
        for ding in dinge:
            ding.aktualisiere(sekunden_seit_letztem_aufruf, self)

    def bei_tastendruck(self, welche_taste, taste_modifikator):
        for box in dinge:
            box.bei_tastendruck(welche_taste, taste_modifikator, self)


def starte():
    """ Main method """
    blockball = Blockball(500, 500, "Blockball")
    blockball.am_anfang()

    leg_los()

if __name__ == "__main__":
    starte()
