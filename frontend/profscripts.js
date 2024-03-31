//Shows the pop up box with the information for each piece
function showModal(piece) {
  //cannot set video height while display is none bc the width is "60%", so
  //not a real number yet that can be multiplied and divided
  document.getElementById(piece).style.display = "inline-block";
  document.getElementsByTagName("body")[0].style.overflow = "hidden";
}

//Hides the pop up box with the information for each piece and stops any videos that areplaying
function hideModal(piece){
  document.getElementById(piece).style.display = "none";
  document.getElementsByTagName("body")[0].style.overflow = "scroll";
}

function createModal(class_code, results) {
    console.log("CREATE MODAL");
    // Create the modal container div
    var modalContainer = document.createElement('div');
    modalContainer.id = class_code + 'Modal';
    modalContainer.className = 'modal';

    // Create the modal content div
    var modalContent = document.createElement('div');
    modalContent.className = 'modalContent';

    // Create the close button span
    var closeButton = document.createElement('span');
    closeButton.className = 'closeBtn';
    closeButton.innerHTML = '&times;';
    closeButton.onclick = function() {
      hideModal(class_code + 'Modal');
    };

    // Create the heading elements
    var heading1 = document.createElement('h3');
    heading1.textContent = class_code;

    var heading2 = document.createElement('h4');
    heading2.textContent = 'Professor Rankings:';

    // Create the list element
    var list = document.createElement('ul');

    console.log(results);
    // Create list items
    var i = 1;
    for (var key in results) {
        var listItem = document.createElement('li');
        listItem.textContent = "Professor " + key + ' - Rank #' + i;
        list.appendChild(listItem);
    }

    // Append elements to the modal content div
    modalContent.appendChild(closeButton);
    modalContent.appendChild(heading1);
    modalContent.appendChild(heading2);
    modalContent.appendChild(list);

    // Append the modal content div to the modal container div
    modalContainer.appendChild(modalContent);

    // Append the modal container div to the body
    document.body.appendChild(modalContainer);

    //--------------------
    var button = document.createElement("button");
    button.textContent = class_code;
    button.onclick = function() {
        showModal(class_code + "Modal");
    };

    var buttonsRow = document.querySelector(".buttons-row");
    buttonsRow.appendChild(button);
}

//Code to make the website look nice when the window is resized
function resizeWindow(){
  setVidHeight(); // the video will shrink or grow depending on window sizes

  //changes the widths of the elements in the Main Content, so that no side scrolling is necessary
  var width = document.getElementsByTagName("nav")[0].style.width;
  if(width == "0px" || width == ""){
    setMCWidths(false); //nav bar is closed
  } else {
    setMCWidths(true); //nav bar is open
    if(window.innerWidth<800){
      document.getElementsByTagName("nav")[0].style.width = "100%";
    } else {
      document.getElementsByTagName("nav")[0].style.width = "500px";
    }
  }
}

//changes the width of the Main Content div when the window is resized
function setMCWidths(navOpen) {
  if(navOpen){
    var winWidth = window.innerWidth - 367; //window width minus the open nav bar
  } else {
    var winWidth = window.innerWidth - 17; //no nav bar to take into account
  }

  var mcStyle = document.getElementById("mainContent").style;
  mcStyle.paddingLeft = (winWidth * .05)+"px"; //left padding is 5% of window size
  mcStyle.paddingRight = (winWidth * .05)+"px"; //right padding is 5% of window size
  mcStyle.width = (winWidth *.9)+"px"; //width of content is 90% of window size
  document.getElementsByClassName("compTitle")[0].getElementsByTagName("h1")[0].style.width = winWidth+"px"; //for title
  //document.getElementById("footer").style.width = winWidth+"px"; //for footer
}

//opens the nav bar
function openNavBar() {
  showSurveyButton();

  if(window.innerWidth<800) {
    document.getElementsByTagName("nav")[0].style.width = "100%";
  }
  else {
    document.getElementsByTagName("nav")[0].style.width = "500px"; //opens nav bar by bringing it from 0 px to 250 px wide
  }
  document.getElementById("mainContent").style.marginLeft = "500px"; //Main Content left margin is 250 px to make room for nav bar
  document.getElementsByClassName("compTitle")[0].getElementsByTagName("h1")[0].style.marginLeft = "500px"; //for title
  /*document.getElementById("footer").style.marginLeft = "250px"; //for footer*/
  /*var openNavStyle = document.getElementById("openNav").style;
  openNavStyle.opacity = "0"; //the symbol to open the nav bar (the 3 lines) is set to 0 opacity (opacity allows for fade out transition)
  openNavStyle.visibility = "hidden"; //hides the 3 lines (with 0 opacity, the button can't be seen but is still active if the user hovers over it)*/
  document.getElementById("topBar").style.paddingLeft = "25px"; //aligns home icon with rest of side nav bar
  setMCWidths(true); //resizes the Main Content elements to make the page look nice
  //500 ms after the nav bar slides out, the stuff in the nav bar fades in
  setTimeout(function() {
    document.getElementsByTagName("nav")[0].getElementsByTagName("div")[0].style.opacity = "1";
  }, 500);

  
}

//closes the nav bar (basically like openNavBar(), but everything is in reverse)
function closeNavBar() {
  document.getElementsByTagName("nav")[0].getElementsByTagName("div")[0].style.opacity = "0"; //the stuff in the nav bar fades out
  //500 ms after the stuff in the nav bar fades out, the nav bar slides out, and the 3 lines to open the nav bar reappear
  setTimeout(function() {
    document.getElementsByTagName("nav")[0].style.width = "0px"; //closes the nav bar from 250 px to 0 px
    document.getElementById("mainContent").style.marginLeft = "0px"; //makes the left margin of the Main Content 0 px bc the nav bar is not there anymore
    document.getElementsByClassName("compTitle")[0].getElementsByTagName("h1")[0].style.marginLeft = "0px"; //for title
    //document.getElementById("footer").style.marginLeft = "0px"; //for footer
    //var openNavStyle = document.getElementById("openNav").style;
    /*
    openNavStyle.opacity = "1"; //the 3 lines fade in
    openNavStyle.visibility = "visible"; //the 3 lines are activated and are visible to users*/
    document.getElementById("topBar").style.paddingLeft = "4%"; //moves home icon back to original position
    setMCWidths(false); //resizes the Main Content elements to make the page look nice
  }, 500);
}

//darkens the image of the home icon when hovering over it
function hovIcon() {
  document.getElementById("homeIcon").src = "homeIconHov.png";
}

//undo the darkening when not hovering over the home icon
function unHovIcon() {
  document.getElementById("homeIcon").src = "homeIcon.png";
}

//makes the image of the home icon even darker when clicking on it
function clickIcon() {
  document.getElementById("homeIcon").src = "homeIconClick.png";
}




// Function to update the slider annotation text
function updateSliderAnnotation(sliderId, annotationId) {
  var sliderValue = document.getElementById(sliderId).value;
  var annotationText;
  
  // Define your annotation text based on the slider value
  if (sliderValue <= 3) {
    annotationText = sliderValue + ": Doesn't Matter";
  } else if (sliderValue <= 6) {
    annotationText = sliderValue + ": Definitely a Plus";
  } else {
    annotationText = sliderValue + ": Very Important";
  }
  
  // Update the annotation text
  document.getElementById(annotationId).innerText = annotationText;
}

// Call this function when you want to initialize and set up your slider annotations
function setupSliderAnnotations() {
  // Assuming you have two sliders for now as per your form setup
  var sliders = [
    { sliderId: "question1", annotationId: "question1-annotation" },
    { sliderId: "question2", annotationId: "question2-annotation" },
    { sliderId: "question3", annotationId: "question3-annotation" },
    { sliderId: "question4", annotationId: "question4-annotation" },
    { sliderId: "question5", annotationId: "question5-annotation" },
    { sliderId: "question6", annotationId: "question6-annotation" },
    { sliderId: "question7", annotationId: "question7-annotation" },
    { sliderId: "question8", annotationId: "question8-annotation" }

  ];

  sliders.forEach(function(item) {
    // Initial annotation update
    updateSliderAnnotation(item.sliderId, item.annotationId);
    
    // Setup event listener for real-time updates
    document.getElementById(item.sliderId).addEventListener('input', function() {
      updateSliderAnnotation(item.sliderId, item.annotationId);
    });
  });
}

function buildSchedule(preference) {
    var allCourses = document.querySelectorAll('#mainContent button');
    var schedule = document.getElementById('courseSchedule');
    schedule.innerHTML = '<h2>Your Customized Schedule:</h2>'; // Clear existing schedule and add title

    allCourses.forEach(function(course) {
        var courseTime = course.getAttribute('data-time');
        if ((preference === 'morning' && parseInt(courseTime.split(':')[0]) < 12) ||
            (preference === 'afternoon' && parseInt(courseTime.split(':')[0]) >= 12)) {
            var courseEntry = document.createElement('div');
            courseEntry.textContent = courseTime + ' - ' + course.textContent;
            schedule.appendChild(courseEntry);
        }
    });
}



// Ensure to call setupSliderAnnotations() when the document is ready or after the nav bar is generated
document.addEventListener("DOMContentLoaded", setupSliderAnnotations);

document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("surveyForm");
  form.addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
  });
});

function showSurveyButton() {
    var buttonDiv = document.getElementById("surveyButton");
    var image = buttonDiv.querySelector("img");
    var button = buttonDiv.querySelector("button");
    image.style.display = "none";
    button.style.display = "block";
}

function hideSurveyButton() {
    var buttonDiv = document.getElementById("surveyButton");
    var button = buttonDiv.querySelector("button");
    var image = buttonDiv.querySelector("img");
    button.style.display = "none";
    image.style.display = "block";
}

function getProfRecs() {

  hideSurveyButton();  

  // Initialize an object to store input values
  var inputValues = {"class_code": "", "ratings": {}};

  var classCodeInput = document.querySelectorAll('input[type="text"]');
  classCodeInput.forEach(function(input) {
    inputValues["class_code"] = input.value;
  });

  // Get the input elements by id or class
  var ratingInputs = document.querySelectorAll('input[type="range"]');

  // Loop through the input elements and store their values
  ratingInputs.forEach(function(input) {
    inputValues["ratings"][input.name] = input.value;
  });

  // Print the input values to the console
  console.log("Input values:", inputValues);

  var jsonData = JSON.stringify(inputValues);
  fetch('http://localhost:5000/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: jsonData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('Form submission successful:', data);
    closeNavBar();
    createModal(classCodeInput[0].value, data);
  })
  .catch(error => {
    console.error('There was a problem with the form submission:', error);
  });
}
