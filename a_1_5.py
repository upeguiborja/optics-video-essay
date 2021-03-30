from manim import *
import numpy as np


class Intro(Scene):

  def construct(self):
    question = Text(
        r'''A1.5 Explique por qué la luz azul del firmamento diurno de verano (con
    escasas nubes) tiene ese color y está parcialmente polarizada, mientras
    que la luz que proviene de las pocas nubes es blanca y no-polarizada.
    como se indica en la figura A1.5''')
    question.scale(0.5)

    self.play(Write(question, run_time=5))
    self.wait()