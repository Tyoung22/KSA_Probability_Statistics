%%manim -ql -v WARNING Part2_1
class Part2_1(Scene):
    def construct(self):

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
            run_time = 1.5 if k<6 else 0.5
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
        



        for lam in range(2, 10):

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
                      ReplacementTransform(Lamda_mean, new_Lamda_mean),
                      
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

            
            self.play(Transform(Lamda_mean, new_Lamda_mean),
                      FadeIn(expected_line),
                     FadeIn(expeted_text),         
                      run_time=1)
            
            
            
            poisson_function_text = new_poisson_function_text 
            bars_group = new_bars_group  
            new_expected_line = expected_line
            new_expeted_text = expeted_text

            self.wait(1)

       # Cleanup at the end
            if bars_group:
                self.remove(bars_group, poisson_function_text)
