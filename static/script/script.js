const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
const links = document.querySelectorAll('.nav-links li'); // Select all nav links

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('active'); // Toggle the close (X) icon
});

// Close navbar when a link is clicked on mobile
links.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        hamburger.classList.remove('active'); // Change back to hamburger icon
    });
});


// Initialize AOS animations
AOS.init({
    duration: 1000, // Animation duration
    once: true     // Only animate once
});



// Show or hide the back-to-top button based on scroll position
window.onscroll = function () {
    let button = document.getElementById("back-to-top");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
};

// Scroll to top when the button is clicked
document.getElementById("back-to-top").addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});



function validateForm() {
    let name = document.forms['contactForm']['name'].value;
    let phone = document.forms['contactForm']['phone'].value;
    let message = document.forms['contactForm']['message'].value;

    if (name == '' || hasNumber(name)) {
        alert('Name must be filled out and must only contain letters');
        return false;
    } else if (!/^\+?\d+$/.test(phone)) {
        alert('Phone number seems to contain letters');
        return false;
    } else if (message == '') {
        alert('Message must be filled out');
        return false;
    } else {
        // confirm or cancel
        return confirm('Do you really want to sent the message?')
    }
}

function hasNumber(myString) {
    return /\d/.test(myString);
}