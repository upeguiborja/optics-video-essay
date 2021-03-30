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


class IntroA(Scene):

  def construct(self):
    question = Text(
        r'''a. Si la irradiancia de la vela es I0 ¿Qué tan brillante es la llama de la
    imagen de la vela en el plano de observacion en comparación con la de la vela misma?'''
    )
    question.scale(0.5)

    self.play(Write(question))
    self.wait()


class IntroB(Scene):

  def construct(self):
    question = Text(
        r'''b. ¿Cuanto debe girarse el analizador para eliminar la image de la vela?
    Una vez hecho el giro ¿qué ángulo hacen los ejes de transmisión del polarizador
    cercano a la vela y del analizador?''')
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
    polarizer_3[1].set_stroke(color=GREEN)

    e_unpolarized_1 = ParametricFunction(
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
    # self.begin_ambient_camera_rotation()
    self.wait()

    e_unpolarized_1.shift(UP * PI * 2)
    e_unpolarized_1.set_opacity(0.2)
    e_unpolarized_2 = e_unpolarized_1.copy()
    e_unpolarized_2.rotate(90 * DEGREES, axis=Y_AXIS)

    e_unpolarized_label = MathTex("I_0")
    e_unpolarized_label.set_color(YELLOW)
    e_unpolarized_label.to_corner(UL)
    self.add_fixed_in_frame_mobjects(e_unpolarized_label)

    self.play(
        Write(e_unpolarized_1),
        Write(e_unpolarized_2),
        Write(e_unpolarized_label),
    )
    self.wait()

    malus_law = MathTex("I_i = I_{i-1}\\cos^{2}\\theta")
    malus_law.to_corner(DR)
    self.add_fixed_in_frame_mobjects(malus_law)

    self.play(Write(malus_law))
    self.wait()

    e_polarized_1 = e_unpolarized_1.copy()
    e_polarized_1.shift(DOWN * PI)
    e_polarized_1.set_color(RED)

    e_polarized_1_label = MathTex("I_1", "=", "{{I_0}", "\\over{2}}")
    e_polarized_1_label.set_color_by_tex_to_color_map({
        "I_0": YELLOW,
        "I_1": RED,
    })
    e_polarized_1_label.to_corner(UL)
    e_polarized_1_label.shift(DOWN * 1.5)
    self.add_fixed_in_frame_mobjects(e_polarized_1_label)

    self.play(
        Write(e_polarized_1),
        Write(e_polarized_1_label),
    )
    self.wait()

    e_polarized_2 = e_polarized_1.copy()
    e_polarized_2.shift(DOWN * PI)
    e_polarized_2.rotate(45 * DEGREES, axis=Y_AXIS)
    e_polarized_2.set_color(BLUE)

    e_polarized_2_label = MathTex("I_2", "=", "{{I_0}", "\\over{4}}")
    e_polarized_2_label.set_color_by_tex_to_color_map({
        "I_0": YELLOW,
        "I_1": RED,
        "I_2": BLUE,
    })
    e_polarized_2_label.to_corner(UL)
    e_polarized_2_label.shift(DOWN * 3)
    self.add_fixed_in_frame_mobjects(e_polarized_2_label)

    self.play(
        Write(e_polarized_2),
        Write(e_polarized_2_label),
    )
    self.wait()

    e_polarized_3 = e_polarized_2.copy()
    e_polarized_3.shift(DOWN * PI)
    e_polarized_3.rotate(-135 * DEGREES, axis=Y_AXIS)
    e_polarized_3.set_color(GREEN)

    e_polarized_3_label = MathTex("I_3", "=", "{{I_0}", "\\over{8}}")
    e_polarized_3_label.set_color_by_tex_to_color_map({
        "I_0": YELLOW,
        "I_1": RED,
        "I_2": BLUE,
        "I_3": GREEN
    })
    e_polarized_3_label.to_corner(UL)
    e_polarized_3_label.shift(DOWN * 4.5)
    self.add_fixed_in_frame_mobjects(e_polarized_3_label)

    self.play(
        Write(e_polarized_3),
        Write(e_polarized_3_label),
    )
    self.wait()
