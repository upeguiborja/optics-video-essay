from manim import *
import numpy as np


class Q1Intro(Scene):

  def construct(self):
    question = Text(
        r'''1. Explicar el significado físico de los coeficientes de Fresnel para interfaces
  entre medios dieléctricos. Ilustrarlos considerando las interfaces
  aire (n=1.0) - vidrio (n=1.5) y vidrio - aire''')
    question.scale(0.5)
    self.play(Write(question, run_time=5))


class Q2Intro(Q1Intro):
  question = Text(
      r'''2. Explicar las leyes de reflexión y refracción desde las perspectivas
  de las ondas electromagnéticas. A partir de la ley de refracción,
  discutir la dispersión de la luz en un prisma''')


class Q3Intro(Q1Intro):
  question = Text(
      r'''3. La siguiente figura muestra un montaje experimental de tres polarizadores
  lineales. Los ejes de transmisión del polarizador cercano a la vela y del analizador
  son mutualmente ortogonales. mientras que el del polarizador del medio
  hace 45º con el del polarizador cercano a la vela.''')


AXES_CONFIG = {
    "z_min": -5,
    "z_max": 5,
    "x_min": -10,
    "x_max": 10,
    "y_min": -10,
    "y_max": 10
}


class Fresnel(ThreeDScene):

  def construct(self):
    self.set_camera_orientation(
        phi=75 * DEGREES,
        theta=10 * DEGREES,
    )

    axes = ThreeDAxes(**AXES_CONFIG)
    prism = Prism(dimensions=[2, 10, 2])
    prism.set_opacity(0.5)
    prism.move_to(np.array([0, 0, -1]))

    self.play(
        FadeIn(axes, run_time=2),
        Write(prism, run_time=2),
    )

    self.wait(0)

    incident_ray = Line(
        start=np.array([0, -10, 10]),
        end=ORIGIN,
        color=RED,
    )

    transmitted_ray = Line(
        start=ORIGIN,
        end=np.array([0, 10 * np.sin(0.490883), -10 * np.cos(0.490883)]),
        color=GREEN,
    )

    reflected_ray = Line(
        start=ORIGIN,
        end=np.array([0, 10, 10]),
        color=BLUE,
    )

    self.play(FadeIn(incident_ray, run_time=2))
    self.play(
        FadeIn(transmitted_ray, run_time=2),
        FadeIn(reflected_ray, run_time=2),
    )
    self.wait()


class Polarized(ThreeDScene):

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

    e_field = ParametricFunction(
        lambda t: np.array([0, t, np.sin(3 * t)]),
        t_min=-PI,
        t_max=0,
        color=YELLOW,
    )

    axes = ThreeDAxes()

    self.play(
        Write(polarizer_1, run_time=2),
        Write(polarizer_2, run_time=2),
        Write(polarizer_3, run_time=2),
        FadeIn(axes, run_time=2),
    )
    self.begin_ambient_camera_rotation()
    self.add(e_field)
    self.wait(10)