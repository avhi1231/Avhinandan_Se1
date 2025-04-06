document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registerForm');
    const errorMsg = document.getElementById('errorMsg');

    form.addEventListener('submit', function (e) {
        const username = document.getElementById('username').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();

        if (!username || !email || !password) {
            e.preventDefault(); // stop form submission
            errorMsg.textContent = "All fields are required.";
        } else if (password.length < 6) {
            e.preventDefault();
            errorMsg.textContent = "Password must be at least 6 characters.";
        } else {
            errorMsg.textContent = "";
        }
    });
});
