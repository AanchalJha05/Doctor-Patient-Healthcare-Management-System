// Example simple form validation
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', e => {
            const inputs = form.querySelectorAll('input[required]');
            for (let input of inputs) {
                if (!input.value) {
                    e.preventDefault();
                    alert('Please fill all required fields');
                    input.focus();
                    break;
                }
            }
        });
    });
});