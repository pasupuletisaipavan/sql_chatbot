# NL2SQL + Hybrid RAG System

This project is an enterprise-grade Natural Language to SQL (NL2SQL) and Hybrid Retrieval-Augmented Generation (RAG) system built using FastAPI. It aims to provide a robust foundation for converting natural language queries into SQL queries and integrating with various data sources.

## Project Structure

```
nl2sql-hybridrag-backend
├── src
│   ├── main.py                # Entry point of the FastAPI application
│   ├── api
│   │   └── v1
│   │       └── endpoints
│   │           └── foundation.py  # API endpoints for health checks and testing
│   ├── core
│   │   ├── config.py          # Centralized configuration using Pydantic
│   │   └── logging.py         # Structured logging setup
│   ├── models
│   │   └── foundation.py      # Data models for the application
│   ├── schemas
│   │   └── foundation.py      # Pydantic schemas for request/response validation
│   ├── services
│   │   └── foundation_service.py  # Service functions for business logic
│   ├── utils
│   │   └── helpers.py         # Utility functions for the application
│   └── types
│       └── index.py           # Custom types and interfaces
├── tests
│   ├── __init__.py            # Marks the tests directory as a package
│   └── test_foundation.py     # Unit tests for the foundation layer
├── requirements.txt            # Project dependencies
├── .env                        # Environment variables for configuration
├── .gitignore                  # Files and directories to ignore in version control
└── README.md                   # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd nl2sql-hybridrag-backend
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and define your environment variables, such as database connection strings and API keys.

5. **Run the application:**
   ```
   uvicorn src.main:app --reload
   ```

## Usage

- **Health Check:** 
  - Endpoint: `/health`
  - Method: `GET`
  - Description: Checks the health status of the application.

- **Test LLM:**
  - Endpoint: `/test-llm`
  - Method: `POST`
  - Description: Tests the Language Model functionality.

- **Test Embedding:**
  - Endpoint: `/test-embedding`
  - Method: `POST`
  - Description: Tests the embedding functionality.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.