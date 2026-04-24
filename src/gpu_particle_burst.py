from array import array
from dataclasses import dataclass

import random, time, math
import arcade, arcade.gl

SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE = 1024, 768, "GPU Particle Explosiion"

PARTICLE_COUNT, MIN_FADE_TIME, MAX_FADE_TIME = 300, 0.25, 1.5

@dataclass
class Burst:
    """ Track for each burst. """
    buffer: arcade.gl.Buffer
    vao: arcade.gl.geometry
    start_time: float

class MyWindow(arcade.Window):
    """ Main Window """
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.burst_list = []

        # Program to visualize the points
        self.program = self.ctx.load_program(
            vertex_shader="vertex_shader_v1.glsl",
            fragment_shader="fragment_shader_v1.glsl",
        )

        self.ctx.enable_only(self.ctx.BLEND)

    def on_draw(self):
        """ Draw everything """
        self.clear()

        # Set the particle size
        self.ctx.point_size = 2 * self.get_pixel_ratio()

        # Loop through each burst
        for burst in self.burst_list:
            # Set the uniform data
            self.program['time'] = time.time() - burst.start_time

            # Render the burst
            burst.vao.render(self.program, mode=self.ctx.POINTS)

    def on_update(self, dt):
        """ Update everything """
        # Create a copy of our list, as we can't modify a list while iterating
        # it. Then see if any of the items have completely faded out and need
        # to be removed.
        temp_list = self.burst_list.copy()
        for burst in temp_list:
            if time.time() - burst.start_time > MAX_FADE_TIME:
                self.burst_list.remove(burst)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """ User clicks mouse """
        def _gen_initial_data(initial_x, initial_y):
            """ Generate data for each particle """
            for i in range(PARTICLE_COUNT):
                angle = random.uniform(0, 2 * math.pi)
                speed = abs(random.gauss(0, 1)) * .5

                dx = math.sin(angle) * speed
                dy = math.cos(angle) * speed

                red = random.uniform(0.5, 1.0)
                green = random.uniform(0, red)
                blue = 0

                fade_rate = random.uniform(
                    1 / MAX_FADE_TIME, 1 / MIN_FADE_TIME
                )

                yield initial_x, initial_y
                yield dx, dy
                yield red, green, blue
                yield fade_rate

        # Recalaculate the coordinates from pixels to the OpenGL system with
        # 0, 0 at the center.
        x2 = x / self.width * 2. - 1.
        y2 = y / self.height * 2. - 1.

        # Get initial particle data
        initial_data = _gen_initial_data(x2, y2)

        # Create a buffer with that data
        buffer = self.ctx.buffer(data=array('f', initial_data))

        # Create a buffer description specifying the buffer's data format
        buffer_description = arcade.gl.BufferDescription(
            buffer,
            '2f 2f 3f f',
            ['in_pos', 'in_vel', 'in_color', 'in_fade_rate']
        )

        # Create our Vertex Attribute Object
        vao = self.ctx.geometry([buffer_description])

        # Create teh Burst object & add it to the list of bursts
        burst = Burst(buffer=buffer, vao=vao, start_time=time.time())
        self.burst_list.append(burst)

if __name__ == "__main__":
    window = MyWindow()
    window.center_window()
    arcade.run()