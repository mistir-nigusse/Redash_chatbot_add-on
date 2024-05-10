import pandas as pd
import psycopg2

def connect_to_database(connection_params: dict):
    """
    Connects to the PostgreSQL database.
    paramters:
        connection_params is a dictionary that define the following:
        {
            'dbname': 'your_database_name',
            'user': 'your_username',
            'password': 'your_password',
            'host': 'your_host',
            'port': 'your_port'
            }
    """
    try:
        connection = psycopg2.connect(**connection_params)
        return connection
    except psycopg2.Error as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None

def load_data(table_name, csv_file, connection_params):
    """
    Loads data from a CSV file into a PostgreSQL table.
    """
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Connect to the PostgreSQL database
    connection = connect_to_database(connection_params)
    
    if connection:
        try:
            cursor = connection.cursor()
            
            # Drop the table if it already exists
            cursor.execute(f'DROP TABLE IF EXISTS {table_name}',db_params)
            connection.commit()
            
            # Create the table
            create_table_query = f'''
                CREATE TABLE "{table_name}" (
                    {", ".join([f'"{col}" TEXT' for col in df.columns])}
                )
            '''

            cursor.execute(create_table_query)
            connection.commit()
            
            # Insert data into the table
            for row in df.itertuples(index=False):
                insert_query = f'INSERT INTO {table_name} VALUES ({", ".join([f"%s" for _ in row])})'
                cursor.execute(insert_query, row)
            connection.commit()
            
            print(f"Data loaded successfully into '{table_name}' table.")
        except Exception as e:
            print(f"Error: Unable to load data into '{table_name}' table. {e}")
        finally:
            if connection:
                connection.close()
    else:
        print("Error: Unable to establish database connection.")


# Database connection parameters
db_params = {
    'dbname': 'youtube_data',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

# Load data into tables
load_data('content_type_table', 'data/Content type/Table data.csv', db_params)
load_data('content_type_chart', 'data/Content type/Chart data.csv', db_params)


# Load data for Device type
load_data('device_type_table', 'data/Device type/Table data.csv',db_params)
load_data('device_type_chart', 'data/Device type/Chart data.csv',db_params)

# Load data for Geography
load_data('geography_table', 'data/Geography/Table data.csv',db_params)
load_data('geography_chart', 'data/Geography/Chart data.csv',db_params)

# Load data for New and returning viewers
load_data('new_and_returning_viewers_table', 'data/New and returning viewers/Table data.csv',db_params)
load_data('new_and_returning_viewers_chart', 'data/New and returning viewers/Chart data.csv',db_params)

# Load data for Viewership by Date
load_data('viewership_by_date_table', 'data/Viewership by Date/Table data.csv',db_params)

# Load data for Viewer gender
load_data('viewer_gender_table', 'data/Viewer gender/Table data.csv',db_params)

# Load data for Viewer age
load_data('viewer_age_table', 'data/Viewer age/Table data.csv',db_params)

# Load data for Traffic source
load_data('traffic_source_table', 'data/Traffic source/Table data.csv',db_params)
load_data('traffic_source_chart', 'data/Traffic source/Chart data.csv',db_params)

# Load data for Subtitles and CC
load_data('subtitles_and_cc_table', 'data/Subtitles and CC/Table data.csv',db_params)
load_data('subtitles_and_cc_chart', 'data/Subtitles and CC/Chart data.csv',db_params)

# Load data for Subscription status
load_data('subscription_status_table', 'data/Subscription status/Table data.csv',db_params)
load_data('subscription_status_chart', 'data/Subscription status/Chart data.csv',db_params)

# Load data for Subscription source
load_data('subscription_source_table', 'data/Subscription source/Table data.csv',db_params)
load_data('subscription_source_chart', 'data/Subscription source/Chart data.csv',db_params)

# Load data for Sharing service
load_data('sharing_service_table', 'data/Sharing service/Table data.csv',db_params)
load_data('sharing_service_chart', 'data/Sharing service/Chart data.csv',db_params)

# Load data for Operating system
load_data('operating_system_table', 'data/Operating system/Table data.csv',db_params)
load_data('operating_system_chart', 'data/Operating system/Chart data.csv',db_params)

print("All data loaded successfully.")
