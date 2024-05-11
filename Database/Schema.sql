-- Create the chart_data database
CREATE DATABASE youtube_data;

-- Switch to the youtube_data database
USE youtube_data;

-- Create the tables and relationships with primary and foreign keys

CREATE TABLE cities_table (
    Cities TEXT,
    CityName TEXT PRIMARY KEY,
    Geography TEXT,
    Geography1 TEXT,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE cities_chart (
    Date TEXT,
    Cities TEXT,
    CityName TEXT,
    Views INTEGER,
    FOREIGN KEY (CityName) REFERENCES cities_table_data (CityName)
);

CREATE TABLE content_type_table (
    ContentType TEXT PRIMARY KEY,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE content_type_chart (
    Date TEXT,
    ContentType TEXT,
    Views INTEGER,
    FOREIGN KEY (ContentType) REFERENCES content_type_table_data (ContentType)
);

CREATE TABLE device_type_table (
    DeviceType TEXT PRIMARY KEY,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE device_type_chart (
    Date TEXT,
    DeviceType TEXT,
    Views INTEGER,
    FOREIGN KEY (DeviceType) REFERENCES device_type_table_data (DeviceType)
);

CREATE TABLE geography_table (
    Geography TEXT PRIMARY KEY,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE geography_chart (
    Date TEXT,
    Geography TEXT,
    Views INTEGER,
    FOREIGN KEY (Geography) REFERENCES geography_table_data (Geography)
);

CREATE TABLE new_and_returning_viewers_table (
    NewAndReturningViewers TEXT PRIMARY KEY,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE new_and_returning_viewers_chart (
    Date TEXT,
    NewAndReturningViewers TEXT,
    Views INTEGER,
    FOREIGN KEY (NewAndReturningViewers) REFERENCES new_and_returning_viewers_table_data (NewAndReturningViewers)
);

CREATE TABLE operating_system_table (
    OperatingSystem TEXT PRIMARY KEY,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE operating_system_chart (
    Date TEXT,
    OperatingSystem TEXT,
    Views INTEGER,
    FOREIGN KEY (OperatingSystem) REFERENCES operating_system_table_data (OperatingSystem)
);

CREATE TABLE sharing_service_table (
    SharingService TEXT PRIMARY KEY,
    Shares INTEGER
);

CREATE TABLE sharing_service_chart (
    Date TEXT,
    SharingService TEXT,
    Shares INTEGER,
    FOREIGN KEY (SharingService) REFERENCES sharing_service_table_data (SharingService)
);

CREATE TABLE subscription_source_table (
    SubscriptionSource TEXT PRIMARY KEY,
    Subscribers INTEGER,
    SubscribersGained INTEGER,
    SubscribersLost INTEGER
);

CREATE TABLE subscription_source_chart (
    Date TEXT,
    SubscriptionSource TEXT,
    Subscribers INTEGER,
    FOREIGN KEY (SubscriptionSource) REFERENCES subscription_source_table_data (SubscriptionSource)
);

CREATE TABLE subscription_status_table (
    SubscriptionStatus TEXT PRIMARY KEY,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE subscription_status_chart (
    Date TEXT,
    SubscriptionStatus TEXT,
    Views INTEGER,
    FOREIGN KEY (SubscriptionStatus) REFERENCES subscription_status_table_data (SubscriptionStatus)
);

CREATE TABLE traffic_source_table (
    TrafficSource TEXT PRIMARY KEY,
    Views FLOAT,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT,
    Impressions FLOAT,
    ImpressionsClickThroughRate FLOAT
);

CREATE TABLE traffic_source_chart (
    Date TEXT,
    TrafficSource TEXT,
    Views INTEGER,
    FOREIGN KEY (TrafficSource) REFERENCES traffic_source_table_data (TrafficSource)
);

-- Create tables for data that only have table data

CREATE TABLE viewer_age_table (
    ViewerAge TEXT,
    ViewsPercentage FLOAT,
    AverageViewDuration TEXT,
    AveragePercentageViewed FLOAT,
    WatchTimeHoursPercentage FLOAT
);

CREATE TABLE viewer_gender_table (
    ViewerGender TEXT,
    ViewsPercentage FLOAT,
    AverageViewDuration TEXT,
    AveragePercentageViewed FLOAT,
    WatchTimeHoursPercentage FLOAT
);

CREATE TABLE viewership_by_age_table (
    Date TEXT,
    Views FLOAT,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);
