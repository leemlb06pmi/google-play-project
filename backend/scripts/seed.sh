#!/bin/bash

# PostgreSQL details
DB_NAME="your_database"
DB_USER="your_username"
DB_HOST="your_host"

# CSV file path and table name
CSV_FILE_PATH="/path/to/your/file.csv"
TEMP_TABLE_NAME="temp_table"
ACTUAL_TABLE_NAME="your_table"
# Columns to import
COLUMNS = "translated_review, sentiment, sentiment_polarity, sentiment_subjectivity" 
CREATE_TEMP_TABLE="CREATE TEMP TABLE $TEMP_TABLE_NAME (column1 datatype, column2 datatype, column3 datatype);"
# SQL COPY command to copy data into temporary table
COPY_COMMAND="\COPY $TEMP_TABLE_NAME($COLUMNS) FROM '$CSV_FILE_PATH' WITH (FORMAT csv, HEADER);"
# SQL command to insert data into actual table
INSERT_INTO_ACTUAL="INSERT INTO $ACTUAL_TABLE_NAME($COLUMNS) SELECT $COLUMNS FROM $TEMP_TABLE_NAME;"
# SQL command to drop the temporary table
DROP_TEMP_TABLE="DROP TABLE $TEMP_TABLE_NAME;"
# Execute the commands
psql -d $DB_NAME -U $DB_USER -h $DB_HOST -c "$CREATE_TEMP_TABLE"
psql -d $DB_NAME -U $DB_USER -h $DB_HOST -c "$COPY_COMMAND"
psql -d $DB_NAME -U $DB_USER -h $DB_HOST -c "$INSERT_INTO_ACTUAL"
psql -d $DB_NAME -U $DB_USER -h $DB_HOST -c "$DROP_TEMP_TABLE"
echo "Data copied successfully into $ACTUAL_TABLE_NAME"

