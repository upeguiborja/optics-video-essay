from manimlib import *
import numpy as np


class Q1Intro(Scene):
  question = Text(
      r'''1. Explicar el significado físico de los coeficientes de Fresnel para interfaces
  entre medios dieléctricos. Ilustrarlos considerando las interfaces
  aire (n=1.0) - vidrio (n=1.5) y vidrio - aire''')

  def construct(self):
    self.question.scale(0.5)
    self.play(Write(self.question, run_time=5))


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


class Snell(Scene):

  def construct(self):
    self.camera.frame.set_euler_angles(phi=75 * DEGREES, theta=45 * DEGREES)
    axes = ThreeDAxes(**AXES_CONFIG)
    prism = Prism(dimensions=[3, 2, 1])
    prism.set_opacity(0.3)
    prism.move_to([0, 0, 0])

    self.add(axes)
    self.add(prism)
    self.wait()
