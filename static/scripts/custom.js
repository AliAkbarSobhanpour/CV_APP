const toggleButtons = document.querySelectorAll('.toggle-button');
const hiddenImages = document.querySelectorAll('.hidden-image');
const fullscreenImage = document.getElementById('fullscreen-image');
const fullscreenImageContent = document.getElementById('fullscreen-image-content');

toggleButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
        // Set the source of the full-screen image
        fullscreenImageContent.src = hiddenImages[index].src;
        // Display the full-screen image
        fullscreenImage.style.display = 'block';
    });
});

// Function to close the full-screen image
function closeFullscreen() {
    fullscreenImage.style.display = 'none';
}

