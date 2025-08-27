function handleRowClick(e) {
    const link = e.currentTarget.dataset.href
    window.location.href = link;
}

const seedTableRows = document.querySelectorAll(".clickable")
seedTableRows.forEach((row) => {
    row.addEventListener("click", handleRowClick)
})

document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll(".delete");
    const deleteMessage = document.getElementById("delete-message")
    const deleteConfirm = document.getElementById("delete-confirm")

    deleteButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const dataTarget = btn.getAttribute("data-id")
            const dataType = btn.getAttribute("data-type")
            deleteMessage.showModal()
            deleteConfirm.href = `/prune/${dataType}/${dataTarget}/`
        });
    });
});

// Registering the GSAP animation plugin for split text
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












// let titleSplit = SplitText.create(".hero-title", {
//     type: "chars",
//     autoSplit: true
// });

// let textSplit = SplitText.create(".hero-text", {
//     type: "lines",
//     autoSplit: true
// });


// tl.from(titleSplit.chars, {
//     opacity: 0,
//     y: 50,
//     duration: 1.5,
//     stagger: 0.2,
// });

// tl.from(textSplit.lines, {
//     opacity: 0,
//     y: 50,
//     duration: 1.5,
//     stagger: { amount: 2 },
// });
