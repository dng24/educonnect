document.addEventListener("DOMContentLoaded", function () {
    // Initial page load slide-in effect
    document.body.classList.add('slide-in');

    // Initially hide the main content and disable scrolling
    document.getElementById("content").style.display = "none";
    document.body.style.overflow = "hidden";

    // Function to check the email and password fields
    window.checkFields = function() {
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;
        
        if (email && password) {
            // Show content and enable scrolling if both fields are filled
            document.getElementById("content").style.display = "block";
            document.body.style.overflow = "auto";
        } else {
            // Hide content and disable scrolling if either field is empty
            document.getElementById("content").style.display = "none";
            document.body.style.overflow = "hidden";
        }
    };

    // Add event listeners to range inputs for survey
    document.querySelectorAll('.question input[type="range"]').forEach(input => {
        input.oninput = function() {
            document.getElementById(this.id + '-value').textContent = this.value;
        };
    });

    // Transition effect for specific navigation (e.g., index to landing page)
    var transitionLinks = document.querySelectorAll('a[href="landing.html"]');
    transitionLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            var destination = this.href;

            document.body.classList.add('slide-out');

            setTimeout(function() {
                window.location = destination;
            }, 500); // Ensure this matches your CSS animation duration
        });
    });
});
