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
    let titleSplit = SplitText.create(".hero-title", {
        type: "chars",
        autoSplit: true,
    });

    let textSplit = SplitText.create(".hero-text", {
        type: "lines",
        autoSplit: true,
    });

    let tl = gsap.timeline({
        scrollTrigger: ".hero"
    })

    tl.from(titleSplit.chars, {
        opacity: 0,
        y: 50,
        duration: 1.5,
        stagger: 0.2,
    });

    tl.from(textSplit.lines, {
        opacity: 0,
        y: 50,
        duration: 1.5,
        stagger: { amount: 2 },
    });
})
