"""
Show how to use lights.

.. note:: This uses features from the upcoming version 2.4. The API for these
        functions may still change. To use, you will need to install one of the
        pre-release packages, or install via GitHub.

Artwork from http://kenney.nl
"""

import arcade
from arcade.future.light import Light, LightLayer

SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE = 1024, 768, "Light Demo"
VIEWPORT_MARGIN, MOVEMENT_SPEED = 200, 5

# This is teh color used for 'ambient light'. If you don't want any
# ambient light, set this to black
AMBIENT_COLOR = (10, 10, 10)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Main Game window """
        def __init__(self, width, height, title):
            """ Initialize the game window. """
            super().__init__(width, height, title, resizable=True)

            # Sprite lists
            self.background_sprite_list = None
            self.player_list = None
            self.wall_list = None
            self.player_sprite = None

            # physics engine
            self.physics_engine = None

            # camera for scrooling
            self.camera = None

            # --- Light related ---
            # List of all the lights
            self.light_layer = None

            # Individual light we move with player, adn turn on/off
            self.player_light = None

        def setup(self):
            """ Create everything """

            # Create sprite lists
            self.background_sprite_list = arcade.SpriteList()
            self.player_list = arcade.SpriteList()
            self.wall_list = arcade.SpriteList()

            # Create player sprite
            self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.4)
            self.player_sprite.center_x = 64
            self.player_sprite.center_y = 270
            self.player_list.append(self.player_sprite)

            # --- Light related ---

        def on_draw(self):
            pass

        def on_resize(self, width, height):
            pass

        def on_key_press(self, key, _):
            pass

        def on_key_release(self, key, _):
            pass

        def scrool_screen(self):
            pass

        def update(self, delta_time):
            pass

if __name__ == "__main__":
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()