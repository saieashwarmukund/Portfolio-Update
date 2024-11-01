function showContent(id) {
    // Hide all content sections
    document.querySelectorAll('.more-content').forEach(content => {
        content.classList.remove('active');
        content.classList.add('d-none');
    });

    // Show the selected content section
    document.getElementById(id).classList.remove('d-none');
    document.getElementById(id).classList.add('active');
}
