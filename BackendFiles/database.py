from sqlalchemy import create_engine, text 
from sqlalchemy.orm import sessionmaker #orm converts python code to sql
from dotenv import load_dotenv
import os
from pymysql.constants import CLIENT
load_dotenv()

# saving the db url to a variable
db_url = f"mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}"

#create_engine access the db via the url
engine = create_engine(db_url, connect_args={"client_flag": CLIENT.MULTI_STATEMENTS})

#Creating an instance of the sessionmaker, the session maker creates a session
session = sessionmaker(bind=engine)
db = session()

create_tables_query = text("""
CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,
                           name VARCHAR(100) NOT NULL,
                           email VARCHAR(100) NOT NULL,
                           password VARCHAR(20) NOT NULL);

CREATE TABLE IF NOT EXISTS courses(id INT AUTO_INCREMENT PRIMARY KEY,
                           title VARCHAR(100) NOT NULL,
                           level VARCHAR(100) NOT NULL);

CREATE TABLE IF NOT EXISTS enrollments(id INT AUTO_INCREMENT PRIMARY KEY,
                           userid INT,
                           courseid INT,
                           FOREIGN KEY(userid) REFERENCES users(id),
                           FOREIGN KEY (courseid) REFERENCES courses(id));
""")

data_table_query = db.execute(create_tables_query)
