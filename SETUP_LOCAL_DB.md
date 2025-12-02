# PostgreSQL Local Database Setup Guide

## Prerequisites
- PostgreSQL installed on your system
- Python 3.8+ installed
- Streamlit installed
- Text editor or IDE

## Step 1: Check if PostgreSQL is Running

### Windows
```bash
# Check if PostgreSQL service is running
sc query postgresql-x64-15

# Or open Services and look for "postgresql-x64-15"
```

### macOS
```bash
# Check if PostgreSQL is running
brew services list | grep postgresql

# Start PostgreSQL if not running
brew services start postgresql
```

### Linux (Ubuntu/Debian)
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Start PostgreSQL
sudo systemctl start postgresql

# Enable on boot
sudo systemctl enable postgresql
```

## Step 2: Get Your PostgreSQL Credentials

### Connect to PostgreSQL
```bash
# On Windows (in Command Prompt or PowerShell)
psql -U postgres

# On macOS/Linux
psql -U postgres
```

You'll be prompted for the password (the one you set during PostgreSQL installation).

### Create a Test Database
```sql
CREATE DATABASE test_db;
\l  -- List all databases
```

### Get Your Host/Port Information
```sql
SELECT version();  -- Shows PostgreSQL version and host info
```

Typical values:
- **Host**: localhost or 127.0.0.1
- **Port**: 5432 (default)
- **User**: postgres (default)
- **Database**: test_db (or your database name)
- **Password**: Your PostgreSQL password

## Step 3: Create .env File in Your Project

1. Open the project root directory
2. Create a file named `.env` (not `.env.example`)
3. Add your database credentials:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=test_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
```

## Step 4: Test the Connection Locally

1. Clone or navigate to the project:
```bash
cd streamlit-postgres-dashboard
```

2. Create and activate virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

The app should open at `http://localhost:8501`

## Step 5: Create Sample Data (Optional)

If you want to test the dashboard with sample data:

```bash
psql -U postgres -d test_db
```

Then run these SQL commands:

```sql
-- Create a sample products table
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(10, 2),
  category VARCHAR(50),
  stock INT
);

-- Insert sample data
INSERT INTO products (name, price, category, stock) VALUES
  ('Laptop', 999.99, 'Electronics', 15),
  ('Mouse', 29.99, 'Electronics', 50),
  ('Keyboard', 79.99, 'Electronics', 30),
  ('Monitor', 299.99, 'Electronics', 10),
  ('Desk Chair', 199.99, 'Furniture', 8),
  ('Desk Lamp', 49.99, 'Furniture', 20);

-- Verify data
SELECT * FROM products;
```

## Step 6: Test Query Execution in Dashboard

1. Go to "Data Explorer" page in the Streamlit app
2. Change the SQL query to:
```sql
SELECT * FROM products;
```
3. Click "Execute Query"
4. You should see the data displayed in a table

## Troubleshooting

### Error: "Connection refused" or "Cannot assign requested address"
**Solution**: PostgreSQL is not running. Start the service using the commands above.

### Error: "fe_sendauth: no password supplied"
**Solution**: Password is incorrect in .env file or PostgreSQL password authentication failed.

**Fix**:
```bash
# Reset PostgreSQL password
psql -U postgres -h localhost
# Or update your .env file with correct password
```

### Error: "Database 'test_db' does not exist"
**Solution**: Create the database first:
```sql
CREATE DATABASE test_db;
```

### Error: "port 5432 is already in use"
**Solution**: Another application is using port 5432, or PostgreSQL is running twice.

**Find and kill the process** (macOS/Linux):
```bash
lsof -i :5432
kill -9 <PID>
```

### Streamlit says "No module named 'psycopg2'"
**Solution**: Reinstall requirements:
```bash
pip install --upgrade -r requirements.txt
```

## Common PostgreSQL Commands

```bash
# Connect to database
psql -U postgres -d test_db

# List all databases
\l

# Connect to a database
\c test_db

# List all tables
\dt

# Show table structure
\d table_name

# Exit PostgreSQL
\q

# Run SQL file
psql -U postgres -d test_db -f script.sql
```

## Next Steps

1. ✅ Verify connection works
2. ✅ Create sample tables and data
3. ✅ Test queries in Data Explorer
4. ✅ Customize dashboard for your data
5. ✅ Deploy to Streamlit Cloud with .env variables

## For Streamlit Cloud Deployment

When deploying to Streamlit Cloud, add your database credentials as secrets:

1. Go to app settings in Streamlit Cloud
2. Navigate to "Secrets"
3. Add:
```toml
DB_HOST = "your-db-host"
DB_PORT = "5432"
DB_NAME = "your-db-name"
DB_USER = "your-user"
DB_PASSWORD = "your-password"
```

Streamlitmakes these available via `st.secrets` or `.env` file.
