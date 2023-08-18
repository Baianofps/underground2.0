document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // You would typically send the credentials to the backend for authentication
    // For this example, let's assume successful login
    const userRole = "manager"; // Assuming the manager's role

    // Redirect to the next page based on the user's role
    if (userRole === "manager") {
        window.location.href = "manager_page.html";
    } else {
        window.location.href = "employee_page.html";
    }
});