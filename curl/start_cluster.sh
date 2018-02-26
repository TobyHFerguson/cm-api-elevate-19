#!/bin/sh

# Starts the named cluster (in this case, one named "Cloudera Quickstart")

curl -u 'cloudera:cloudera' 'http://localhost:7180/api/v17/clusters/Cloudera%20Quickstart/commands/start'
