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


document.fonts.ready.then(() => {
    let split = SplitText.create(".hero-text", {
        type: "lines",
        autoSplit: true,
        // onSplit: (self) => {
        //     gsap.from(self.lines, {
        //         yPercent: "random([-100, 100])",
        //         rotation: "random(-30, 30)",
        //         ease: "back.out",
        //         // y: 100,
        //         autoAlpha: 0,
        //         stagger: {
        //             amount: 0.05,
        //             from: "random",
        //             yoyo: true,
        //         }
        //     })
        // }
    })
})
