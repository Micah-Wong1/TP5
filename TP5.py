import arcade
import random

""" 
Nom: Micah Wong
Gr: 406
Ce code dessine un archer tirant une flèche sur une autre personne à une personne armée d'une épée et d'un bouclier
dans la nuit
"""

screen_width = 800
screen_height = 600
star = 25
window_title = "Arcade?"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)


def main():
    arcade.open_window(screen_width, screen_height, window_title)
    arcade.set_background_color(arcade.color.MIDNIGHT_BLUE)

    arcade.start_render()

    # BACKGROUND
    stars = []
    for i in range(star):
        x = random.randrange(screen_width)
        y = random.randrange(200, 555)
        stars.append((x, y))

    arcade.draw_points(stars, arcade.color.GOLD, 5)
    arcade.draw_lrbt_rectangle_filled(0, screen_width, 0, screen_height / 3.5, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(150, 500, 50, arcade.color.SILVER_LAKE_BLUE)
    arcade.draw_circle_filled(180, 500, 48, arcade.color.MIDNIGHT_BLUE)

    # Rouge personne
    arcade.draw_circle_filled(200, 230, 10, arcade.color.BONE)
    arcade.draw_lrbt_rectangle_filled(190, 210, screen_height / 3.5, 220, arcade.color.RUBY_RED)
    arcade.draw_lrbt_rectangle_filled(210, 235, 200, 210, arcade.color.RUBY_RED)
    arcade.draw_lrbt_rectangle_filled(170, 190, 200, 210, arcade.color.DARK_RED)

    # BOW
    arcade.draw_line(210, 235, 180, 205, arcade.color.WHITE, 5)
    arcade.draw_line(210, 175, 180, 205, arcade.color.WHITE, 5)
    arcade.draw_arc_outline(210, 205, 50, 60, arcade.color.DARK_BROWN,
                            270, 450, 10)

    # ARROWS
    arcade.draw_triangle_filled(238, 210, 238, 200, 250, 205, arcade.color.WHITE)
    arcade.draw_line(238, 205, 180, 205, arcade.color.WOOD_BROWN, 3)
    arcade.draw_triangle_filled(458, 210, 458, 200, 470, 205, arcade.color.WHITE)
    arcade.draw_triangle_filled(405, 213, 405, 198, 420, 205.5, arcade.color.GRAY)
    arcade.draw_line(458, 205, 410, 205, arcade.color.WOOD_BROWN, 3)
    arcade.draw_line(270, 205, 390, 205, arcade.color.WHITE_SMOKE, 1)
    arcade.draw_line(300, 200, 360, 200, arcade.color.WHITE_SMOKE, 1)

    # Mauve personne
    arcade.draw_circle_filled(600, 230, 10, arcade.color.BONE)
    arcade.draw_lrbt_rectangle_filled(590, 610, screen_height / 3.5, 220, arcade.color.PURPLE)
    arcade.draw_lrbt_rectangle_filled(575, 590, 200, 210, arcade.color.PURPLE)
    arcade.draw_line(608, 207, 630, 190, arcade.color.PURPLE, 9)

    # SHIELD + SWORD
    arcade.draw_ellipse_filled(575, 205, 20, 50, arcade.color.SILVER_PINK)
    arcade.draw_line(628, 183, 636, 196, arcade.color.GOLDEN_BROWN, 5)
    arcade.draw_line(630, 199, 640, 191, arcade.color.ROMAN_SILVER, 5)
    points = [(634, 199), (655, 235), (663, 240), (665, 230), (640, 194)]
    arcade.draw_polygon_filled(points, arcade.color.AERO_BLUE)

    # Text
    arrow_sound = arcade.Text("fwip!", 260, 215, arcade.color.WHITE_SMOKE, 10, italic=True)
    arrow_sound.draw()

    arcade.finish_render()
    arcade.run()


main()
