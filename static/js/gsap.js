/* global gsap, SplitText, ScrollTrigger */

// Registering the GSAP animation plugins
// SplitText: allows splitting text into characters, words, or lines for animation
// ScrollTrigger: triggers animations when elements enter/exit the viewport
gsap.registerPlugin(ScrollTrigger, SplitText);


// Wait until all fonts are loaded before running animations
// This ensures SplitText measures lines correctly, especially in Firefox
document.fonts.ready.then(() => {

    // Use requestAnimationFrame to wait for the browser to finish layout and painting
    // Prevents Firefox from miscalculating line positions
    requestAnimationFrame(() => {

        // Create a timeline for all hero animations
        // Attach a ScrollTrigger so animations play on scroll
        let tl = gsap.timeline({
            scrollTrigger: {
                trigger: ".hero-content", // element that triggers the timeline
                start: "top bottom",      // start when top of trigger hits bottom of viewport
                toggleActions: "play none none none", // play on enter, do nothing else
            }
        });

        // Animate the hero title character by character
        SplitText.create(".hero-title", {
            type: "chars", // split text into individual characters
            onSplit: (self) => {
                // Reveal the parent container
                gsap.set(".hero-title", { visibility: "visible" });

                // Animate each character from opacity 0 and x offset
                tl.from(self.chars, {
                    opacity: 0,   // start invisible
                    x: 50,        // start offset on x-axis
                    stagger: 0.1, // animate characters one after another
                    duration: 1.5 // duration per character
                }, 0);
            }
        });

        // Animate paragraph 1 line by line
        SplitText.create("#para1", {
            type: "lines",
            autoSplit: true,
            onSplit: (self) => {
                gsap.set("#para1", { visibility: "visible" });
                tl.from(self.lines, {
                    opacity: 0,
                    y: 50,
                    stagger: 1,
                    duration: 1.5,
                }, 1);
            }
        });

        // Animate paragraph 2 line by line
        SplitText.create("#para2", {
            type: "lines",
            autoSplit: true,
            onSplit: (self) => {
                gsap.set("#para2", { visibility: "visible" });
                tl.from(self.lines, {
                    opacity: 0,
                    y: 50,
                    stagger: 1,
                    duration: 1.5,
                }, 6); // add 2-second delay in timeline
            }
        });

        // Animate paragraph 3 line by line
        SplitText.create("#para3", {
            type: "lines",
            autoSplit: true,
            onSplit: (self) => {
                gsap.set("#para3", { visibility: "visible" });
                tl.from(self.lines, {
                    opacity: 0,
                    y: 50,
                    stagger: 1,
                    duration: 1.5,
                }, 12);
            }
        });

        // Animate paragraph 4 line by line
        SplitText.create("#para4", {
            type: "lines",
            autoSplit: true,
            onSplit: (self) => {
                gsap.set("#para4", { visibility: "visible" });
                tl.from(self.lines, {
                    opacity: 0,
                    y: 50,
                    stagger: 1,
                    duration: 1.5,
                }, 18);
            }
        });

        // Animate paragraph 5 line by line
        SplitText.create("#para5", {
            type: "lines",
            autoSplit: true,
            onSplit: (self) => {
                gsap.set("#para5", { visibility: "visible" });
                tl.from(self.lines, {
                    opacity: 0,
                    y: 50,
                    stagger: 1,
                    duration: 1.5,
                }, 24);
            }
        });

        // Animate paragraph 6 line by line
        SplitText.create("#para6", {
            type: "lines",
            autoSplit: true,
            onSplit: (self) => {
                gsap.set("#para6", { visibility: "visible" });
                tl.from(self.lines, {
                    opacity: 0,
                    y: 50,
                    stagger: 1,
                    duration: 1.5,
                }, 30);
            }
        });
        ScrollTrigger.refresh();
    });
});
