# AtmoSync — Microclimate Arbitrage Analytics

AtmoSync is an end-to-end **real-time telemetry analytics pipeline** designed to monitor container microclimate conditions, identify potential spoilage risks, prioritize critical events, and trigger automated email alerts.

The project demonstrates a complete data workflow from **real-time event generation and streaming to cloud storage, transformation, analytics, visualization, and alerting**.

## System Architecture

```text
                    ┌─────────────────────────┐
                    │  Python Telemetry       │
                    │      Generator          │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Apache Kafka        │
                    │   Real-time Streaming    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Kafka Connect       │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       Snowflake         │
                    │       Raw Layer         │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │          dbt            │
                    │ Staging + Analytics     │
                    └────────────┬────────────┘
                                 │
                         ┌───────┴────────┐
                         ▼                ▼
                ┌────────────────┐  ┌─────────────────┐
                │    Power BI    │  │  Email Alerts   │
                │   Dashboard    │  │ Critical Events │
                └────────────────┘  └─────────────────┘
```

## Key Features

* Real-time container telemetry generation using Python
* Event streaming using Apache Kafka
* Kafka Connect integration for data ingestion
* Raw telemetry storage in Snowflake
* Data cleaning and transformation using dbt
* Analytical models for operational insights
* Priority-level classification of telemetry conditions
* Spoilage category classification
* Spoilage arbitrage identification
* Interactive Power BI dashboard
* Automated email alerts for critical telemetry conditions
* Docker-based project environment

## Data Pipeline

1. **Telemetry Generation**
   `telemetry_generator.py` generates simulated container telemetry containing environmental and operational measurements.

2. **Real-Time Streaming**
   Generated events are published to an Apache Kafka topic for real-time processing.

3. **Data Ingestion**
   Kafka Connect transfers streaming telemetry into the Snowflake raw data layer.

4. **Data Transformation**
   dbt models clean, structure, and transform raw telemetry into analytics-ready datasets.

5. **Analytics & Classification**
   Analytical models derive business-oriented metrics such as:

   * Priority Level
   * Spoilage Category
   * Spoilage Arbitrage
   * Container condition indicators

6. **Business Intelligence**
   Power BI consumes the analytics layer and provides interactive dashboards with KPIs, filters, and visual analysis.

7. **Automated Alerts**
   `email_alert.py` evaluates critical telemetry conditions and supports automated email notifications so that high-priority events can be identified without relying only on dashboard monitoring.

## Analytics Layer

The dbt analytics layer converts raw telemetry into meaningful operational information.

Key analytical outputs include:

| Metric             | Purpose                                           |
| ------------------ | ------------------------------------------------- |
| Priority Level     | Identifies the urgency of a telemetry condition   |
| Spoilage Category  | Classifies potential spoilage risk                |
| Spoilage Arbitrage | Identifies potential arbitrage-related conditions |
| Container Metrics  | Provides container-level operational visibility   |

## Power BI Dashboard

The Power BI dashboard provides an interactive view of the processed telemetry data.

### Dashboard Capabilities

* KPI monitoring
* Container-level analysis
* Telemetry condition monitoring
* Priority-level analysis
* Spoilage classification
* Interactive filtering and slicers
* Operational trend analysis

## Email Alerting

AtmoSync includes an automated alerting component through `email_alert.py`.

The alerting layer is designed to notify relevant users when telemetry conditions meet defined critical criteria.

```text
Telemetry Data
      ↓
Critical Condition Detected
      ↓
Alert Logic
      ↓
Email Notification
```

This extends the system from **analytics and visualization to proactive operational monitoring**.

## Technology Stack

**Programming:** Python
**Database & Warehouse:** Snowflake
**Streaming:** Apache Kafka, Kafka Connect
**Transformation:** dbt, SQL
**Visualization:** Power BI
**Alerting:** Python Email Alerting
**Containerization:** Docker
**Version Control:** Git, GitHub

## Repository Structure

```text
AtmoSync/
│
├── atmosync_dbt/             # dbt project and transformation models
│   ├── models/
│   └── ...
│
├── consumer/                 # Streaming/data consumption components
│
├── data/                     # Telemetry/sample data
│
├── sql/                      # SQL scripts and queries
│
├── .gitignore
├── Atmosync_dashboard.pbix   # Power BI dashboard
├── docker-compose.yml        # Docker service configuration
├── dockerfile                # Docker image configuration
├── email_alert.py            # Automated email alerting
├── telemetry_generator.py    # Real-time telemetry generator
└── README.md
```

## Project Outcome

Built an end-to-end real-time analytics solution integrating:

**Python → Kafka → Kafka Connect → Snowflake → dbt → Power BI + Email Alerts**

The project demonstrates practical experience with **real-time data pipelines, cloud data warehousing, SQL-based transformation, analytics engineering, business intelligence, and automated alerting**.

## Business Value

AtmoSync helps transform raw real-time telemetry into actionable operational insights by combining streaming data infrastructure, cloud analytics, visualization, and proactive alerting.

The solution can help operations teams:

* Monitor container conditions
* Identify high-risk situations
* Prioritize critical events
* Detect potential spoilage risks
* Receive automated notifications
* Support faster operational decision-making

## Author

**Madhuri Duddupudi**

Data Analytics | Python | SQL | Power BI | Data Visualization
