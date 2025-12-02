# Streamlit PostgreSQL Dashboard

A comprehensive Streamlit dashboard application for creating reports and analytics with PostgreSQL database connection.

## Features

- PostgreSQL database connection
- Interactive data visualization
- Real-time dashboard updates
- Sample reports with drill-down capabilities
- Data filtering and search functionality
- Export data to CSV

## Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/m24de3020-byte/streamlit-postgres-dashboard.git
cd streamlit-postgres-dashboard
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── config.py             # Configuration settings
├── database.py           # Database connection handler
├── pages/                # Multi-page app pages
│   ├── dashboard.py      # Main dashboard page
│   └── reports.py        # Reports page
└── README.md
```

## License

MIT
