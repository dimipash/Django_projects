# MovieLister

MovieLister is a simple Django web application that allows users to search and browse through a collection of movies. The application implements pagination to display the movies in a organized manner across multiple pages.

## Features

- Search for movies by title
- View a list of movies with pagination (multiple pages)
- Navigate between pages using Next, Previous, First, and Last links
- Case-insensitive movie title search

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install the required Python packages: `pip install -r requirements.txt`
4. Set up the database and apply migrations: `python manage.py migrate`
5. Load sample movie data (optional): `python manage.py loaddata movies.json`
6. Start the development server: `python manage.py runserver`
7. Access the application at `http://localhost:8000`

## Usage

1. Open the application in your web browser
2. Use the search box to enter a movie title (partial or full)
3. The application will display a list of movies matching the search query
4. Use the pagination links (Next, Previous, First, Last) to navigate between pages
5. Click on a movie title to view its details (if implemented)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

Note: This README assumes that you have a basic understanding of Django and have set up the necessary database and movie data for the application. If you need further assistance, please refer to the Django documentation or open an issue in the repository.