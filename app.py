"""Main Streamlit Application - PostgreSQL Dashboard."""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from database import execute_query
# Page configuration
st.set_page_config(
    page_title="PostgreSQL Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        .metric-card {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 PostgreSQL Dashboard & Reports")
st.markdown("""---""")

# Sidebar navigation
with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Select a page:",
        ["Dashboard", "Data Explorer", "Reports", "Settings"]
    )

if page == "Dashboard":
    st.header("Dashboard Overview")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", "1,234", "+5%")
    with col2:
        st.metric("Active Users", "456", "+12%")
    with col3:
        st.metric("Last Updated", "2 min ago", "-1%")
    
    # Sample Chart
    st.subheader("Sample Data Trend")
    
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [65, 78, 90, 81, 95, 107],
        'Revenue': [2300, 2100, 2290, 2000, 2181, 2500]
    }
    df = pd.DataFrame(data)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Month'], y=df['Sales'],
        mode='lines+markers', name='Sales'
    ))
    fig.add_trace(go.Scatter(
        x=df['Month'], y=df['Revenue'],
        mode='lines+markers', name='Revenue'
    ))
    fig.update_layout(title="Sales and Revenue Trend", height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == "Data Explorer":
    st.header("Data Explorer")
    
    # SQL Query Input
    query_input = st.text_area(
        "Enter SQL Query:",
        "SELECT * FROM information_schema.tables LIMIT 10;",
        height=100
    )
    
    if st.button("Execute Query"):
        try:
            columns, data = execute_query(query_input)
            if columns:
                df = pd.DataFrame(data, columns=columns)
                st.success(f"Query executed successfully! Rows: {len(df)}")
                st.dataframe(df, use_container_width=True)
                
                # Download CSV
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download as CSV",
                    data=csv,
                    file_name="query_results.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"Error: {e}")

elif page == "Reports":
    st.header("Reports")
    
    report_type = st.selectbox(
        "Select Report Type:",
        ["Sales Report", "User Activity", "Performance Analysis"]
    )
    
    st.subheader(f"Generating {report_type}...")
    
    # Generate sample report
    report_data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Q1': [100, 150, 200, 120],
        'Q2': [120, 160, 210, 140],
        'Q3': [140, 180, 230, 160],
        'Q4': [160, 200, 250, 180]
    }
    report_df = pd.DataFrame(report_data)
    
    # Bar chart
    fig = go.Figure(data=[
        go.Bar(name='Q1', x=report_df['Category'], y=report_df['Q1']),
        go.Bar(name='Q2', x=report_df['Category'], y=report_df['Q2']),
        go.Bar(name='Q3', x=report_df['Category'], y=report_df['Q3']),
        go.Bar(name='Q4', x=report_df['Category'], y=report_df['Q4'])
    ])
    fig.update_layout(barmode='group', height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(report_df, use_container_width=True)

else:  # Settings
    st.header("Settings")
    
    st.subheader("Database Configuration")
    st.info("Database connection settings can be configured via .env file")
    
    col1, col2 = st.columns(2)
    with col1:
        db_host = st.text_input("Database Host")
        db_name = st.text_input("Database Name")
    with col2:
        db_port = st.text_input("Database Port")
        db_user = st.text_input("Database User")
    
    if st.button("Test Connection"):
        st.success("Connection test would be implemented here")

st.markdown("---")
st.markdown("© 2024 Streamlit PostgreSQL Dashboard")
