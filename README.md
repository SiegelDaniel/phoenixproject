# Prerequisites

# Docker
This application is validated to run on Windows 11.  
First, make sure to install Docker Desktop and enable WSL2 for it to run, as using HyperV virtualization may cause problems.  

Make sure to first create a virtual volume within Docker Desktop and call it postgres. 

Using 
````
    docker run --name pgsql-dev -e POSTGRES_PASSWORD=phoenix -e POSTGRES_DB=db -d  --mount source=postgres,target=/var/lib/postgresql/data -p 5432:5432 postgres
````

We create a container with a PostgreSQL database. It is not necessary to use PostgreSQL, any other SQL database will work too.  
If you are not using this PostgreSQL container, then make sure to change the connection string in main.py.

# Node
Install NodeJS to host the frontend: https://nodejs.org/de/download  

## Running the frontend  
In the phoenix2/vue-frontend, run ``` npm install & npm run serve```.  
It assumes you are running the backend at ```localhost:8000```.

## API Specification
The API specification can be viewed at ```localhost:8000/docs```

# Limitations
There are several limitations in this app that were not fully polished to due lack of time.
- A general limitation is the lack of async operations.
- The session management is not optimized yet. It does not allow for concurrent access to a database as it does not use scoped sessions.  
- There are no tests (yet)

 # Repository
- All repositories currently do not support bulk/batch operations.
- Importing files needs a specific order due to the relations between Employees, Departments and Projects.  
- The order is as follows: departments => projects => employees 

# Controller
- The controller currently uses the domain models as DTOs to the frontend. A clean separation of concerns would allow for DTOs, Domain Models and DAOs to be separate.

# Frontend
- As it is written in JS, the frontend practically provides no Type-safety.  This can be migitated by porting it to Typescript.  
- The styling is very rudimentary and can be improved drastically.  
- The URLs are hardcoded into the frontend and could be made configurable by an environment variable.  (This is especially interesting for docker-compose deployment)

