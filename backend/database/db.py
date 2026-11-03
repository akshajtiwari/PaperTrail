import sqlite3 as sql
import logging

logging.basicConfig( #schema for  basic logging 
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
    logging.FileHandler("db.log", encoding="utf-8")
)

logger = logging.getLogger(__name__) #initialise the logger

try:
    connection = sql.connect("applications.db")
    logger.info("Applications database created successfully")

    cursor = connection.cursor()

except Exception as e:
    logger.error(f"Failed to create database: {e}")