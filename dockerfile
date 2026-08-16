FROM confluentinc/cp-kafka-connect:latest

USER root

RUN confluent-hub install --no-prompt snowflakeinc/snowflake-kafka-connector:latest

USER appuser