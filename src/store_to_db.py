import os
import pandas as pd
from sqlalchemy import create_engine
os.chdir('..')
from sqlalchemy.orm import sessionmaker
from ..models.location import Location
from ..models.analytics import Analytics
from ..models.new_returning_viewers import NewReturningViewers

engine = create_engine('postgresql://missy:123456@localhost/youtube_data')

# Step 3: Create the tables in the database
Location.metadata.create_all(engine)
Analytics.metadata.create_all(engine)
NewReturningViewers.metadata.create_all(engine)

# Step 4: Read the CSV files
cities = pd.read_csv('../data/Cities/Chart data.csv')
content_type = pd.read_csv('../data/Content type/Chart data.csv')
device_type = pd.read_csv('../data/Device type/Chart data.csv')
geography = pd.read_csv('../data/Geography/Chart data.csv')
new_and_returning_viewers = pd.read_csv('../data/New and returning viewers/Chart data.csv')
operating_system = pd.read_csv('../data/Operating system/Chart data.csv')
sharing_service = pd.read_csv('../data/Sharing service/Chart data.csv')
subscription_source = pd.read_csv('../data/Subscription source/Chart data.csv')
subscription_status = pd.read_csv('../data/Subscription status/Chart data.csv')
subtitles_and_cc = pd.read_csv('../data/Subtitles and CC/Chart data.csv')
traffic_source = pd.read_csv('../data/Traffic source/Chart data.csv')
viewership_by_data = pd.read_csv('../data/Traffic source/Table Data.csv')

# Step 5: Convert date columns to proper data type
date_columns = ['Date', 'date']  # Add all date columns here

for df in [cities, content_type, device_type, geography, new_and_returning_viewers,
           operating_system, sharing_service, subscription_source, subscription_status,
           subtitles_and_cc, traffic_source, viewership_by_data]:
    for col in date_columns:
        if col in df:
            df[col] = pd.to_datetime(df[col])

# Step 6: Drop unnecessary columns if needed (not necessary in this case)

# Step 7: Migrate the data to the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a dictionary of dataframes
data_frames = {
    'location': cities,
    'analytics': content_type,  # Assuming content_type contains all analytics data
    'new_returning_viewers': new_and_returning_viewers
}

# Migrate data to the database
for table_name, df in data_frames.items():
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Commit changes and close session
session.commit()
session.close()
