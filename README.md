# Educonnect
#### A web application to pair students with the instructors most compatible with their learning style
This application was created in less than 48 hours as part of the Innovate hackathon at Northeastern University produced by the AINU club, and the Babson 
AI club.
## Functionality
The app consists of 5 main components which are not mutually exclusive: The frontend, the backend, the web scrapers, the LLM integration, and the custom ranking algorithm. 
The backend contains all other components with the exception of the frontend.
### Frontend
The primarily functional part of the front end is contained in the **insert file** file. 
This is where users can use the sliders to answer questions about their study habits and their learning styles. They 
also input which class they are currently trying to pick a professor for.
The inputs the users produce here are what gets fed into the back end. 

The styling is contained in the **insert file** file. 

There is also a more speculative piece of the front end that contains **calendar features, y, and z**, which is contained in the **insert file** files.
### Backend framework
The backend implementation is built in Python with the Flask framework. Our choice of framework was primarily because of how small the application was, and how few requests 
we needed to implement for the purposes of the hackathon. The backend consists of web request routes to receive user input data, 2 web scrapers to gather relevant information 
from the web, and a custom algorithm to generate compatibility scores. The backend routes are contained in the **insert file**
### Web Scraper
The web scrapers are for the purposes of retrieving data on professors. There are two main scrapers. 

Firstly, to retrieve the professors who teach each class: 
Once a specific course has been determined through user input, a scrape to the Northeastern University Banner 
website takes place to see which professors are teaching that class. This is unfortunately quite slow right now as the scrape has to performed with Selenium since no suitable 
web requests were found that could return the appropriate data. This scraper is in the **Insert File**

Secondly, to gather qualitative and quantitative data about professors performance:
A simpler scrape using the Python requests library was performed to gather all professor reviews and ratings from the website ratemyprofessors.com. The original intention was to 
use the official trace evaluations, but they were discovered to all be behind a 2 factor authentication layer of security. 
The ratemyprofessor.com scraper is in the **insert file**
### LLM integration 
Once qualitative data has been scraped from each professor's page, the data is processed by an LLM to quantify certain aspects of their teaching styles, as well as getting summarized paragraphs about the given professor's strengths and weaknesses. Prompt engineering is used to determine the format in which the information is returned. Data relating to specific teaching styles that needs to be quantified is returned as a series of integers, and qualitative data is returned in simple string format. The LLM processing is contained in the **insert file**
### Custom Algorithm
Once professor data has been gathered and quantified, it is passed through an algorithm with the user input data to determine final compatibility. The algorithm accounts for the student strength in certain, as well as the professor compatibility for those factors. Each factor is either increased or reduced by a multiplier which is determined by the students self-identifying the importance of each factor to their overall learning experience. This algorithm is contained in the **insert file**


All factors are aggregated to determine a final compatibility score for the student and the professor. This process is repeated for each professor who teaches the class in question. Overally professor strengths and weaknesses which were summarized by the LLM are added to to the end of each professor profile. Processed results are returned to the front end in ranked order of compatibility for the user to judge.

## Demo
**Insert Video**
## Features to be implemented
Ideas for future features included a calendar feature that would automatically integrate with the student's banner account so that they could be limited to classes and professors that worked with their existing schedules. 

Plans for calendar also included adding inputs relating to time of day preferences with users. 

Plans for calendar also included producing suggested full schedules based on student preferences.
