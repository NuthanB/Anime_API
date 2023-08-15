# Anime API

This is a simple RESTful API built using Flask that allows you to manage anime data. It provides endpoints for adding, retrieving, updating, and deleting anime records.

## Getting Started

To get started with the Anime API, follow the steps below:

### Prerequisites

- Python (version 3.6 or higher)
- Flask
- Flask SQLAlchemy

### Installation

1. Clone the repository or download the source code.

2. Install the required dependencies using pip:
   pip install -r requirements.txt

## Usage

1. Start the API server by running the following command:
   python app.py


The API server will start running on `http://localhost:5000`.

2. You can now access the API using the following endpoints:

- `GET /anime`: Retrieves all anime records.
- `GET /anime/<anime_id>`: Retrieves a single anime record by its ID.
- `POST /anime`: Adds a new anime record. Requires a JSON payload with `name`, `description`, `seasons`, and `episodes_per_season`.
- `PUT /anime/<anime_id>`: Updates an existing anime record by its ID. Requires a JSON payload with any fields to be updated (`name`, `description`, `seasons`, or `episodes_per_season`).
- `DELETE /anime/<anime_id>`: Deletes an anime record by its ID.

Replace `<anime_id>` in the URL with the actual ID of the anime record.

### Examples

Here are some examples of how to use the API endpoints:

# Retrieve all anime
GET /anime

# Retrieve a single anime with ID 1
GET /anime/1

# Add a new anime
POST /anime
Content-Type: application/json

{
"name": "Attack on Titan",
"description": "A thrilling anime series set in a world dominated by Titans.",
"seasons": 4,
"episodes_per_season": "12-25"
}

# Update an existing anime with ID 1
PUT /anime/1
Content-Type: application/json

{
"name": "Attack on Titan: The Final Season",
"description": "The epic conclusion to the Attack on Titan series.",
"seasons": 4,
"episodes_per_season": "16-24"
}

# Delete an anime with ID 1
DELETE /anime/1

## Error Handling
The API returns appropriate error messages and status codes in case of any errors or invalid requests. For example, if a requested anime record is not found, the API will return a JSON response with a message indicating the error.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.