# main.py
# Import necessary modules and types for the FastAPI application
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from contextlib import asynccontextmanager

# Database connection string - replace with actual credentials
DATABASE_URL = "postgresql://<user>:<pass>@<host>:5432/<dbname>"
# Create database engine with connection pooling
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Define the Todo model that maps to the 'todos' table in the database
class Todo(SQLModel, table=True):
    # Primary key field, auto-generated
    id: Optional[int] = Field(default=None, primary_key=True)
    # Content field to store the todo item text
    content: str

# Lifespan context manager to handle startup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create all database tables based on defined models
    SQLModel.metadata.create_all(engine)
    yield
    # Shutdown: Cleanup operations would go here if needed

# Initialize FastAPI app with the lifespan handler
app = FastAPI(lifespan=lifespan)

# Dependency function to provide database sessions
def get_session():
    # Create and yield a database session
    with Session(engine) as session:
        yield session

# POST endpoint to create a new todo item
@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, session: Session = Depends(get_session)):
    # Add the new todo to the session
    session.add(todo)
    # Commit the changes to the database
    session.commit()
    # Refresh the todo object with updated data from the database
    session.refresh(todo)
    # Return the created todo
    return todo

# GET endpoint to retrieve all todo items
@app.get("/todos/")
def read_todos(session: Session = Depends(get_session)):
    # Execute a select query to get all Todo records
    return session.exec(select(Todo)).all()

# GET endpoint to retrieve a specific todo item by ID
@app.get("/todos/{id}")
def read_todo(id: int, session: Session = Depends(get_session)):
    # Get the todo with the specified ID from the database
    todo = session.get(Todo, id)
    # If the todo doesn't exist, raise a 404 error
    if not todo:
        raise HTTPException(status_code=404)
    # Return the found todo
    return todo


# ___________________________________________________________________________#
'''

### DB Session (SQLModel / SQLAlchemy)

**`Session`** = database connection wrapper.

**What it does:**

* Opens DB connection
* Sends queries
* Manages transactions
* Commits or rolls back
* Closes automatically

**Usage:**

```python
with Session(engine) as session:
```

* Open connection
* Use during request
* Auto-close after request

**Why sessions are needed:**

* Transaction safety
* Prevents connection leaks
* Handles commit / rollback
* Isolates each request

**Without a session:**

* No transaction safety
* Partial / broken writes
* Leaked connections
* Race conditions

**Rule:**

* **1 request = 1 DB session**

**Shortest meaning:**
Sessions safely communicate with the database.
'''
# ___________________________________________________________________________#
