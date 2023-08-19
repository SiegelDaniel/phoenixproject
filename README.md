# Prerequisites

This application is validated to run on Windows 11.  
First, make sure to install Docker Desktop and enable WSL2 for it to run, as using HyperV virtualization may cause problems.  

Make sure to first create a virtual volume within Docker Desktop and call it postgres. 

Using 
````
    docker run --name pgsql-dev -e POSTGRES_PASSWORD=phoenix -e POSTGRES_DB=db -d  --mount source=postgres,target=/var/lib/postgresql/data -p 5432:5432 postgres
````

We create a container with a PostgreSQL database. It is not necessary to use PostgreSQL, any other SQL database will work too.  
If you are not using this PostgreSQL container, then make sure to change the connection string in main.py.

# Limitations
There are several limitations in this app that were not fully polished to due lack of time.  

 # Repository
- All repositories currently do not support bulk/batch operations.

# Controller
- The controller currently uses the domain models as DTOs to the frontend. A clean separation of concerns would allow for DTOs, Domain Models and DAOs to be separate.  
- 