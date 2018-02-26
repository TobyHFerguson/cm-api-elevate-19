#!/usr/bin/env python

from cm_api.api_client import ApiResource

cm_host = "localhost"
api = ApiResource(cm_host, username="cloudera", password="cloudera", version=17)

# Get info about a specific cluster by name
# Note that I don't need to urlencode the name, as I did in the REST call made with curl
c = api.get_cluster('Cloudera Quickstart')
print "Name=%s" % c.name

# the 'c' variable is of type cm_api.endpoints.clusters.ApiCluster, 
# which is documented here:
# http://cloudera.github.io/cm_api/epydoc/5.12.0/cm_api.endpoints.clusters.ApiCluster-class.html
