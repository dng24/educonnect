# EduConnect
#### A web application that pairs students with instructors based on learning style compatibility
This application was developed in less than 48 hours as part of the Innovate Hackathon at Northeastern University, hosted by the AINU and Babson AI clubs.

## Functionality / TL;DR:
EduConnect consists of 5 main components:
- Frontend
- Backend
  - The backend includes the web scrapers, LLM integration, and custom ranking algorithm.
- Web Scrapers
- LLM Integration
- Custom Ranking Algorithm

### Frontend
The main functionality of the frontend is located in **[frontend file]**. Here, users answer questions using sliders to describe their study habits and learning styles. They also input which class they are trying to pick a professor for.

User inputs are passed to the backend for processing.

Styling is handled in **[styling file]**.

Additionally, there are speculative features such as **calendar integration**, located in **[calendar feature file]**.

### Backend Framework
The backend is built using Python and the Flask framework. Flask was chosen due to the simplicity and small scale of the project, which required minimal requests.

Backend routes handle user data submission, web scraping, and algorithm execution. The routes are located in **[backend file]**.

### Web Scrapers
We implemented two web scrapers:

1. **Course Professor Scraper**: This scraper retrieves professors for specific courses by scraping Northeastern University's Banner website. It uses Selenium due to the lack of suitable web requests for this data. The scraper is located in **[scraper file 1]**.

2. **Professor Reviews Scraper**: This scraper gathers qualitative and quantitative data about professors from RateMyProfessors.com. We initially planned to use Trace evaluations, but they are behind two-factor authentication. The scraper is in **[scraper file 2]**.

### LLM Integration
Qualitative data scraped from professor reviews is processed using an LLM to quantify aspects of teaching style and summarize strengths and weaknesses. Prompt engineering ensures that the LLM returns both numeric and text-based responses. The LLM processing is located in **[LLM integration file]**.

### Custom Algorithm
After gathering and quantifying professor data, a custom algorithm matches it with user input to calculate a compatibility score. The algorithm adjusts weights based on the importance users assign to various factors. The compatibility scores are ranked, and summaries from the LLM are appended to each professor's profile. The algorithm is located in **[algorithm file]**.

### Demo
**[Insert Demo Video]**

### Future Features
Potential future features include:
- Calendar integration with students' Banner accounts to limit professor selections based on availability.
- Inputs for time-of-day preferences.
- Automatic schedule suggestions based on student preferences.
