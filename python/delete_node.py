#!/usr/bin/env python

##Delete a Node

from cm_api.api_client import ApiResource
from cm_api.endpoints.cms import ClouderaManager

CM_HOST = "localhost"
CM_USERNAME = "cloudera"
CM_PASSWD = "cloudera "
CM_PORT = 7180
CLUSTER_NAME = "Cluster 1"
HOST_NAME = ""

api_handle = ApiResource(CM_HOST,CM_PORT,CM_USERNAME,CM_PASSWD,version=16) #Get the cm api resource

cluster = api_handle.get_cluster(CLUSTER_NAME)  #Get Cluster by name

cms = CLouderaManager(api_handle) #Get Cloudera Manager handle

#Decommissioning Hosts and Stopping the Roles

hosts = []
hosts.append(HOST_NAME)

cms.hosts_decommission(hosts)

#Delete the Node (Remove the Roles after Decommissioning)

api_handle.delete_host(HOST_NAME)