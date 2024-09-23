# EduConnect
#### A web application that pairs students with instructors based on learning style compatibility
This application was developed in less than 48 hours as part of the InnovAIte Hackathon at Northeastern University, hosted by the AINEU and Babson AI clubs.

## TL;DR:
EduConnect consists of 5 main components:
- Frontend
- Backend
  - The backend includes the web scrapers, LLM integration, and custom ranking algorithm.
- Web Scrapers
- LLM Integration
- Custom Ranking Algorithm

## Demo Video
[Youtube video demo](https://youtu.be/mEA085TzxbI)

## Functionality
### Frontend
The main functionality of the frontend is located in **[the frontend folder](https://github.com/dng24/educonnect/tree/master/frontend)**. Here, users answer questions using sliders to describe their study habits and learning styles. They also input which class they are trying to pick a professor for.

User inputs are passed to the backend for processing.

Styling is handled in **[profstyles.css](https://github.com/dng24/educonnect/blob/master/frontend/profstyles.css)**, 
**[style.css](https://github.com/dng24/educonnect/blob/master/frontend/style.css)**, and **[styler.css](https://github.com/dng24/educonnect/blob/master/frontend/styler.css)**.

Additionally, there are speculative features such as **calendar integration**.

### Backend Framework
The backend is built using Python and the Flask framework. Flask was chosen due to the simplicity and small scale of the project, which required minimal requests.

Backend routes handle user data submission, web scraping, and algorithm execution. The routes are located in **[main.py](https://github.com/dng24/educonnect/blob/master/backend/main.py)**.

### Web Scrapers
We implemented two web scrapers:

1. **Course Professor Scraper**: This scraper retrieves professors for specific courses by scraping Northeastern University's Banner website. It uses Selenium due to the lack of suitable web requests for this data. The scraper is located in **[login.py](https://github.com/dng24/educonnect/blob/master/backend/login.py)**.

2. **Professor Reviews Scraper**: This scraper gathers qualitative and quantitative data about professors from RateMyProfessors.com. We initially planned to use Trace evaluations, but they are behind two-factor authentication. The scraper is in **[ratemyprof.py](https://github.com/dng24/educonnect/blob/master/backend/ratemyprof.py)**.

### LLM Integration
Qualitative data scraped from professor reviews is processed using an LLM to quantify aspects of teaching style and summarize strengths and weaknesses. Prompt engineering ensures that the LLM returns both numeric and text-based responses. The LLM processing is located in **[llm.py](https://github.com/dng24/educonnect/blob/master/backend/llm.py)**.

### Custom Algorithm
After gathering and quantifying professor data, a custom algorithm matches it with user input to calculate a compatibility score. The algorithm adjusts weights based on the importance users assign to various factors. The compatibility scores are ranked, and summaries from the LLM are appended to each professor's profile. The algorithm is located in **[algorithm.py](https://github.com/dng24/educonnect/blob/master/backend/Algorithm.py)**.

## Future Features
Potential future features include:
- Calendar integration with students' Banner accounts to limit professor selections based on availability.
- Inputs for time-of-day preferences.
- Automatic schedule suggestions based on student preferences.

## Credits
Daniel Ip - Selenium Webscraper, Custom Algorithm, README file

Dev Patel - LLM integration/prompt engineering

Derek Ng - Flask App, ratemyprofessor webscraper

Anthony Campos, Julia Arkin, Yefan He - Front end design
