from manim import *
import numpy as np


class Intro(Scene):

  def construct(self):
    question = Text(
        r'''3. La siguiente figura muestra un montaje experimental de tres polarizadores
    lineales. Los ejes de transmisión del polarizador cercano a la vela y del analizador
    son mutualmente ortogonales. mientras que el del polarizador del medio
    hace 45º con el del polarizador cercano a la vela.''')
    question.scale(0.5)

    self.play(Write(question))
    self.wait()


class Polarizer(ThreeDScene):

  def construct(self):
    self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
    polarizer_body = Square(fill_opacity=0.25, color=BLUE)

    polarizer_arrow = Line(start=np.array([0, 0, 0]),
                           end=np.array([0, 1, 0]),
                           stroke_color=RED)

    polarizer_1 = VGroup(polarizer_body, polarizer_arrow)
    polarizer_1.rotate(90 * DEGREES, axis=X_AXIS)
    polarizer_1.move_to(np.array([0, PI, 0]))

    polarizer_2 = polarizer_1.copy()
    polarizer_2.move_to(np.array([0, 0, 0]))
    polarizer_2.rotate(45 * DEGREES, axis=Y_AXIS)
    polarizer_2[1].set_stroke(color=BLUE)

    polarizer_3 = polarizer_1.copy()
    polarizer_3.move_to(np.array([0, -PI, 0]))
    polarizer_3.rotate(90 * DEGREES, axis=Y_AXIS)

    e_unpolarized = Cylinder(height=PI,
                             direction=(0, 1, 0),
                             fill_color=YELLOW,
                             fill_opacity=0.5)

    e_field = ParametricFunction(
        lambda t: np.array([0, t, np.sin(3 * t)]),
        t_min=-PI,
        t_max=0,
        color=YELLOW,
    )

    axes = ThreeDAxes()

    # self.play(
    #     Write(polarizer_1, run_time=2),
    #     Write(polarizer_2, run_time=2),
    #     Write(polarizer_3, run_time=2),
    #     FadeIn(axes, run_time=2),
    # )
    # self.begin_ambient_camera_rotation()
    self.add(e_unpolarized, polarizer_1, polarizer_2, polarizer_3, axes)
    self.wait(10)