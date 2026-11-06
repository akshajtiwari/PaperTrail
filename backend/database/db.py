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


try:
    connection = sql.connect("applications.db")

    logger.info("Applications database created successfully")

    cursor = connection.cursor()
    #create the applications table
    #type TEXT so that uuid  are valid from the backend api 
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


    try:
        cursor.execute(create_applications_table)
        logger.info("Applications Table was created successfully")
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

    except sql.Error as e:
        logger.error(f"Failed to create the table: {e}")
        

    try:
        values = (
            "some-uuid",
            "Google",
            "SDE Intern",
            "https://careers.google.com",
            "2026-11-06",
            "Applied",
            "Campus application",
            "2026-11-06T19:00:00",
            "2026-11-06T19:00:00"
        )
        cursor.execute(insert_applications,values) 
        logger.info("Data inserted in the applications table successfully")
        connection.commit()
    except sql.Error as e:
        logger.error(f"Failed to insert data in the applications table: {e}")
except sql.Error as e:
    logger.error(f"Database operations failed: {e}")
