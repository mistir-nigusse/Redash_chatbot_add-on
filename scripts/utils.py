import pandas as pd
import psycopg2
from sqlalchemy import create_engine



def run_sql_query(connection_params: dict, query: str) -> None:
    try:
        connection = psycopg2.connect(**connection_params)

        # Create a cursor
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(query)

        # Commit the transaction
        connection.commit()

        # Log success
        print("Log success")

    except Exception as e:
        print("Log the error: ", e)
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return None



def populate_dataframe_to_database(connection_params: dict, df: pd.DataFrame, table_name:str) -> None:
    try:
        # Extract connection parameters
        db_url = f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}"

        # Create database connection
        engine = create_engine(db_url, echo=False)

        # # Drop the table and its dependent objects (CASCADE)
        # with engine.connect() as connection:
        #     connection.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")

        # Insert DataFrame into the database
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

        # Log information
        print(f"Inserted {len(df)} rows into the database table {table_name}.")

    except Exception as e:
        # Log the error
        print(f"Error inserting data into the database: {e}")

    finally:
        # Close the connection
        if engine:
            engine.dispose()

    return None

def create_table_query(df: pd.DataFrame, table_name: str) -> str:
    try:
        # Dictionary to map column names to PostgreSQL data types
        data_type_mapping = {
            'int64': 'INTEGER',
            'float64': 'DOUBLE PRECISION',
            'object': 'TEXT',
            'datetime64[ns]': 'DATE'  # Explicitly add datetime type
            # Add more data types as needed
        }

        # Generate column definitions for the CREATE TABLE query
        column_definitions = ', '.join([f'"{column}" {data_type_mapping.get(str(df[column].dtype), "TEXT")}' for column in df.columns])

        # Determine the primary key based on the data types
        primary_key_columns = ['"' + df.columns[0] + '"']

        if table_name in ['viewership_by_date_table_data', "totals_table_data"]:
            primary_key_columns = ['"' + df.columns[0] + '"']

        elif df.columns[0] == "Date":
            primary_key_columns.append('"' + df.columns[1] + '"')

        # Create the primary key constraint
        primary_key_constraint = f'PRIMARY KEY ({", ".join(primary_key_columns)})'

        # Create the full CREATE TABLE query
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                {column_definitions},
                {primary_key_constraint}
            );
        '''
        return create_table_query

    except Exception as e:
        # Log the error
        print(f"Error creating table query: {e}")
        return ''
        