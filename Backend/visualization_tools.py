from redashAPI import RedashAPIClient
from langchain.agents import tool
from typing import Optional
from pydantic import BaseModel, Field
from typing import List, Tuple

from utils import get_postgres_data, get_postgres_df


Redash = RedashAPIClient(api_key, api_url)

@tool
def create_redash_query(data_source_id: int, query: str, name: str, description: str="", options: dict=None):
    """Create a query in Redash and return the response json"""
    response = Redash.create_query(data_source_id, name, query, description, options)
    return response.json()

@tool
def create_redash_visualization(query_id: int, visualization_type: str, name: str,columns:list=None,  x_axis:str=None, y_axis: list=None):
    """Create a visualization in Redash and return the response json"""
    response = Redash.create_visualization(qry_id=query_id, _type=visualization_type, name=name,columns=columns, x_axis=x_axis, y_axis=y_axis)
    return response.json()

@tool
def create_redash_dashboard(name: str):
    """Create a dashboard in redash and return the response json"""
    response = Redash.create_dashboard(name)
    return response.json()

@tool
def add_widget_on_dashboard(dashboard_id: int, text: str="", visualization_id: int=None, full_width: bool=False, position: dict=None):
    """Add a widget in redash dashboard and return the response json"""
    response = Redash.add_widget(dashboard_id, text, visualization_id, full_width, position)
    return response.json()


@tool
def publish_dashboard(self, dashboard_id: int):
    """ Publish dashboard and return the response json"""
    response = Redash.publish_dashboard(dashboard_id)
    return response.json()
    