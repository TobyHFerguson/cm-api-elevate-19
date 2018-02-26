#!/bin/sh

# This returns information about a specific cluster, as per the
# documentation here:
#
# https://cloudera.github.io/cm_api/apidocs/v17/path__clusters_-clusterName-.html

curl -u 'cloudera:cloudera' 'http://localhost:7180/api/v17/clusters/Cloudera%20Quickstart'

