from manim import *
import numpy as np


class Intro(Scene):

  def construct(self):
    question = Text(
        r'''2. Explicar las leyes de reflexión y refracción desde las perspectivas
    de las ondas electromagnéticas. A partir de la ley de refracción,
    discutir la dispersión de la luz en un prisma''')

    question.scale(0.5)
    self.play(Write(question, run_time=5))


class OpticalPrism(Scene):

  def construct(self):
    theta = ValueTracker(10 * DEGREES)
    prism = Triangle(
        fill_opacity=0.25,
        color="WHITE",
    )
    prism.move_to(ORIGIN)
    prism.scale(3)
    vertices = prism.get_vertices()

    center = midpoint(vertices[0], vertices[1])

    self.play(Write(prism))

    incident_ray = Line(
        start=(-10, -2, 0),
        end=center,
        stroke_width=5,
    )

    self.play(Write(incident_ray))
    self.wait()