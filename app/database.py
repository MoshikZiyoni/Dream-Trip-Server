# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# # Replace 'your_database_url' with the actual URL of your database (e.g., PostgreSQL, MySQL, etc.)
# engine = create_engine('postgresql://postgres:Moshik1!@localhost/postgres', pool_size=10, max_overflow=20)
# Session = sessionmaker(bind=engine)

# from django.db import close_old_connections

# def get_connection():
#     close_old_connections()
from django.db import connection

def get_connection():
    return connection