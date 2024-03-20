# Django CV Generator

This is a Django web application that allows users to create and manage their CV (Curriculum Vitae) profiles. Users can fill out a form with their personal details, education, work experience, and skills, and the application will generate a PDF version of their CV.

## Features

- User registration and authentication
- Create, update, and delete CV profiles
- Generate PDF versions of CVs
- View and download CV PDFs

## Prerequisites

- Python 3.x
- Django
- wkhtmltopdf (for PDF generation)

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/django-cv-generator.git
```

2. Install Python dependencies:
```
pip install -r requirements.txt
```

3. Install wkhtmltopdf:
   - On Ubuntu/Debian: `sudo apt-get install wkhtmltopdf`
   - On macOS (using Homebrew): `brew install wkhtmltopdf`
   - On Windows: Download the installer from [wkhtmltopdf website](https://wkhtmltopdf.org/downloads.html) and add the binary to your system's PATH.

4. Run database migrations:
```
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```

6. Open your web browser and navigate to `http://localhost:8000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Note: Make sure to replace `your-username` with your actual GitHub username in the clone URL.