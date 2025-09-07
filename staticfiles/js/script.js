function handleRowClick(e) {
    const link = e.currentTarget.dataset.href;
    window.location.href = link;
}

const seedTableRows = document.querySelectorAll(".clickable")
seedTableRows.forEach((row) => {
    row.addEventListener("click", handleRowClick);
});

document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll(".delete");
    const deleteMessage = document.getElementById("delete-message");
    const deleteConfirm = document.getElementById("delete-confirm");

    deleteButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const dataTarget = btn.getAttribute("data-id");
            const dataType = btn.getAttribute("data-type");
            deleteMessage.showModal();
            deleteConfirm.href = `/prune/${dataType}/${dataTarget}/`;
        });
    });
});
