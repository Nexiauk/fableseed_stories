function handleRowClick(e) {
        const link = e.currentTarget.dataset.href
        window.location.href = link;
}

const seedTableRows = document.querySelectorAll(".clickable")
seedTableRows.forEach((row) => {
    row.addEventListener("click", handleRowClick)
})