{{ config(materialized='table') }}

WITH telemetry AS (

    SELECT
        CONTAINER_ID,
        CARGO_TYPE,
        TEMPERATURE,
        HUMIDITY,
        VIBRATION,
        ORIGIN,
        DESTINATION,
        ALERT_STATUS,
        RECOMMENDED_ACTION,
        DISTANCE_REMAINING,
        SPOILAGE_RISK,
        TIMESTAMP,

        CASE
            WHEN ALERT_STATUS = 'Critical' THEN 'HIGH PRIORITY'
            WHEN ALERT_STATUS = 'Warning' THEN 'MEDIUM PRIORITY'
            ELSE 'NORMAL'
        END AS PRIORITY_LEVEL,

        CASE
            WHEN SPOILAGE_RISK = 'High' THEN 'AT RISK'
            WHEN SPOILAGE_RISK = 'Medium' THEN 'MONITOR'
            ELSE 'LOW RISK'
        END AS SPOILAGE_CATEGORY,

        CASE
            WHEN SPOILAGE_RISK = 'High' THEN 3
            WHEN SPOILAGE_RISK = 'Medium' THEN 2
            ELSE 1
        END AS RISK_FACTOR

    FROM {{ ref('staging_telemetry') }}

),

scored AS (

    SELECT
        *,
        
        ROUND(
            RISK_FACTOR *
            (1 - DISTANCE_REMAINING / MAX(DISTANCE_REMAINING) OVER ()),
            3
        ) AS SPOILAGE_ARBITRAGE_SCORE

    FROM telemetry

)

SELECT
    CONTAINER_ID,
    CARGO_TYPE,
    TEMPERATURE,
    HUMIDITY,
    VIBRATION,
    ORIGIN,
    DESTINATION,
    ALERT_STATUS,
    RECOMMENDED_ACTION,
    DISTANCE_REMAINING,
    SPOILAGE_RISK,
    TIMESTAMP,
    PRIORITY_LEVEL,
    SPOILAGE_CATEGORY,
    SPOILAGE_ARBITRAGE_SCORE

FROM scored