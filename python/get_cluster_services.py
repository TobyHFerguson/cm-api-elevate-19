#!/usr/bin/env python

from cm_api.api_client import ApiResource

cm_host = "localhost"
api = ApiResource(cm_host, username="cloudera", password="cloudera", version=17)

c = api.get_cluster('Cloudera Quickstart')
services = c.get_all_services()
for service in services:
  print "Service=%s" % service.name

# The 'service' variable is of type cm_api.endpoints.services.ApiService, which
# is documented here:
# http://cloudera.github.io/cm_api/epydoc/5.12.0/cm_api.endpoints.services.ApiService-class.html
