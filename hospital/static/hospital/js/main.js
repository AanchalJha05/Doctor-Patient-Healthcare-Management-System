// Simple form validation + animation

document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", (e) => {
            let valid = true;

            form.querySelectorAll("input, select").forEach(input => {
                if (!input.value) {
                    valid = false;
                    input.style.border = "2px solid red";
                }
            });

            if (!valid) {
                e.preventDefault();
                alert("Please fill all fields!");
            }
        });
    });
});