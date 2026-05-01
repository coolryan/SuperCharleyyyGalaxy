import arcade, arcade.gui

# screen title & size
SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE = 800, 600, "Making a Menu"

class MainView(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        switch_menu_button = arcade.gui.UIFlatButton(text="Pause", width=250)

        # Initialize the button with an on_click event.
        @switch_menu_button.event("on_click")
        def on_click_switch_button(switch):
            # Passing the main view into menu view as an argument
            menu_view = MainView(self)
            self.window.show_view(menu_view)

        # Use the anchor to position the button on the screen.
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=switch_menu_button,
        )

    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Enable the UIManager when the view is shown.
        self.manager.enable()

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()

        # Draw the manager
        self.manager.draw()

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    mainView = MainView()
    window.show_view(mainView)
    arcade.run()

if __name__ == "__main__":
    main()