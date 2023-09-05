// Get the current page URL
var currentUrl = window.location.href;

// Check if the current URL matches the respective page and add the "active" class
if (currentUrl.includes("home")) {
    document.getElementById("home-link").classList.add("active");
} else if (currentUrl.includes("features")) {
    document.getElementById("features-link").classList.add("active");
} else if (currentUrl.includes("why-us")) {
    document.getElementById("why-us-link").classList.add("active");
} else if (currentUrl.includes("pricing")) {
    document.getElementById("pricing-link").classList.add("active");
}