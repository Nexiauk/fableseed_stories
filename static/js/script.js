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
    const deleteMessage = document.getElementById("delete_message")

    deleteButtons.forEach(btn => {
        btn.addEventListener("click", (e) => {
            let dataTarget = e.target.getAttribute("data-id")
            deleteMessage.showModal()
        });
    });
});
