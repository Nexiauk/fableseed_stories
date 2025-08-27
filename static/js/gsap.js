// Registering the GSAP animation plugins for split text and Scroll Trigger
gsap.registerPlugin(SplitText);
gsap.registerPlugin(ScrollTrigger);


document.fonts.ready.then(() => {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: ".hero-content",
            start: "top bottom",      // when the top of .hero hits 80% of viewport
            end: "bottom 20%",     // optional end
            toggleActions: "play none none none",
        }
    })

    SplitText.create(".hero-title", {
        type: "chars",
        autoSplit: true,
        onSplit: (self) => {
            tl.from(self.chars, {
                opacity: 0,
                x: 50,
                stagger: 0.1,
                duration: 1.5,
            })
        }
    });

    SplitText.create("#para1", {
        type: "lines",
        autoSplit: true,
        onSplit: (self) => {
            tl.from(self.lines, {
                opacity: 0,
                y: 50,
                stagger: 1,
                duration: 1.5
            }, "+=1")
        }
    });

    SplitText.create("#para2", {
        type: "lines",
        autoSplit: true,
        onSplit: (self) => {
            tl.from(self.lines, {
                opacity: 0,
                y: 50,
                stagger: 1,
                duration: 1.5,
            }, "+=2")
        }
    });

    SplitText.create("#para3", {
        type: "lines",
        autoSplit: true,
        onSplit: (self) => {
            tl.from(self.lines, {
                opacity: 0,
                y: 50,
                stagger: 1,
                duration: 1.5,
            }, "+=2")
        }
    });

    SplitText.create("#para4", {
        type: "lines",
        autoSplit: true,
        onSplit: (self) => {
            tl.from(self.lines, {
                opacity: 0,
                y: 50,
                stagger: 1,
                duration: 1.5,
            }, "+=2")
        }
    });

    SplitText.create("#para5", {
        type: "lines",
        autoSplit: true,
        onSplit: (self) => {
            tl.from(self.lines, {
                opacity: 0,
                y: 50,
                stagger: 1,
                duration: 1.5,
            }, "+=2")
        }
    });

    SplitText.create("#para6", {
        type: "lines",
        autoSplit: true,
        onSplit: (self) => {
            tl.from(self.lines, {
                opacity: 0,
                y: 50,
                stagger: 1,
                duration: 1.5,
            }, "+=2")
        }
    });

});