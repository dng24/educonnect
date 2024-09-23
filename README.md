# Educonnect
#### A web application to pair students with the instructors most compatible with their learning style
This application was created in less than 48 hours as part of the Innovate hackathon at Northeastern University produced by the AINU club, and the Babson 
AI club.
## Functionality
The app consists of 5 main components which are not mutually exclusive: The frontend, the backend, the web scrapers, the LLM integration, and the custom ranking algorithm. 
The backend contains all other components with the exception of the frontend.
### Frontend
The primarily functional part of the front end is contained in the ____ file. 
This is where users can use the sliders to answer questions about their study habits and their learning styles. 
The inputs the users produce here are what gets fed into the back end. 

The styling is contained in the ____ file. 

There is also a more speculative piece of the front end that contains ___calendar features, y, and z,_ which is contained in the ____ files.
### Backend framework
The backend implementation is built in Python with the Flask framework. Our choice of framework was primarily because of how small the application was, and how few requests 
we needed to implement for the purposes of the hackathon. The backend consists of web request routes to receive user input data, 2 web scrapers to gather relevant information 
from the web, and a custom algorithm to generate compatibility scores.
### Web Scraper
The web scrapers are for the purposes of retrieving data on professors. There are two main scrapers. 

Firstly, to retrieve the professors who teach each class: 
Once a specific course has been determined through user input, a scrape to the Northeastern University Banner 
website takes place to see which professors are teaching that class. This is unfortunately quite slow right now as the scrape has to performed with Selenium since no suitable 
web requests were found that could return the appropriate data.  

Secondly, to gather qualitative and quantitative data about professors performance:
A simpler scrape using the Python requests library was performed to gather all professor reviews and ratings from the website ratemyprofessors.com. The original intention was to 
use the official trace evaluations, but they were discovered to all be behind a 2 factor authentication layer of security. 
### LLM integration 

### Custom Algorithm
