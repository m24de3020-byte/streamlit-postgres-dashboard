"""Database connection module for PostgreSQL."""
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

@st.cache_resource
def get_db_connection():
    """Get PostgreSQL database connection - cached resource."""
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 5432)),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        return conn
    except Exception as e:
        st.error(f"Database connection error: {e}")
        return None

def execute_query(query, params=None):
    """Execute a SELECT query and return results."""
    try:
        conn = get_db_connection()
        if conn is None:
            return None, None
        
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        data = cursor.fetchall()
        cursor.close()
        
        return columns, data
    except Exception as e:
        st.error(f"Query execution error: {e}")
        return None, None
