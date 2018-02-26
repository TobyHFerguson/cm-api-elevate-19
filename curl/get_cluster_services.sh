#!/bin/sh

# This returns a JSON response containing the list of services installed
# on a specific cluster, as per the documentation here:
#
# https://cloudera.github.io/cm_api/apidocs/v17/path__clusters_-clusterName-_services.html

curl -u 'cloudera:cloudera' 'http://localhost:7180/api/v17/clusters/Cloudera%20Quickstart/services'

