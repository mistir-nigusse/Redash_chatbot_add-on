from langchain.agents import tool
from typing import Optional
from pydantic import BaseModel, Field
from typing import List, Tuple

from utils import get_postgres_data, get_postgres_df

class SQLQuery(BaseModel):
    query: str = Field(description="SQL query to execute")

@tool
def execute_sql(query: str) -> Tuple[List[Tuple], List[Tuple]]:
    """Returns the result of SQL query execution and cursor description"""
    return get_postgres_data(query)


class SQLTable(BaseModel):
    table: str = Field(description="Table name")

@tool
def get_table_columns(table:str) -> str:
    """Returns a list of table column names and types in JSON"""

    query = f'''
   SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = '{table}';
    '''

    result_df = get_postgres_df(query)

    # Convert the result DataFrame to a list of dictionaries
    result_list = result_df.to_dict('records')

    # Convert the list to a JSON-formatted string
    return str(result_list)


class SQLTableColumn(BaseModel):
    database: str = Field(description="Database name")
    table: str = Field(description="Table name")
    column: str = Field(description="Column name")
    n: Optional[int] = Field(description="Number of rows, default limit 10")

@tool
def get_table_column_distr( table: str, column: str, n:int = 10) -> str:
    """Returns top n values for the column in JSON"""
    print(column)
    q = f'''

     SELECT "{column}", COUNT(1) AS count
    FROM {table}
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT {n};

    '''

    return str(list(get_postgres_df(q)[column].values))

tools = [execute_sql,get_table_columns,get_table_column_distr]

# converting tools into OpenAI functions
sql_functions = list(map(format_tool_to_openai_function, 
    [execute_sql, get_table_columns, get_table_column_distr]))
