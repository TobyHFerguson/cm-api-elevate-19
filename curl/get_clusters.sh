#!/bin/sh

# This is one of the most basic calls you could make with CM API. It returns 
# some JSON-formatted information about all clusters managed by this instance
# of Cloudera Manager.
#
# Doc: https://cloudera.github.io/cm_api/apidocs/v17/path__clusters.html
#
# When run from the QuickStart VM, the JSON response will contain information
# for exactly one cluster, which contains the following tuple:
#
#     "name" : "Cloudera QuickStart"
#
# This value can be used (after URL-encoding the value to replace the space 
# with %20) to construct the URL for REST calls that return more specific
# information about the cluster, such as a list of services or hosts.
# 
# The -u 'cloudera:cloudera' provides the authentication credentials to use
# (username, colon, password). Obviously, a local user could see these values
# in the process since we're specifying them on the command line, and a user
# who has access to our network could capture them since we're not using TLS.


curl -u 'cloudera:cloudera' 'http://localhost:7180/api/v17/clusters'
