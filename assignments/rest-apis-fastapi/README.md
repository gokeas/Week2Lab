# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will learn how to design and implement a RESTful API using the FastAPI framework in Python. The focus is on creating endpoints, using Pydantic models for validation, and running the service with uvicorn.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Build a basic API with at least three endpoints (GET, POST, DELETE) to manage a simple resource such as "items" or "books".

#### Requirements
Completed program should:

- Define Pydantic models for request and response data.
- Implement GET, POST, DELETE routes using FastAPI.
- Run the application with uvicorn and respond with JSON.


### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance the API by adding validation rules and proper error responses.

#### Requirements
Completed program should:

- Validate incoming data using Pydantic field constraints.
- Return meaningful HTTP status codes for invalid inputs.
- Include sample input and output in comments or documentation.


### 🛠️ Write Basic Tests (Optional/Extension)

#### Description
(Optional) Write simple tests using FastAPI's TestClient or pytest to verify the endpoints.

#### Requirements
Completed program should:

- Include at least two test cases covering different endpoints.
- Tests should programmatically send requests and check responses.
