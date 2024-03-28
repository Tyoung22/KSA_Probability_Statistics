%%manim -qh -v WARNING Part0_Introduction

class Part0_Introduction(Scene):
    def construct(self):

#         Part 0: Introduction
        title = Text("Poisson Distribution: Expectation Proof", font_size=36)
        creator_name = Text("Made by Kim DoYoung", font_size=24).shift(DOWN * 1)       
        self.play(Write(title),
                 Write(creator_name))
        self.wait(2)
        self.play(FadeOut(title),
                 FadeOut(creator_name))
    
        common_text = Text("of Poisson Distribution").to_edge(UP)
        self.add(common_text)
        PMF_part = Text("PMF ", color=BLUE)
        Expect_part = Text("Expectation ", color=BLUE)


        First_text = VGroup(PMF_part, common_text).arrange(RIGHT,aligned_edge=DOWN)
        
        self.play(FadeIn(First_text))
        self.wait()
        
        self.play(First_text.animate.to_edge(UP))
        
        PMF_form = VGroup(MathTex(r"P(X = k) "),
                         MathTex(r"="),
                         MathTex(r"\frac{e^{-\lambda} \lambda^k}{k!}")).arrange(RIGHT)
        eq00 = VGroup(MathTex(r"E(X) = \sum_{k=0}^{\infty} k \cdot "),
                     MathTex(r"P(X = k)").next_to(PMF_form, UP)).arrange(RIGHT).next_to(First_text,DOWN*1.5)
        
        self.play(FadeIn(PMF_form))
                      
        self.wait(1)

        Second_text = VGroup(Expect_part, common_text.copy()).arrange(RIGHT,aligned_edge=DOWN).to_edge(UP)

        self.play(
            Transform(PMF_part, Expect_part),
            common_text.animate.next_to(Expect_part, RIGHT, buff=0.2),
            FadeIn(eq00)
            
        )
        
        box1 = SurroundingRectangle(eq00[1], buff=0.1)
        box2 = SurroundingRectangle(PMF_form[0], buff=0.1)
        self.wait()
        self.play(Create(box1),
                  Create(box2)
                 )
        self.wait()
        
        copy_PMF_form = PMF_form[0].copy()
        self.play(Transform(box2, box1),
                  Transform(copy_PMF_form, eq00[1]))
#                  copy_PMF_form.animate.move_to(eq00[1]))
        self.wait()
        

        

        self.play(
            PMF_form[2].animate.move_to(eq00[1]),
            FadeOut(eq00[1]),
            FadeOut(PMF_form[0]), 
            FadeOut(copy_PMF_form),
            FadeOut(PMF_form[1]),
            FadeOut(box1),
            FadeOut(box2)
            
        )
        
        
                      
        self.wait()
        eq01 = MathTex(r"=e^{-\lambda} \lambda \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}")
        eq02 = MathTex(r"=e^{-\lambda} \lambda e^{\lambda} \; ( \because \text{Taylor series} ) ")
        eq03 = MathTex(r"= \lambda")
        VGroup(eq01,eq02,eq03).arrange(DOWN,aligned_edge=LEFT).next_to(eq00,DOWN)
        self.play(LaggedStart(Write(eq01), Write(eq02),Write(eq03), lag_ratio=1))
        
        self.wait(3)



       


        
        

