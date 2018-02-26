#!/usr/bin/env python

# This example starts the QuickStart VM cluster. Before running it, 
# make sure that the cluster is shut down, and then go to the main
# page in CM (http://quickstart.cloudera:7180/cmf/home). The command
# exits immediately after you run it, but the CM home page will 
# refresh periodically, so you'll see services starting up (it took
# about two minutes for the startup to complete on the VM).

from cm_api.api_client import ApiResource

cm_host = "localhost"
api = ApiResource(cm_host, username="cloudera", password="cloudera", version=17)

c = api.get_cluster('Cloudera Quickstart')
c.start()
