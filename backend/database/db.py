import sqlite3 as sql
import logging

logging.basicConfig(
    level=logging.INFO,
    format="{asctime} [{levelname}] {name}: {message}",
    style="{",
    handlers=[
        logging.FileHandler("applications_db.log", encoding="utf-8")
    ]
)


logger = logging.getLogger(__name__) #initialise the logger 

# QUERIES IN FORM OF VARIABLES
create_applications_table=""" 
    CREATE TABLE IF NOT EXISTS applications (
      id TEXT PRIMARY KEY, 
      company_name varchar(255) NOT NULL,
      role_title varchar(255) NOT NULL,
      application_url VARCHAR(255) NULL,
      date_applied DATE NULL,
      status VARCHAR(255) NOT NULL,
      notes VARCHAR(255) NULL,
      created_at DATETIME NOT NULL,
      updated_at DATETIME NOT NULL
    ) """  #for the number 255/10 sqllite ignores it and it becomes infinite length column

insert_applications="""
            INSERT into applications(
            id,
            company_name,
            role_title,
            application_url,
            date_applied,
            status,
            notes,
            created_at,
            updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
def get_db_connection():
    try:
        connection=sql.connect("applications.db")
        logger.info("Database Created Successfully")
        cursor=connection.cursor()
        return cursor ,connection
    except sql.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise
    
def initialise_database():
    cursor, connection = get_db_connection()

    try:
        cursor.execute(create_applications_table)
        connection.commit()
        logger.info("Applications table created successfully")

    except sql.Error as e:
        logger.error(f"Failed to create the table: {e}")
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()
if __name__=="__main__":
    initialise_database()
