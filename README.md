# Steelers Hype App

## 1) Executive Summary

**Problem:** The Pittsburgh Steelers fanbase is one of the most passionate and die-hard fandoms in not just the NFL but across all the major sports leagues. Steelers Nation takes pride in their players, and those that especially rise to the top hold a special place in all Steelers' fans hearts. These players - both past and present - have a connection to each and every Yinzer because of the massive importance that the Steelers have for their fans. With such a rich history, there are players across generations that have made an impact on the Steel-City. However, multimedia content surronding these great Steelers players are scattered across the web, making it difficult for enthusiastic Steelers fans to find exactly what they are looking for when they want to be hyped up for their team or to reminisnce on the good-ole days of Steeler football.

**Solution:** Steelers Hype Central is an app that is a central hub containing players who date back to the glory years of the 1970s all the way to the current Steelers team under Mike Tomlin. This app allows users to take a look at each of these players, like the great Ben Roethlisberger and Hall of Famer Mean Joe Greene, and be in awe of their presence through the screen as they view their greatness in a Steelers uniform. By clicking on a player, the user is directed to a highlight, tribute, or hype video about that player that is surely guaranteed to fire the user up. Even if the user isn't a Steelers fan, this app will likely increase their appreciation and respect for such a historic and proud organization that is the Pittsburgh Steelers. 


## 2) System Overview

**Course Concepts:** Flask API, Containerization with Docker, Cloud Deployment with Azure App Service

**Architecture Diagram:**

![Architecture Diagram](assets/architecture.png)

**Data/Models/Services:**
The app uses information of 12 former and current Pittsburgh Steelers Players. Each player record contains:
- ID 
- Name
- Image Path (png, webp, JPEG)
- Video Path (mp4)

Licensing: the application includes a LICENSE file for project code (MIT License). All videos pulled for the project are credited at the bottom of the app under "Videos Used" 


## 3) How to Run (Local)

**Docker**
```bash
# build
docker build -t steelers-hype-app:latest .

# run
docker run --rm -p 8080:8080 steelers-hype-app:latest

# health check 
curl http://localhost:8080/health
```


## 4) Design Decisions

**Why this Concept?**  I decided to create a Flask app with Docker containerization because it is a simple yet foundational concept that could carry out my vision of my Steelers app. I chose Flask over FastAPI despite FlaskAPI being a little faster and more modern because I believed Flask was suitable enough for the basic framework of my project. As for the container, I chose Docker over Appainter because Docker seemed easier for general development and deployment tasks (which again aligned with the simple strucutre of my app) while Appainter is direct more towards higher performance computing with a need for security. Finally, I also considered to employ blob storage for my app, but decided against it because I wanted the app to be more defined (by separating the players that users can click on) rather than just having one place to store pictures and videos.

**Tradeoffs:** 
- Performance: 