import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Arcade?"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    arcade.set_background_color(arcade.color.SKY_BLUE)

    arcade.start_render()

    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3.5, arcade.color.DARK_GREEN)

    arcade.draw_circle_filled(200, 230, 10, arcade.color.BONE)
    arcade.draw_lrbt_rectangle_filled(190, 210, SCREEN_HEIGHT / 3.5, 220, arcade.color.RUBY_RED)
    arcade.draw_lrbt_rectangle_filled(210, 235, 200, 210, arcade.color.RUBY_RED)
    arcade.draw_lrbt_rectangle_filled(170, 190, 200, 210, arcade.color.DARK_RED)

    arcade.draw_line(210, 235, 180, 205, arcade.color.WHITE, 5)
    arcade.draw_line(210, 175, 180, 205, arcade.color.WHITE, 5)
    arcade.draw_arc_outline(210, 205, 50, 60, arcade.color.DARK_BROWN,
                            270, 450, 10)

    arcade.draw_triangle_filled(238, 210, 238, 200, 250, 205, arcade.color.WHITE)
    arcade.draw_line(238, 205, 180, 205, arcade.color.WOOD_BROWN, 3)
    arcade.draw_triangle_filled(458, 210, 458, 200, 470, 205, arcade.color.WHITE)
    arcade.draw_line(458, 205, 410, 205, arcade.color.WOOD_BROWN, 3)

    arcade.draw_circle_filled(600, 230, 10, arcade.color.BONE)
    arcade.draw_lrbt_rectangle_filled(590, 610, SCREEN_HEIGHT / 3.5, 220, arcade.color.PURPLE)
    arcade.draw_lrbt_rectangle_filled(575, 590, 200, 210, arcade.color.PURPLE)
    arcade.draw_line(608, 207, 630, 190, arcade.color.PURPLE, 9)

    arcade.draw_ellipse_filled(575, 205, 20, 50, arcade.color.SILVER_PINK)


    arcade.finish_render()
    arcade.run()


def on_draw():
    arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))


main()
