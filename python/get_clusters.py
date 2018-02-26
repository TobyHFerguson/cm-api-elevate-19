#!/usr/bin/env python

from cm_api.api_client import ApiResource

# NOTE: I added the version=17 argument below, which wasn't in the example
# on the CM API Python client page from which I copied this code, because
# the version of the Python client libraries use a newer API version [v19]
# than what's available on CM [v17].
cm_host = "localhost"
api = ApiResource(cm_host, username="cloudera", password="cloudera", version=17)

# Get a list of all clusters
for c in api.get_all_clusters():
  print "Name=%s" % c.name
