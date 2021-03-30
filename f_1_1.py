from manim import *
import numpy as np

AXES_CONFIG = {
    "z_min": -5,
    "z_max": 5,
    "x_min": -10,
    "x_max": 10,
    "y_min": -10,
    "y_max": 10
}


class Intro(Scene):

  def construct(self):
    question = Text(
        r'''F1.1 Explicar el significado físico de los coeficientes de Fresnel para interfaces
    entre medios dieléctricos. Ilustrarlos considerando las interfaces
    aire (n=1.0) - vidrio (n=1.5) y vidrio - aire''')
    question.scale(0.5)

    self.play(Write(question, run_time=5))
    self.wait(5)


class Fresnel(Scene):

  def construct(self):
    normal = DashedLine(
        start=(0, -10, 0),
        end=(0, 10, 0),
        stroke_width=2,
    )

    glass = Rectangle(
        fill_opacity=0.15,
        stroke_opacity=0,
        height=10,
        width=40,
    )
    glass.shift(DOWN * 5)

    theta = ValueTracker(135 * DEGREES)

    line_i = Line(start=ORIGIN,
                  end=(0, 10, 0),
                  stroke_opacity=0.5,
                  color=YELLOW,
                  stroke_width=2)
    line_i.set_angle(theta.get_value())

    line_r = Line(start=ORIGIN,
                  end=(0, 10, 0),
                  stroke_opacity=0.5,
                  color=YELLOW,
                  stroke_width=2)
    line_r.set_angle(180 * DEGREES - theta.get_value())

    line_t = Line(start=ORIGIN,
                  end=(0, 10, 0),
                  stroke_opacity=0.5,
                  color=YELLOW,
                  stroke_width=2)
    line_t.set_angle(270 * DEGREES +
                     np.arcsin(1 / 1.5 * np.sin(theta.get_value())))

    arc_i = Arc(radius=1,
                start_angle=90 * DEGREES,
                angle=line_i.get_angle() - 90 * DEGREES,
                stroke_width=2,
                arc_center=ORIGIN)

    arc_r = Arc(radius=1,
                start_angle=90 * DEGREES,
                angle=line_r.get_angle() - 90 * DEGREES,
                stroke_width=2,
                arc_center=ORIGIN)

    arc_t = Arc(radius=1,
                start_angle=270 * DEGREES,
                angle=line_t.get_angle() + 90 * DEGREES,
                stroke_width=2,
                arc_center=ORIGIN)

    arc_i_label = MathTex("\\theta_{I}")
    arc_r_label = MathTex("\\theta_{R}")
    arc_t_label = MathTex("\\theta_{T}")

    arc_i_label.move_to(arc_i)
    arc_i_label.shift((UP + LEFT) * 0.5)

    arc_r_label.move_to(arc_r)
    arc_r_label.shift((UP + RIGHT) * 0.5)

    arc_t_label.move_to(arc_t)
    arc_t_label.shift((DOWN + RIGHT) * 0.5)

    objects = [
        glass,
        normal,
        line_i,
        line_r,
        line_t,
    ]

    angles = [
        arc_i,
        arc_r,
        arc_t,
        arc_i_label,
        arc_r_label,
        arc_t_label,
    ]

    #Start
    for item in objects:
      self.add(item)

    self.wait(6)

    #Angles
    for item in angles:
      self.play(Write(item))

    self.wait(4)

    line_i.add_updater(lambda m: m.set_angle(theta.get_value()))
    line_r.add_updater(lambda m: m.set_angle(180 * DEGREES - theta.get_value()))
    line_t.add_updater(lambda m: m.set_angle(270 * DEGREES + np.arcsin(
        1 / 1.5 * np.sin(theta.get_value()))))
    arc_i.add_updater(lambda m: m.become(
        Arc(
            radius=1,
            start_angle=90 * DEGREES,
            angle=line_i.get_angle() - 90 * DEGREES,
            stroke_width=2,
            arc_center=ORIGIN,
        )))
    arc_r.add_updater(lambda m: m.become(
        Arc(
            radius=1,
            start_angle=90 * DEGREES,
            angle=line_r.get_angle() - 90 * DEGREES,
            stroke_width=2,
            arc_center=ORIGIN,
        )))
    arc_t.add_updater(lambda m: m.become(
        Arc(
            radius=1,
            start_angle=270 * DEGREES,
            angle=line_t.get_angle() + 90 * DEGREES,
            stroke_width=2,
            arc_center=ORIGIN,
        )))

    # Rotation
    self.play(theta.animate.set_value(95 * DEGREES))
    self.play(theta.animate.set_value(175 * DEGREES))
    self.play(theta.animate.set_value(135 * DEGREES))
    self.wait(5)

    k_i = Arrow(start=(-2, 2, 0), end=(-1, 1, 0), color=GREEN, buff=0)

    h_i = k_i.copy()
    h_i.set_color(BLUE)
    h_i.rotate(-90 * DEGREES, about_point=h_i.start)

    dot_i = Dot(point=k_i.start, color=RED)
    circle_i = Circle(color=RED, radius=0.25)
    circle_i.move_to(dot_i)
    e_i = VGroup(dot_i, circle_i)

    k_i_label = MathTex("k_{I}", color=GREEN)
    h_i_label = MathTex("H_{I\\perp}", color=BLUE)
    e_i_label = MathTex("E_{I\\perp}", color=RED)

    labels_i = VGroup(h_i_label, e_i_label, k_i_label)
    labels_i.arrange(UP)
    labels_i.to_corner(UL)

    em_i = VGroup(k_i, h_i, e_i)

    #Labels
    self.play(Write(k_i_label))
    self.wait(2)
    self.play(Write(e_i_label))
    self.wait(2)
    self.play(Write(h_i_label))
    self.wait(3)

    #Field
    self.play(Write(em_i))

    k_r = Arrow(start=(2, 2, 0), end=(3, 3, 0), color=GREEN, buff=0)

    h_r = k_r.copy()
    h_r.set_color(BLUE)
    h_r.rotate(-90 * DEGREES, about_point=h_r.start)

    dot_r = Dot(point=k_r.start, color=RED)
    circle_r = Circle(color=RED, radius=0.25)
    circle_r.move_to(dot_r)
    e_r = VGroup(dot_r, circle_r)

    k_r_label = MathTex("k_{R}", color=GREEN)
    h_r_label = MathTex("H_{R\\perp}", color=BLUE)
    e_r_label = MathTex("E_{R\\perp}", color=RED)

    labels_r = VGroup(h_r_label, e_r_label, k_r_label)
    labels_r.arrange(UP)
    labels_r.to_corner(UR)

    em_r = VGroup(k_r, h_r, e_r)

    k_t = Arrow(start=(1.33333413582, -2.4944378289, 0),
                end=(2.00000120373, -3.74165674335, 0),
                color=GREEN,
                buff=0)

    h_t = k_t.copy()
    h_t.set_color(BLUE)
    h_t.rotate(-90 * DEGREES, about_point=h_t.start)

    dot_t = Dot(point=k_t.start, color=RED)
    circle_t = Circle(color=RED, radius=0.25)
    circle_t.move_to(dot_t)
    e_t = VGroup(dot_t, circle_t)

    k_t_label = MathTex("k_{R}", color=GREEN)
    h_t_label = MathTex("H_{R\\perp}", color=BLUE)
    e_t_label = MathTex("E_{R\\perp}", color=RED)

    labels_t = VGroup(h_t_label, e_t_label, k_t_label)
    labels_t.arrange(UP)
    labels_t.to_corner(DR)

    em_t = VGroup(k_t, h_t, e_t)

    #Fields
    self.play(Write(em_r), Write(labels_r), Write(em_t), Write(labels_t))
    self.wait(40)

    boundary_1_part_1 = MathTex("E_{tan,1} = E_{tan,2}")
    boundary_2_part_1 = MathTex("H_{tan,1} = H_{tan,2}")

    boundary_1_part_1.to_corner(DL)
    boundary_1_part_1.shift(UP)
    boundary_2_part_1.to_corner(DL)

    #Boundary
    self.play(Write(boundary_1_part_1), Write(boundary_2_part_1))
    self.wait(18)

    boundary_1_part_2 = MathTex("E_{I\\perp} + E_{R\\perp} = E_{T\\perp}")
    boundary_1_part_2.to_corner(DL)
    boundary_1_part_2.shift(UP)

    #Boundary 2
    self.play(Transform(boundary_1_part_1, boundary_1_part_2))
    self.wait(2)

    boundary_2_part_2 = MathTex(
        "H_{I\\perp}\\cos{\\theta_{I}} - H_{R\\perp}\\cos{\\theta_{P} = H_{T\\perp}\\cos{\\theta_{T}"
    )
    boundary_2_part_2.to_corner(DL)

    #Boundary 3
    self.play(Transform(boundary_2_part_1, boundary_2_part_2))
    self.wait(2)


class FresnelEquationsPartOne(Scene):

  def construct(self):
    boundary_2_part_2 = MathTex(
        "H_{I\\perp}",
        "\\cos{\\theta_{I}} -",
        "H_{R\\perp}",
        "\\cos{\\theta_{P} =",
        "H_{T\\perp}",
        "\\cos{\\theta_{T}",
    )
    boundary_2_part_2.set_color_by_tex("H", BLUE)
    boundary_2_part_2.to_corner(UL)

    self.add(boundary_2_part_2)
    self.wait(5)

    electric_magnetic = MathTex("E", "= {\\eta \\over n}", "H")
    electric_magnetic.set_color_by_tex_to_color_map({"E": RED, "H": BLUE})
    electric_magnetic.to_corner(UR)

    self.play(Write(electric_magnetic))
    self.wait()

    boundary_2_part_3 = MathTex(
        "n_1\\cos{\\theta_{I}}(",
        "E_{I\\perp}",
        "-",
        "E_{R\\perp}",
        ") = n_2\\cos{\\theta_{T}}",
        "E_{T\\perp}",
    )
    boundary_2_part_3.set_color_by_tex("E", RED)
    boundary_2_part_3.to_corner(UL)
    boundary_2_part_3.shift(DOWN)

    self.play(Write(boundary_2_part_3))
    self.wait()

    boundary_1_part_2 = MathTex(
        "E_{I\\perp}",
        "+",
        "E_{R\\perp}",
        "=",
        "E_{T\\perp}",
    )
    boundary_1_part_2.set_color_by_tex("E", RED)
    boundary_1_part_2.to_corner(UL)
    boundary_1_part_2.shift(DOWN)

    self.play(
        Uncreate(boundary_2_part_2),
        boundary_2_part_3.animate.shift(UP),
    )
    self.play(Write(boundary_1_part_2))
    self.wait(5)

    r_s = MathTex(
        "r_{\\perp} = {{E_{R\\perp}} \\over {E_{I\\perp}}}",
        "= {{n_1\\cos{\\theta_{I}} - n_2\\cos{\\theta_{T}}} \\over",
        "{n_1\\cos{\\theta_{I}} + n_2\\cos{\\theta_{T}}}}",
    )
    r_s.shift(UP)

    t_s = MathTex(
        "t_{\\perp} = {{E_{T\\perp}} \\over {E_{I\\perp}}}",
        "= {{2n_1\\cos{\\theta_I}} \\over",
        "{n_1\\cos{\\theta_{I}} + n_2\\cos{\\theta_{T}}}}",
    )
    t_s.shift(DOWN)

    self.play(
        Uncreate(boundary_1_part_2),
        Uncreate(boundary_2_part_3),
        Uncreate(electric_magnetic),
    )
    self.play(
        Write(r_s),
        Write(t_s),
    )
    self.wait(3)


class FresnelEquationsPartTwo(Scene):

  def construct(self):
    r_s = MathTex(
        "{{E_{R\\perp}} \\over {E_{I\\perp}}}",
        "= {{n_1\\cos{\\theta_{I}} - n_2\\cos{\\theta_{T}}} \\over",
        "{n_1\\cos{\\theta_{I}} + n_2\\cos{\\theta_{T}}}}",
    )
    r_s.shift(UP)
    r_s.shift(LEFT * 3.5)

    t_s = MathTex(
        "{{{E_{T\\perp}} \\over {E_{I\\perp}}}",
        "= {{2n_1\\cos{\\theta_I}} \\over",
        "{n_1\\cos{\\theta_{I}} + n_2\\cos{\\theta_{T}}}}",
    )
    t_s.shift(DOWN)
    t_s.shift(LEFT * 3.5)

    r_p = MathTex(
        "{{E_{R\\parallel}} \\over {E_{I\\parallel}}}",
        "= {{n_2\\cos{\\theta_{I}} - n_1\\cos{\\theta_{T}}} \\over",
        "{n_2\\cos{\\theta_{I}} + n_1\\cos{\\theta_{T}}}}",
    )
    r_p.shift(UP)
    r_p.shift(RIGHT * 3.5)

    t_p = MathTex(
        "{{{E_{T\\parallel}} \\over {E_{I\\parallel}}}",
        "= {{2n_1\\cos{\\theta_I}} \\over",
        "{n_2\\cos{\\theta_{I}} + n_1\\cos{\\theta_{T}}}}",
    )
    t_p.shift(DOWN)
    t_p.shift(RIGHT * 3.5)

    self.wait(2)
    self.play(
        Write(r_s),
        Write(t_s),
        Write(r_p),
        Write(t_p),
    )
    self.wait(10)
