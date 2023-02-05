# FastTrack

A family chore management API built with Python and FastAPI. This app allows families to assign and track chores, rewards, and punishments for their children, all while keeping track of each child's balance.

## Features

- Create and manage tasks for family members
- Assign monetary value to tasks
- Keep track of balance for each family member
- Create rewards and punishments that can be purchased with the balance

## Tech Stack

- Python 3.9
- FastAPI
- SQLAlchemy
- JWT
- Docker
- NodeJS
- Vue or React (I haven't decided yet)

## Getting Started

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies using `pip install -r requirements.txt`
4. Run `docker-compose up` to start the application
5. Access the API through `http://localhost:8000`
6. Swagger API documentation found at `http://localhost:8000/docs`
7. ReDoc API documentation found at `http://localhost:8000/redoc`
8. Access the pgAdmin UI for the database at `http://localhost:5050`
9. Run `docker-compose down -v` to stop the application and delete the database
10. Run `docker-compose down` to stop the application

## Project Structure

The project is structured as follows:

- `app`: Main application module
- `app/main.py`: Entry point for the application
- `app/models.py`: Database models
- `app/routers`: API endpoints
- `app/Functions`: CRUD operations for the models
- `app/dbConnection.py`: Database setup
- `app/logs`: Logs
- `app/models.py`: SQLAlchemy models for PostgreSQL
- `app/Functions/test_*.py`: Test files for the application

## Current Progress

- [x] Setting up the project structure
- [x] Database models
- [ ] CRUD operations
- [ ] JWT authentication
- [ ] Error handling
- [ ] Data validation
- [ ] API endpoints
- [ ] Frontend

## Future Additions

- [ ] Ability for multiple families to use the app
- [ ] Ability for families to create their own rewards and punishments
- [ ] Ability for families to assign their own children tasks

## Contact

If you have any questions or suggestions, please feel free to contact me at `skyler@attracdev.com`

## Acknowledgments

I would like to extend my gratitude to OpenAI's GPT-3 model for providing valuable assistance throughout the development of this project. It's a new concept, asking for guidance from an AI, but it definitely proved useful more than once. That said, there were more than a few times I tried to get some info by consulting ChatGPT, only to be run around in circles and not given accurate information. This was definitely a good trial-run for using it as a utility.
