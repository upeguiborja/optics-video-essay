from manim import *
import numpy as np


class Intro(Scene):

  def construct(self):
    question = Text(
        r'''F1.2 Explicar las leyes de reflexión y refracción desde las perspectivas
    de las ondas electromagnéticas. A partir de la ley de refracción,
    discutir la dispersión de la luz en un prisma''')
    question.scale(0.5)

    self.play(Write(question, run_time=5))
    self.wait(5)


class OpticalPrism(Scene):

  def construct(self):
    prism = Triangle(
        fill_opacity=0.25,
        color="WHITE",
    )
    prism.move_to(ORIGIN)
    prism.scale(3)
    vertices = prism.get_vertices()

    center_1 = midpoint(vertices[0], vertices[1])

    self.play(Write(prism))
    self.wait(3)

    incident_ray = Line(
        start=(-10, -2, 0),
        end=center_1,
        stroke_width=5,
    )

    #Incident
    self.play(Write(incident_ray))
    self.wait(13)

    #Refraction Index
    refraction_index = MathTex("n = {c \\over v}")
    refraction_index.to_corner(UL)
    self.play(Write(refraction_index))

    #Snell Law
    snell_law = MathTex("n_I\\sin\\theta_I = n_T\\sin\\theta_T")
    snell_law.to_corner(UL)
    snell_law.shift(DOWN * 1.5)
    self.play(Write(snell_law))

    #Snell Law Mod
    snell_law_theta = MathTex(
        "\\theta_T = \\arcsin\\left(\\frac{n_I\\sin\\theta_I}{n_T}\\right)")
    snell_law_theta.to_corner(UL)
    snell_law_theta.shift(DOWN * 1.5)
    self.play(Transform(snell_law, snell_law_theta))
    self.wait(10)

    center_2 = midpoint(vertices[0], vertices[2])

    grow = midpoint(vertices[0], vertices[2]) - vertices[0]
    diff_ray_1 = Line(
        start=center_1,
        end=center_2,
        stroke_width=5,
        color=RED,
    )

    diff_ray_2 = Line(
        start=center_1,
        end=diff_ray_1.end + grow * 0.1,
        stroke_width=5,
        color=YELLOW,
    )

    diff_ray_3 = Line(
        start=center_1,
        end=diff_ray_1.end + grow * 0.2,
        stroke_width=5,
        color=GREEN,
    )

    diff_ray_4 = Line(
        start=center_1,
        end=diff_ray_1.end + grow * 0.3,
        stroke_width=5,
        color=BLUE_C,
    )

    diff_ray_5 = Line(
        start=center_1,
        end=diff_ray_1.end + grow * 0.4,
        stroke_width=5,
        color=BLUE_E,
    )

    diff_ray_6 = Line(
        start=center_1,
        end=diff_ray_1.end + grow * 0.5,
        stroke_width=5,
        color=PURPLE,
    )

    self.play(
        Write(diff_ray_1),
        Write(diff_ray_2),
        Write(diff_ray_3),
        Write(diff_ray_4),
        Write(diff_ray_5),
        Write(diff_ray_6),
    )
    self.wait(5)

    end_ray_1 = Line(
        start=diff_ray_1.end,
        end=(10, -2, 0),
        stroke_width=5,
        color=RED,
    )

    end_ray_2 = Line(
        start=diff_ray_2.end,
        end=end_ray_1.end + DOWN * 0.5,
        stroke_width=5,
        color=YELLOW,
    )

    end_ray_3 = Line(
        start=diff_ray_3.end,
        end=end_ray_1.end + DOWN * 1,
        stroke_width=5,
        color=GREEN,
    )

    end_ray_4 = Line(
        start=diff_ray_4.end,
        end=end_ray_1.end + DOWN * 1.5,
        stroke_width=5,
        color=BLUE_C,
    )

    end_ray_5 = Line(
        start=diff_ray_5.end,
        end=end_ray_1.end + DOWN * 2,
        stroke_width=5,
        color=BLUE_E,
    )

    end_ray_6 = Line(
        start=diff_ray_6.end,
        end=end_ray_1.end + DOWN * 2.5,
        stroke_width=5,
        color=PURPLE,
    )

    self.play(
        Write(end_ray_1),
        Write(end_ray_2),
        Write(end_ray_3),
        Write(end_ray_4),
        Write(end_ray_5),
        Write(end_ray_6),
    )
    self.wait(5)
