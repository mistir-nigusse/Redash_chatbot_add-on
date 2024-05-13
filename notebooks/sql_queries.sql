
            CREATE TABLE IF NOT EXISTS subscription_status_chart_data (
                "Date" TEXT, 
                "Subscription status" TEXT, 
                "Views" INTEGER,
                PRIMARY KEY ("Date", "Subscription status")
            );
        
            CREATE TABLE IF NOT EXISTS subscription_status_table_data (
                "Subscription status" TEXT, 
                "Views" INTEGER, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT,
                PRIMARY KEY ("Subscription status")
            );
        
            CREATE TABLE IF NOT EXISTS content_type_chart_data (
                "Date" TEXT, 
                "Content type" TEXT, 
                "Views" INTEGER,
                PRIMARY KEY ("Date", "Content type")
            );
        
            CREATE TABLE IF NOT EXISTS content_type_table_data (
                "Content type" TEXT, 
                "Views" INTEGER, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT,
                PRIMARY KEY ("Content type")
            );
        
            CREATE TABLE IF NOT EXISTS traffic_source_chart_data (
                "Date" TEXT, 
                "Traffic source" TEXT, 
                "Views" INTEGER,
                PRIMARY KEY ("Date", "Traffic source")
            );
        
            CREATE TABLE IF NOT EXISTS traffic_source_table_data (
                "Traffic source" TEXT, 
                "Views" DOUBLE PRECISION, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT, 
                "Impressions" DOUBLE PRECISION, 
                "Impressions click-through rate (%)" DOUBLE PRECISION,
                PRIMARY KEY ("Traffic source")
            );
        
            CREATE TABLE IF NOT EXISTS viewership_by_date_table_data (
                "Date" TEXT, 
                "Views" DOUBLE PRECISION, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT,
                PRIMARY KEY ("Date")
            );
        
            CREATE TABLE IF NOT EXISTS subtitles_and_cc_chart_data (
                "Date" TEXT, 
                "Subtitles and CC" TEXT, 
                "Views" INTEGER,
                PRIMARY KEY ("Date", "Subtitles and CC")
            );
        
            CREATE TABLE IF NOT EXISTS subtitles_and_cc_table_data (
                "Subtitles and CC" TEXT, 
                "Views" INTEGER, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT,
                PRIMARY KEY ("Subtitles and CC")
            );
        
            CREATE TABLE IF NOT EXISTS operating_system_chart_data (
                "Date" TEXT, 
                "Operating system" TEXT, 
                "Views" INTEGER,
                PRIMARY KEY ("Date", "Operating system")
            );
        
            CREATE TABLE IF NOT EXISTS operating_system_table_data (
                "Operating system" TEXT, 
                "Views" INTEGER, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT,
                PRIMARY KEY ("Operating system")
            );
        
            CREATE TABLE IF NOT EXISTS viewer_age_table_data (
                "Viewer age" TEXT, 
                "Views (%)" DOUBLE PRECISION, 
                "Average view duration" TEXT, 
                "Average percentage viewed (%)" DOUBLE PRECISION, 
                "Watch time (hours) (%)" DOUBLE PRECISION,
                PRIMARY KEY ("Viewer age")
            );
        
            CREATE TABLE IF NOT EXISTS device_type_chart_data (
                "Date" TEXT, 
                "Device type" TEXT, 
                "Views" INTEGER,
                PRIMARY KEY ("Date", "Device type")
            );
        
            CREATE TABLE IF NOT EXISTS device_type_table_data (
                "Device type" TEXT, 
                "Views" INTEGER, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT,
                PRIMARY KEY ("Device type")
            );
        
            CREATE TABLE IF NOT EXISTS sharing_service_chart_data (
                "Date" TEXT, 
                "Sharing service" TEXT, 
                "Shares" INTEGER,
                PRIMARY KEY ("Date", "Sharing service")
            );
        
            CREATE TABLE IF NOT EXISTS sharing_service_table_data (
                "Sharing service" TEXT, 
                "Shares" INTEGER,
                PRIMARY KEY ("Sharing service")
            );
        
            CREATE TABLE IF NOT EXISTS cities_chart_data (
                "Date" TEXT, 
                "Cities" TEXT, 
                "City name" TEXT, 
                "Views" INTEGER,
                PRIMARY KEY ("Date", "Cities")
            );
        
            CREATE TABLE IF NOT EXISTS cities_table_data (
                "Cities" TEXT, 
                "City name" TEXT, 
                "Geography" TEXT, 
                "Geography.1" TEXT, 
                "Views" INTEGER, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT,
                PRIMARY KEY ("Cities")
            );
        
            CREATE TABLE IF NOT EXISTS geography_chart_data (
                "Date" TEXT, 
                "Geography" TEXT, 
                "Views" INTEGER,
                PRIMARY KEY ("Date", "Geography")
            );
        
            CREATE TABLE IF NOT EXISTS geography_table_data (
                "Geography" TEXT, 
                "Views" INTEGER, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT,
                PRIMARY KEY ("Geography")
            );
        
            CREATE TABLE IF NOT EXISTS viewer_gender_table_data (
                "Viewer gender" TEXT, 
                "Views (%)" DOUBLE PRECISION, 
                "Average view duration" TEXT, 
                "Average percentage viewed (%)" DOUBLE PRECISION, 
                "Watch time (hours) (%)" DOUBLE PRECISION,
                PRIMARY KEY ("Viewer gender")
            );
        
            CREATE TABLE IF NOT EXISTS new_and_returning_viewers_chart_data (
                "Date" TEXT, 
                "New and returning viewers" TEXT, 
                "Views" INTEGER,
                PRIMARY KEY ("Date", "New and returning viewers")
            );
        
            CREATE TABLE IF NOT EXISTS new_and_returning_viewers_table_data (
                "New and returning viewers" TEXT, 
                "Views" INTEGER, 
                "Watch time (hours)" DOUBLE PRECISION, 
                "Average view duration" TEXT,
                PRIMARY KEY ("New and returning viewers")
            );
        
            CREATE TABLE IF NOT EXISTS subscription_source_chart_data (
                "Date" TEXT, 
                "Subscription source" TEXT, 
                "Subscribers" INTEGER,
                PRIMARY KEY ("Date", "Subscription source")
            );
        
            CREATE TABLE IF NOT EXISTS subscription_source_table_data (
                "Subscription source" TEXT, 
                "Subscribers" INTEGER, 
                "Subscribers gained" INTEGER, 
                "Subscribers lost" INTEGER,
                PRIMARY KEY ("Subscription source")
            );
        
        