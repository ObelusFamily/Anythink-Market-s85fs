# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## First setup

1. Install Docker from here https://docs.docker.com/get-docker/

2. Once the installation is successfull . You can verify docker is ready by running the following commands in your terminal: docker -v and docker-compose -v.

3. Now we will load Anythink's frontend and backend using the following command: docker-compose up

4. If Docker is working correctly, the backend should be running and able to connect to your local database.
   Let's test this by pointing your browser to http://localhost:3000/api/ping
   It sghould look like this:
   ![image](https://user-images.githubusercontent.com/62787867/182322551-b112f068-5c80-4a92-9827-b77d1a309b49.png)

5. Easy Peasy! The backend is up and running.
   Now, it’s time to check the frontend and make sure it’s connected to the backend.
   If everything is working properly, you’ll be able to create a new user on http://localhost:3001/register
   It should look like this:
   ![image](https://user-images.githubusercontent.com/62787867/182323811-061e25e5-78ad-41b2-a33c-7a13c08581ad.png)
   
6. Your environment is ready! 😀


