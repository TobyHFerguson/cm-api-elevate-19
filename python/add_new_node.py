#!/usr/bin/env python

##Adding a Node

from cm_api.api_client import ApiResource
from cm_api.endpoints.cms import ClouderaManager

CM_HOST = "localhost"
CM_USERNAME = "cloudera"
CM_PASSWD = "cloudera"
CLUSTER_NAME = "Cluster 1"
CM_PORT = 7180
HOST_NAME = ""


api_handle = ApiResource(CM_HOST,CM_PORT,CM_USERNAME,CM_PASSWD,version=16) #Get the cm api resource

cluster = api_handle.get_cluster(CLUSTER_NAME)  #Get Cluster by name


#Adding the New Host to the Cluster
newHosts = ["",""]
hostlist = []
for hostName in api.get_all_hosts():
        if hostName.hostname in newHosts:
                hostlist = api.get_host(hostName.hostId)

addHost = cluster.add_hosts(hostlist)


#Adding Roles on the Hosts using Templates
applyTemplate = cluster.get_host_template(TEMPLATE_NAME).apply_host_template(hostlist,'TRUE')
