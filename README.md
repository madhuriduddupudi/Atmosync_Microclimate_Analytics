# AtmoSync — Microclimate Arbitrage Analytics

A real-time telemetry analytics pipeline for monitoring microclimate conditions and identifying potential spoilage-arbitrage situations in temperature-sensitive operations.

## Overview

AtmoSync processes simulated container telemetry through a real-time data pipeline, transforms raw sensor data into analytics-ready datasets, and presents operational insights through an interactive Power BI dashboard.

The project demonstrates an end-to-end workflow covering **real-time data ingestion, cloud data warehousing, data transformation, analytics modeling, alerting, and business intelligence**.

## System Architecture

```text
Python Telemetry Generator
          ↓
     Apache Kafka
          ↓
     Kafka Connect
          ↓
   Snowflake Raw Layer
          ↓
        dbt
   ┌──────┴──────┐
   ↓             ↓
Staging     Analytics Models
                 ↓
            Power BI
                 ↓
        Business Insights
```

## Key Features

* Real-time telemetry event generation using Python
* Streaming data ingestion using Apache Kafka
* Raw telemetry storage in Snowflake
* Data transformation and modeling using dbt
* SQL-based analytical logic for operational classification
* Spoilage category and priority-level identification
* Automated email alerting for critical conditions
* Interactive Power BI dashboard for monitoring and analysis
* Docker-based environment for supporting services

## Tech Stack

**Languages & Analytics:** Python, SQL
**Streaming:** Apache Kafka, Kafka Connect
**Data Warehouse:** Snowflake
**Transformation:** dbt
**Visualization:** Power BI
**Infrastructure:** Docker
**Development:** VS Code, Git, GitHub

## Data Pipeline

1. `telemetry_generator.py` generates simulated container telemetry.
2. Telemetry events are published to the Kafka topic.
3. Kafka Connect transfers streaming data into Snowflake.
4. Raw telemetry is stored in the Snowflake raw layer.
5. dbt staging models clean and standardize the data.
6. dbt analytical models derive business metrics and classifications.
7. Power BI connects to the analytics layer for visualization.
8. `email_alert.py` supports automated alerts for critical telemetry conditions.

## Analytics

The dbt analytics layer derives operational indicators such as:

* Priority Level
* Spoilage Category
* Temperature and environmental condition monitoring
* Spoilage Arbitrage classification
* Container-level operational insights

These metrics help identify potentially critical conditions requiring operational attention.

## Repository Structure

```text
AtmoSync/
│
├── atmosync_dbt/          # dbt project and transformation models
├── consumer/              # Streaming/data consumption components
├── data/                  # Project data and sample telemetry
├── sql/                   # SQL scripts and database queries
├── .gitignore
├── Atmosync_dashboard.pbix # Power BI dashboard
├── docker-compose.yml     # Docker service configuration
├── dockerfile             # Docker image configuration
├── email_alert.py         # Automated alerting logic
├── telemetry_generator.py # Telemetry event generator
└── README.md
```

## Business Value

AtmoSync demonstrates how real-time telemetry can be converted into actionable analytics by combining streaming infrastructure, cloud data warehousing, transformation models, and BI dashboards.

The solution can help operations teams **monitor environmental conditions, identify high-risk containers, prioritize potential spoilage events, and support faster operational decision-making**.

## Project Outcome

Built an end-to-end real-time analytics pipeline integrating **Python → Kafka → Snowflake → dbt → Power BI**, with automated alerting and business-focused telemetry analytics.

## Author

**Madhuri Duddupudi**

B.Tech — Artificial Intelligence & Machine Learning
