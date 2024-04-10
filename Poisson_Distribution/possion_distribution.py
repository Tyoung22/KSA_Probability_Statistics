#%%manim -ql -v WARNING PoissonDistributionProofAndVisualization

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
        
        self.clear()
        self.wait()
        
 

        # Transition to Part 2
        transition_text = Text("Visualizing the distribution with varying λ values", font_size=32)
        self.play(Write(transition_text))
        self.wait(2)
        self.play(FadeOut(transition_text))
          
        # Part 2: Visualization of Poisson Distribution with Varying λ           
        axes = Axes(
            x_range=[0, 20],
            y_range=[0, 0.4, 0.05],
            x_axis_config={"numbers_to_include": np.arange(0, 21, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 0.41, 0.1)},
            tips=False,
        )
        labels = axes.get_axis_labels(x_label="k", y_label="P(X=k)")
        self.play(Create(axes), Write(labels),run_time=2)
        self.wait()
        
        
        P_XK = labels[1].copy()           
        lam = "\lambda";k = 'k'
        Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{lam} ")                               
                               ).arrange(RIGHT).to_edge(UP)
        poisson_function_text = MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{k}}}{{{k}!}}")
        VGroup(P_XK,poisson_function_text).arrange(RIGHT)
        P_XK_real = labels[1].copy()
        self.play(
            P_XK_real.animate.move_to(P_XK),
        )
        self.play(
            FadeIn(poisson_function_text)        
        )
        self.play(
            FadeIn(Lamda_mean),
            VGroup(
                P_XK_real,
            poisson_function_text
            ).animate.next_to(Lamda_mean,DOWN)
            
        )
        self.wait()
            
            

        #create bars_group
        lam = 1 ;mean_val = '?'
              

        
        new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{mean_val} ")                               
                               ).arrange(RIGHT).to_edge(UP)
        new_poisson_function_text =  MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{{{k}}}}}{{{k}!}}").next_to(P_XK_real,RIGHT)
        
        self.play(Transform(Lamda_mean, new_Lamda_mean))
        self.wait()     
        
        
        self.play(ApplyMethod(Lamda_mean[1].set_color, RED))
        self.wait()        
        self.play(ReplacementTransform(poisson_function_text, new_poisson_function_text))
        self.wait()
        
        poisson_function_text = new_poisson_function_text
        bars = []         
        for k in range(21):
            if k<6:run_time=1.5
            elif k<11:run_time=0.5
            else: run_time = 0.1
    
            new_poisson_function_text =  MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{{{k}}}}}{{{k}!}}").next_to(P_XK_real,RIGHT)
            p = ((lam**k) * np.exp(-lam)) / np.math.factorial(k)
            bar_height = 15 * p  # Adjusted for visualization scale
            bar = Rectangle(width=0.5, height=bar_height, fill_opacity=0.7, color=BLUE)
            bar.move_to(axes.c2p(k, 0) + UP * bar_height / 2)
            self.play(FadeIn(bar),
                     ReplacementTransform(poisson_function_text, new_poisson_function_text),run_time = run_time
                     )
            poisson_function_text = new_poisson_function_text
            bars.append(bar)
        bars_group = VGroup(*bars)       
        
        
        expected_line = DashedLine(
            start=axes.c2p(lam, 0),
            end=axes.c2p(lam, 0.3),
            color=YELLOW,
        )
        expeted_text = Text("Mean",font_size=24).next_to(expected_line,UP)
        mean_val= lam
        new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                        MathTex(fr"{lam} "),
                        MathTex(fr", \; Mean = "),
                        MathTex(fr"{mean_val} ")                               
                       ).arrange(RIGHT).to_edge(UP)
            
        self.wait()
        self.play(
            FadeIn(expected_line),
            FadeIn(expeted_text),
            Transform(Lamda_mean, new_Lamda_mean),           
            
        
         )

        
        self.wait(3)
        



        for lam in range(2, 6):

            mean_val = '?'
            new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{mean_val} ")                               
                               ).arrange(RIGHT).to_edge(UP)
            new_poisson_function_text = MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{{k}}}}{{k!}}").next_to(P_XK_real,RIGHT)
            
            
            bars = []
            for k in range(21):
                p = ((lam**k) * np.exp(-lam)) / np.math.factorial(k)
                bar_height = 15 * p  # Adjusted for visualization scale
                bar = Rectangle(width=0.5, height=bar_height, fill_opacity=0.7, color=BLUE)
                bar.move_to(axes.c2p(k, 0) + UP * bar_height / 2)
                bars.append(bar)
            new_bars_group = VGroup(*bars)
            
            


            self.play(ReplacementTransform(bars_group, new_bars_group),
                      ReplacementTransform(poisson_function_text, new_poisson_function_text),
                      Transform(Lamda_mean, new_Lamda_mean),
                      
                      FadeOut(expected_line),
                      FadeOut(expeted_text),  
                      run_time=1)
                    
            self.wait()
            
            mean_val = lam

            new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{mean_val} ")                               
                               ).arrange(RIGHT).to_edge(UP)
            expected_line = DashedLine(
            start=axes.c2p(lam, 0),
            end=axes.c2p(lam, 0.3),
            color=YELLOW,
        )
            expeted_text = Text("Mean",font_size=24).next_to(expected_line,UP)

            
            
            
            self.play(
                Transform(Lamda_mean, new_Lamda_mean),                     
                FadeIn(expected_line),
                     FadeIn(expeted_text),         
                      run_time=1)
            
            
            
            poisson_function_text = new_poisson_function_text 
            bars_group = new_bars_group  
      

            self.wait(1)
            
            
        for lam in range(6, 10):

            mean_val = lam
            new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{mean_val} ")                               
                               ).arrange(RIGHT).to_edge(UP)
            new_poisson_function_text = MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{{k}}}}{{k!}}").next_to(P_XK_real,RIGHT)
            
            
            bars = []
            for k in range(21):
                p = ((lam**k) * np.exp(-lam)) / np.math.factorial(k)
                bar_height = 15 * p  # Adjusted for visualization scale
                bar = Rectangle(width=0.5, height=bar_height, fill_opacity=0.7, color=BLUE)
                bar.move_to(axes.c2p(k, 0) + UP * bar_height / 2)
                bars.append(bar)
            new_bars_group = VGroup(*bars)
            
            next_expected_line = DashedLine(
            start=axes.c2p(lam, 0),
            end=axes.c2p(lam, 0.3),
            color=YELLOW,
                )
            next_expeted_text = Text("Mean",font_size=24).next_to(next_expected_line,UP)
            
            


            self.play(ReplacementTransform(bars_group, new_bars_group),
                      ReplacementTransform(poisson_function_text, new_poisson_function_text),
                      Transform(Lamda_mean, new_Lamda_mean),
                      
                      FadeOut(expected_line),
                      FadeOut(expeted_text),  
                      FadeIn(next_expected_line),
                      FadeIn(next_expeted_text),  
                      run_time=1)

            
            
            
            
            poisson_function_text = new_poisson_function_text 
            bars_group = new_bars_group  
            expected_line = next_expected_line
            expeted_text = next_expeted_text

            self.wait(1)
            
        self.clear()
        
        #Ending Credit
        self.wait()
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


#%%manim -ql -v WARNING PoissonDistributionProofAndVisualization

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
        
        self.clear()
        self.wait()
        
 

        # Transition to Part 2
        transition_text = Text("Visualizing the distribution with varying λ values", font_size=32)
        self.play(Write(transition_text))
        self.wait(2)
        self.play(FadeOut(transition_text))
          
        # Part 2: Visualization of Poisson Distribution with Varying λ           
        axes = Axes(
            x_range=[0, 20],
            y_range=[0, 0.4, 0.05],
            x_axis_config={"numbers_to_include": np.arange(0, 21, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 0.41, 0.1)},
            tips=False,
        )
        labels = axes.get_axis_labels(x_label="k", y_label="P(X=k)")
        self.play(Create(axes), Write(labels),run_time=2)
        self.wait()
        
        
        P_XK = labels[1].copy()           
        lam = "\lambda";k = 'k'
        Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{lam} ")                               
                               ).arrange(RIGHT).to_edge(UP)
        poisson_function_text = MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{k}}}{{{k}!}}")
        VGroup(P_XK,poisson_function_text).arrange(RIGHT)
        P_XK_real = labels[1].copy()
        self.play(
            P_XK_real.animate.move_to(P_XK),
        )
        self.play(
            FadeIn(poisson_function_text)        
        )
        self.play(
            FadeIn(Lamda_mean),
            VGroup(
                P_XK_real,
            poisson_function_text
            ).animate.next_to(Lamda_mean,DOWN)
            
        )
        self.wait()
            
            

        #create bars_group
        lam = 1 ;mean_val = '?'
              

        
        new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{mean_val} ")                               
                               ).arrange(RIGHT).to_edge(UP)
        new_poisson_function_text =  MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{{{k}}}}}{{{k}!}}").next_to(P_XK_real,RIGHT)
        
        self.play(Transform(Lamda_mean, new_Lamda_mean))
        self.wait()     
        
        
        self.play(ApplyMethod(Lamda_mean[1].set_color, RED))
        self.wait()        
        self.play(ReplacementTransform(poisson_function_text, new_poisson_function_text))
        self.wait()
        
        poisson_function_text = new_poisson_function_text
        bars = []         
        for k in range(21):
            if k<6:run_time=1.5
            elif k<11:run_time=0.5
            else: run_time = 0.1
    
            new_poisson_function_text =  MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{{{k}}}}}{{{k}!}}").next_to(P_XK_real,RIGHT)
            p = ((lam**k) * np.exp(-lam)) / np.math.factorial(k)
            bar_height = 15 * p  # Adjusted for visualization scale
            bar = Rectangle(width=0.5, height=bar_height, fill_opacity=0.7, color=BLUE)
            bar.move_to(axes.c2p(k, 0) + UP * bar_height / 2)
            self.play(FadeIn(bar),
                     ReplacementTransform(poisson_function_text, new_poisson_function_text),run_time = run_time
                     )
            poisson_function_text = new_poisson_function_text
            bars.append(bar)
        bars_group = VGroup(*bars)       
        
        
        expected_line = DashedLine(
            start=axes.c2p(lam, 0),
            end=axes.c2p(lam, 0.3),
            color=YELLOW,
        )
        expeted_text = Text("Mean",font_size=24).next_to(expected_line,UP)
        mean_val= lam
        new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                        MathTex(fr"{lam} "),
                        MathTex(fr", \; Mean = "),
                        MathTex(fr"{mean_val} ")                               
                       ).arrange(RIGHT).to_edge(UP)
            
        self.wait()
        self.play(
            FadeIn(expected_line),
            FadeIn(expeted_text),
            Transform(Lamda_mean, new_Lamda_mean),           
            
        
         )

        
        self.wait(3)
        



        for lam in range(2, 6):

            mean_val = '?'
            new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{mean_val} ")                               
                               ).arrange(RIGHT).to_edge(UP)
            new_poisson_function_text = MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{{k}}}}{{k!}}").next_to(P_XK_real,RIGHT)
            
            
            bars = []
            for k in range(21):
                p = ((lam**k) * np.exp(-lam)) / np.math.factorial(k)
                bar_height = 15 * p  # Adjusted for visualization scale
                bar = Rectangle(width=0.5, height=bar_height, fill_opacity=0.7, color=BLUE)
                bar.move_to(axes.c2p(k, 0) + UP * bar_height / 2)
                bars.append(bar)
            new_bars_group = VGroup(*bars)
            
            


            self.play(ReplacementTransform(bars_group, new_bars_group),
                      ReplacementTransform(poisson_function_text, new_poisson_function_text),
                      Transform(Lamda_mean, new_Lamda_mean),
                      
                      FadeOut(expected_line),
                      FadeOut(expeted_text),  
                      run_time=1)
                    
            self.wait()
            
            mean_val = lam

            new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{mean_val} ")                               
                               ).arrange(RIGHT).to_edge(UP)
            expected_line = DashedLine(
            start=axes.c2p(lam, 0),
            end=axes.c2p(lam, 0.3),
            color=YELLOW,
        )
            expeted_text = Text("Mean",font_size=24).next_to(expected_line,UP)

            
            
            
            self.play(
                Transform(Lamda_mean, new_Lamda_mean),                     
                FadeIn(expected_line),
                     FadeIn(expeted_text),         
                      run_time=1)
            
            
            
            poisson_function_text = new_poisson_function_text 
            bars_group = new_bars_group  
      

            self.wait(1)
            
            
        for lam in range(6, 10):

            mean_val = lam
            new_Lamda_mean = VGroup(MathTex(fr"\lambda =  "),
                                MathTex(fr"{lam} "),
                                MathTex(fr", \; Mean = "),
                                MathTex(fr"{mean_val} ")                               
                               ).arrange(RIGHT).to_edge(UP)
            new_poisson_function_text = MathTex(fr" = \frac{{e^{{-{lam}}} {lam}^{{k}}}}{{k!}}").next_to(P_XK_real,RIGHT)
            
            
            bars = []
            for k in range(21):
                p = ((lam**k) * np.exp(-lam)) / np.math.factorial(k)
                bar_height = 15 * p  # Adjusted for visualization scale
                bar = Rectangle(width=0.5, height=bar_height, fill_opacity=0.7, color=BLUE)
                bar.move_to(axes.c2p(k, 0) + UP * bar_height / 2)
                bars.append(bar)
            new_bars_group = VGroup(*bars)
            
            next_expected_line = DashedLine(
            start=axes.c2p(lam, 0),
            end=axes.c2p(lam, 0.3),
            color=YELLOW,
                )
            next_expeted_text = Text("Mean",font_size=24).next_to(next_expected_line,UP)
            
            


            self.play(ReplacementTransform(bars_group, new_bars_group),
                      ReplacementTransform(poisson_function_text, new_poisson_function_text),
                      Transform(Lamda_mean, new_Lamda_mean),
                      
                      FadeOut(expected_line),
                      FadeOut(expeted_text),  
                      FadeIn(next_expected_line),
                      FadeIn(next_expeted_text),  
                      run_time=1)

            
            
            
            
            poisson_function_text = new_poisson_function_text 
            bars_group = new_bars_group  
            expected_line = next_expected_line
            expeted_text = next_expeted_text

            self.wait(1)
            
        self.clear()
        
        #Ending Credit
        self.wait()
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

