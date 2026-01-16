"""
Solitaire Game
"""
import arcade

# Screen titles & size
SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE = 1024, 768, "Drag & Drop Cards"

class MyGame(arcade.Window):
    """
    Main application class.
    """
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background_color = arcade.color.AMAZON

    def setup(self):
        """
        Set up the game here. Call this function to restart the game.
        """
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        # Clear the screen
        self.clear()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """
        Called when a user releases a mouse button.
        """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """
        User moves mouse
        """
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()