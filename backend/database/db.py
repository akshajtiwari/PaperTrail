import sqlite3 as sql
import logging

logging.basicConfig( #schema for  basic logging 
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
    logging.FileHandler("applications_db.log", encoding="utf-8")
)

logger = logging.getLogger(__name__) #initialise the logger

try:
    connection = sql.connect("applications.db")
    logger.info("Applications database created successfully")

    cursor = connection.cursor()

except Exception as e:
    logger.error(f"Failed to create database: {e}")

#create the applications table
create_applications_table="""
 CREATE TABLE IF NOT EXISTS applications (
  id TEXT PRIMARY KEY AUTOINCREMENT, #type TEXT so that uuid  are valid from the backend api 
  company_name varchar(255) NOT NULL,
  role_title varchar(255) NOT NULL,
  application_url VARCHAR(255) NULL,
  date_applied DATE NULL,
  status VARCHAR(255) NOT NULL,
  notes VARCHAR(255) NULL,
  created_at DATETIME NOT NULL,
  updated_at DATETIME NOT NULL
) """  #for the number 255/10 sqllite ignores it and it becomes infinite length column

try:
    cursor.execute(create_applications_table)
    logger.info("Applications Table was created successfully")

except Exception as e:
    logger.error(f"Failed to create the table: {e}")
#insert applications 
insert_applications="""
    INSERT into application(
    id,
    company_name,
    role_title,
    application_url,
    date_applied,
    status,
    notes,
    created_at,
    updated_at
    )"""

try:
    cursor.execute(insert_applications) 
    logger.info("Data inserted in the applications table successfully")
except Exception as e:
    logger.error(f"Failed to insert data in the applications table: {e}")
