#!/usr/bin/env python

from cm_api.api_client import ApiResource

cm_host = "localhost"
api = ApiResource(cm_host, username="cloudera", password="cloudera", version=17)

c = api.get_cluster('Cloudera Quickstart')
services = c.get_all_services()
for service in services:
  if service.name == 'hbase':  
    cmd = service.stop()
    cmd = cmd.wait()
    print "Successfully stopped HBase? %s" % cmd.success

