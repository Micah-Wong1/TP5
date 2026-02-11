import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Arcade?"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    arcade.set_background_color(arcade.color.PALE_BLUE)

    arcade.start_render()
    arcade.finish_render()
    arcade.run()


def on_draw():
    arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))


main()
on_draw()
