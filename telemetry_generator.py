from kafka import KafkaProducer
import json
import csv
import os
import random
import time
from datetime import datetime


# ---------------------------------------------------
# Kafka Producer Configuration
# ---------------------------------------------------

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

TOPIC_NAME = "container_telemetry"


# ---------------------------------------------------
# Container Information
# ---------------------------------------------------

containers = [
    {
        "container_id": "CONT_001",
        "cargo_type": "Vaccines",
        "origin": "Hyderabad",
        "destination": "Chennai"
    },
    {
        "container_id": "CONT_002",
        "cargo_type": "Seafood",
        "origin": "Vizag",
        "destination": "Mumbai"
    },
    {
        "container_id": "CONT_003",
        "cargo_type": "Dairy",
        "origin": "Bengaluru",
        "destination": "Pune"
    },
    {
        "container_id": "CONT_004",
        "cargo_type": "Fruits",
        "origin": "Nagpur",
        "destination": "Delhi"
    }
]


file_name = "telemetry_data.csv"


# ---------------------------------------------------
# Create CSV with Headers
# ---------------------------------------------------

if not os.path.exists(file_name):

    with open(file_name, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Timestamp",
            "Container_ID",
            "Cargo_Type",
            "Origin",
            "Destination",
            "Temperature_C",
            "Humidity_Percent",
            "Vibration_Level",
            "Distance_Remaining_km",
            "Spoilage_Risk",
            "Recommended_Action",
            "Alert_Status"
        ])


# ---------------------------------------------------
# Generate Real-Time Telemetry
# ---------------------------------------------------

while True:

    container = random.choice(containers)

    cargo = container["cargo_type"]


    # Temperature based on cargo type

    if cargo == "Vaccines":

        temperature = round(random.uniform(2, 8), 2)

    elif cargo == "Seafood":

        temperature = round(random.uniform(-2, 4), 2)

    elif cargo == "Dairy":

        temperature = round(random.uniform(1, 5), 2)

    else:

        temperature = round(random.uniform(4, 12), 2)


    humidity = round(random.uniform(60, 90), 2)

    vibration = round(random.uniform(0.01, 0.10), 3)

    distance_remaining = round(random.uniform(20, 1500), 2)


    # ---------------------------------------------------
    # Business Rules
    # ---------------------------------------------------

    if temperature > 8 or vibration > 0.08:

        spoilage_risk = "High"
        recommended_action = "Immediate Inspection"
        alert_status = "Critical"


    elif temperature > 5 or vibration > 0.05:

        spoilage_risk = "Medium"
        recommended_action = "Check Cooling System"
        alert_status = "Warning"


    else:

        spoilage_risk = "Low"
        recommended_action = "Continue Monitoring"
        alert_status = "Normal"



    # ---------------------------------------------------
    # Create Telemetry JSON Message
    # ---------------------------------------------------

    telemetry_data = {

        "timestamp": str(datetime.now()),

        "container_id": container["container_id"],

        "cargo_type": cargo,

        "origin": container["origin"],

        "destination": container["destination"],

        "temperature": temperature,

        "humidity": humidity,

        "vibration": vibration,

        "distance_remaining": distance_remaining,

        "spoilage_risk": spoilage_risk,

        "recommended_action": recommended_action,

        "alert_status": alert_status

    }


    # ---------------------------------------------------
    # Send Data To Kafka
    # ---------------------------------------------------

    producer.send(
        TOPIC_NAME,
        value=telemetry_data
    )

    producer.flush()



    # ---------------------------------------------------
    # Save Data To CSV
    # ---------------------------------------------------

    with open(file_name, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([

            datetime.now(),

            container["container_id"],

            cargo,

            container["origin"],

            container["destination"],

            temperature,

            humidity,

            vibration,

            distance_remaining,

            spoilage_risk,

            recommended_action,

            alert_status

        ])



    print("Telemetry Sent:", telemetry_data)


    time.sleep(1)