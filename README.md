# Requirements
Docker Desktop:
```https://www.docker.com/products/docker-desktop/```

# Installation Guide

1. Clone the repository:
   ```git clone https://github.com/kmehta25/fetch-receipt-processor.git```
2. Open Docker Desktop
3. Open an editor or terminal in the root directory of the project, which contains all the Docker files (the outer fetch_backend folder).
4. In the terminal, use the following command to create and execute the Docker containers and set up the environment ```docker-compose --build```
5. Once the containers are set up and running, the APIs can be found at port 8000 and can be interacted with and tested using the Swagger link: ```http://localhost:8000/swagger```   
6. In order to run the pre-existing test cases in the app, the web container needs to be accessed via a terminal. This may be done using Docker desktop, by clicking on the container itself and going to the 'terminal' tab. This can also be done via a terminal as follows:
- Make sure you are in the outer fetch_backend folder where the docker files are
- use the following command to access the web container's terminal: ```docker exec -it fetch_backend-web-1 bash```
- Once you are in the terminal, use the following command to run the test cases: ```python manage.py test```


## Tech Stack:

Language: *Python 3.11.0*

Backend API: *Django REST Framework*

Database: *Postgres*

Containerization : *Docker*

API Documentation: *Swagger

**Author**:
*Kunj Viral Kumar Mehta*
