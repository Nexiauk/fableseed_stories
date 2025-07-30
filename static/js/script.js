const seedTableRows = document.querySelectorAll(".clickable")

seedTableRows.forEach((row) => {
    row.addEventListener("click", () => {
        const link = row.dataset.href
        window.location.href = link;
    })
})