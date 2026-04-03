"""
N-Body Gravity with Compute Shaders & Buffers
"""
import random, arcade
from array import array
from pathlib import Path
from typing import Generator, Tuple
from arcade.gl import BufferDescription

# Window dimensions in pixels
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

# Size of performance graphs in pixels
GRAPH_WIDTH, GRAPH_HEIGHT, GRAPH_MARGIN = 200, 120, 5

NUM_STARS: int = 4000
USE_COLORED_STARS: bool = True

def gen_initial_data (
    screen_size: Tuple[int, int],
    num_stars: int = NUM_STARS,
    use_color: bool = False
) -> array:
    """
    Generate an :py:class:`~array.array` of randomly positioned star data.
    Some of this data is wasted as padding because:

    1. GPUs expect SSBO data to be aligned to multiples of 4
    2. GLSL's vec3 is actually a vec4 with compiler-side restrictions,
        so we have to use 4-length vectors anyway.

    Args:
        screen_size: A (width, height) of the area to generate stars in
        num_stars: How many stars to generate
        use_color: Whether to generate white or randomized pastel stars
    
    Returns: An array of star position data
    """
    width, height = screen_size
    color_channel_min = 0.5 if use_color else 1.0

    def _data_generator() -> Generator[float, None, None]:
        """Inner generator function used to illustrate memory layout"""
        for i in range(num_stars):
            # Position/radius

            # Velocity (unused by visualization shaders)

            # Color
            pass

    # Use the generator function to fill an array in RAM
    return array('f', _data_generator())

class NBodyGravityWindow(arcade.Window):
    def __int__(self):
        # Ask for OpenGL context supporting version 4.3 or greater when
        # calling the parent initializer to make sure we have compute shader
        # support.
        super().__init__(
            WINDOW_WIDTH, WINDOW_HEIGHT,
            "N-Body Gravity with Compute Shaders & Buffers",
            gl_version=(4, 3),
            resizable=False
        )

    def on_draw(self):
        # Clear the screen
        self.clear()

# run the python program
if __name__ == "__main__":
    app = NBodyGravityWindow()
    arcade.run()