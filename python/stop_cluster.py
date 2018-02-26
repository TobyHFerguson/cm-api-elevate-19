#!/usr/bin/env python

# This example stops the QuickStart VM cluster. Before running it, 
# make sure that the cluster is started down, and then go to the main
# page in CM (http://quickstart.cloudera:7180/cmf/home). The call is 
# asynchronous, so the command exits immediately after you run it. The 
# CM home page will refresh periodically, so you'll see services stopping 
# (it took about 45 seconds for the shutdown to complete on the VM).
# Be sure to notice after you run it that the "All Recent Commands" 
# item begins showing a "1" indicator while the shutdown is in progress, 
# and this disappears once the shutdown is complete.

from cm_api.api_client import ApiResource

cm_host = "localhost"
api = ApiResource(cm_host, username="cloudera", password="cloudera", version=17)

c = api.get_cluster('Cloudera Quickstart')
c.stop()
