"""
SuperChareleyyyGalaxy Plaformer Game

Author: Ryan Setaruddin
Date: 2025-12-05
Description: A 2D platformer game where players navigate through various levels, overcoming obstacles and enemies to reach the final goal.
"""
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "SuperChareleyyyGalaxy"

class GameView(arcade.Window):
    """ Main Appliaction class. """
    def __init__(self):
        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def on_draw(self):
        """ Render the screen """
        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()
        
        # Draw game elements here

def main():
    """ Main function """
    window = GameView()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()