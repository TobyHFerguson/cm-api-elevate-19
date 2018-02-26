#!/usr/bin/env python

##Adding a Service

from cm_api.api_client import ApiResource
from cm_api.endpoints.cms import ClouderaManager

CM_HOST = "localhost"
CM_USERNAME = "cloudera"
CM_PASSWD = "cloudera"
CLUSTER_NAME = "Cluster 1"
CM_PORT = 7180
flumeService=""
i=0

api_handle = ApiResource(CM_HOST,CM_PORT,CM_USERNAME,CM_PASSWD,version=10) #Get the cm api resource

cluster = api_handle.get_cluster(CLUSTER_NAME)

#Create the Service
service = cluster.create_service("FLUME-1","FLUME")

#Add the role instances to hosts

for service in cluster.get_all_services():
		if service.type == "FLUME":
			flumeService = service
			for host in api_handle.get_all_hosts():
				i=i+1
				newFlumeAgent=flumeService.create_role("FLUME-AGENT-"+str(i),"AGENT",host.hostId)
			flumeService.restart
