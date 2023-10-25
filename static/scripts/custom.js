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



document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("ContactUsForm");

    form.addEventListener("submit", async function(e) {
      e.preventDefault();

      const formData = new FormData(form);
      const response = await fetch(form.action, {
        method: form.method,
        body: formData,
      });

      if (response.status === 200) {
        // Form submission successful
        Swal.fire({
          icon: 'success',
          title: 'Success',
          text: 'Data saved successfully!',
        });
        form.reset()
        // Optionally, you can redirect the user to another page here.
      } else {
        // Form submission failed
        const data = await response.json();
        if (data.errors) {
          // Server-side validation errors
          let errorMessages = "";
          for (const key in data.errors) {
            errorMessages += `${key}: ${data.errors[key].join(", ")}\n`;
          }
          console.log(errorMessages);
          Swal.fire({
            icon: 'error',
            title: 'Validation Error',
            text: "we have som truble in submiting your form" + errorMessages,
          });
        } else {
          // Handle other errors as needed
          Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'An error occurred while saving data.',
          });
        }
      }
    });
  });