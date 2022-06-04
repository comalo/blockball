# Das ist eine sogenannte Programmbibliothek, die stellt Funktionen bereit.
# Sie heisst arcade
from __future__ import annotations
import arcade

from arcade import start_render as beginne_bild, \
            draw_rectangle_filled as zeichne_gefülltes_rechteck, \
            set_background_color as setz_hintergrund_farbe, \
            schedule as mach_wiederholt, \
            open_window as öffne_fenster, \
            run as leg_los, \
            draw_line as zeichne_linie, \
            draw_text as schreib_text, \
            draw_point as zeichne_punkt, \
            draw_lines as zeichne_linien, \
            draw_circle_filled as zeichne_gefüllten_kreis, \
            draw_polygon_filled as zeichne_gefülltes_vieleck, \
            draw_polygon_outline as zeichne_vieleck, \
            draw_circle_outline as zeichne_kreis, \
            load_sound as geräusch_laden, \
            play_sound as geräusch_abspielen, \
            stop_sound as geräusch_stoppen, \
            Sprite, Window, Sound

import arcade.key as taste

class SpielFenster(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, breite, höhe, titel):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(breite, höhe, titel)
        self.breite = breite
        self.höhe = höhe
        self.titel = titel

    def setup(self):
        self.am_anfang()

    def am_anfang(self):
        pass

    def on_draw(self):
        self.zeichne_bild()

    def zeichne_bild(self):
        pass

    def on_update(self, delta_time):
        self.aktualisiere(delta_time)

    def aktualisiere(self, sekunden_seit_letztem_aufruf):
        pass

    def on_key_press(self, key, modifiers):
        self.bei_tastendruck(key, modifiers)

    def bei_tastendruck(self, welche_taste, taste_modifikator):
        pass

    def on_key_release(self, key, modifiers):
        self.bei_taste_loslassen(key, modifiers)

    def bei_taste_loslassen(self, welche_taste, taste_modifikator):
        pass
