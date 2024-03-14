import pygame as pg
from pygame.sprite import Group
from Settings import Settings
from Button import Button
from Game_Stats import GameStats
from Scoreboard import Scoreboard
from Ship import Ship
import game_functions as gf


def run_game(): 
    pg.init()
    gc_settings = Settings() 
    screen = pg.display.set_mode((gc_settings.screen_width, gc_settings.screen_height))
    pg.display.set_caption("Galaga Clone")
    play_button = Button(gc_settings, screen, "Play")

    stats = GameStats(gc_settings) 
    sb = Scoreboard(gc_settings, screen, stats)
    ship = Ship(gc_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(gc_settings, screen, ship, aliens)

    while True:
        gf.check_events(gc_settings,screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(gc_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(gc_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(gc_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        pg.display.flip()

run_game()