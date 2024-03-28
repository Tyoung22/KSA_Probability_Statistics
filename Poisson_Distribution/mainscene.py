# %%manim -ql -v WARNING PoissonDistributionProofAndVisualization


from manim import *
import numpy as np

config.media_width = "75%"

class PoissonDistributionProofAndVisualization(Scene):
    def construct(self):

        # Part 0: Introduction
        title = Text("Poisson Distribution: Expectation Proof", font_size=36)
        creator_name = Text("Made by Kim DoYoung", font_size=24).shift(DOWN * 1)       
        self.play(Write(title),
                 Write(creator_name))
        self.wait(2)
        self.play(FadeOut(title),
                 FadeOut(creator_name))

        #Part 1: Proof of Expectation
        #         Part 0: Introduction
        
 

        # Transition to Part 2
        transition_text = Text("Visualizing the distribution with varying λ values", font_size=32)
        self.play(Write(transition_text))
        self.wait(2)
        self.play(FadeOut(transition_text))

        # Part 2: Visualization of Poisson Distribution with Varying λ           
     
         
        
        #Ending Credit
        Ending_text = Text("KSA Probability and Statistics EC2").to_edge(UP,buff=1)
        Ending_text2 = Text("Thanks for watching",font_size=80).next_to(Ending_text,DOWN*10)
        Ending_text3 = Text("By 22-010 Kim Doyoung", font_size=32).next_to(Ending_text2,DOWN)
        
        
        self.play(
            Write(Ending_text)                 
                 )
        self.play(
            FadeIn(Ending_text2),
            FadeIn(Ending_text3)
        )

        

        self.wait(2)

