# Tech Challenge API

[![Static Badge](https://img.shields.io/badge/video-ededed?style=for-the-badge&logo=youtube&logoColor=red)](https://www.youtube.com)
[![Static Badge](https://img.shields.io/badge/live-lightgreen?style=for-the-badge&logo=render&label=demo)](https://tech-challenge-one.onrender.com)

## The Problem

This project provides REST API endpoints for authentication and data retrieval concerning production, processing, and commercial activities in vitiviniculture. These endpoints are designed to serve data directly to machine learning models, dashboards, and notebooks.

## Architecture Diagram

![Architecture Diagram](./assets/architecture_diagram.png)

### Tech Stack

* **Core API Development:** Python, FastAPI, Pydantic (data validation and settings).
* **Authentication:** JWT (secure user authentication and authorization).
* **Infrastructure & Deployment:** Docker (containerization), Poetry (dependency management), Redis (caching), Render (cloud deployment).
* **Data Acquisition:** BeautifulSoup and Requests (web scraping).

### User Flow

1.  **Authentication**: Users authenticate by sending credentials to the `/auth/token` endpoint, receiving a JWT in return.
2.  **Data Access**: The JWT is then used to access and retrieve data from protected `/embrapa` endpoints.
3.  **JSON Output**: All data is provided in a structured JSON format to be consumed.

### Services

- **URL Parsing**: Responsible for constructing the URL to be requested and scrapped by the Scrapping service.
- **Scrapping**: Receives an URL for scrapping and returns the information in a JSON format.

### App Structure

The project is organized into the following directories:

| Directory        | Description                                                            |
|------------------|------------------------------------------------------------------------|
| **`api/`**       | Contains API routes, organized by version for better maintainability.  |
| **`core/`**      | Includes core application settings such as configuration and security. |
| **`schemas/`**   | Houses Pydantic models used for request and response validation.       |
| **`services/`**  | Implements business logic and integrates with external services.       |

This structure promotes modularity and makes the codebase easier to navigate and extend.

## Local Development

To run the project locally, ensure you have Docker and Docker Compose installed. Follow these steps:

1. Clone the repository:

    ```bash
    gh repo clone lucas-tremaroli/tech-challenge-one && cd tech-challenge-one
    ```

2. Build and run the Docker container:

    ```bash
    docker-compose up --build
    ```

3. Access the API at `http://localhost:8000`.
4. Use the Swagger UI at `http://localhost:8000/docs` to interact with the API.
5. Use the ReDoc UI at `http://localhost:8000/redoc` for API documentation.
