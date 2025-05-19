# Tech Challenge API

This is a FastAPI-based project designed to provide endpoints for authentication and data retrieval related to production, processing, and commercial activities. This project is part of a technical challenge and demonstrates the use of modern Python web development practices.

## Features

- **Authentication**: Secure login using OAuth2 with password flow.
- **Production Data**: Retrieve production data for a given year.
- **Processing Data**: Retrieve processing data for a given year and option.
- **Commercial Data**: Retrieve commercial data for a given year.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lucas-tremaroli/tech-challenge-one.git
   cd tech-challenge-one
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

1. Access the API documentation at `http://127.0.0.1:8000/docs`.
2. Authenticate using the following credentials:
   - **Username**: `fiap`
   - **Password**: `secret`
3. Use the available endpoints:
   - `/auth/token`: Obtain an access token.
   - `/auth/users/me/`: Retrieve the current user's details.
   - `/embrapa/production/{year}`: Get production data for a specific year.
   - `/embrapa/processing/{year}/{option}`: Get processing data for a specific year and option.
   - `/embrapa/commercial/{year}`: Get commercial data for a specific year.

## Development

### Pre-requisites

- Python 3.10 or higher
- FastAPI
- Uvicorn

### Code Structure

- **`app/api/v1`**: Contains the API routes for authentication and data retrieval.
- **`app/core`**: Core configurations and authentication logic.
- **`app/schemas`**: Pydantic models for request and response validation.
- **`app/services`**: Services for fetching and parsing data from external sources.

## Technologies Used

- **FastAPI**: For building the web API.
- **Pydantic**: For data validation.
- **Passlib**: For password hashing.
- **JWT**: For token-based authentication.
- **BeautifulSoup**: For parsing HTML data.
- **Requests**: For making HTTP requests.
