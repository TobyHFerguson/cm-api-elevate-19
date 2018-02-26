#!/usr/bin/env python

from cm_api.api_client import ApiResource

cm_host = "localhost"
api = ApiResource(cm_host, username="cloudera", password="cloudera", version=17)

c = api.get_cluster('Cloudera Quickstart')
hosts = c.list_hosts()
for host in hosts:
  print "Host=%s" % host.hostId

# The 'host' variable is of type cm_api.endpoints.types.ApiHostRef, which
# is documented here:
# http://cloudera.github.io/cm_api/epydoc/5.12.0/cm_api.endpoints.types.ApiHostRef-class.html
