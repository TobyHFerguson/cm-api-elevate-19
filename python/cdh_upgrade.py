#!/usr/bin/env python

##Cluster Upgrade

from cm_api.api_client import ApiResource
from cm_api.endpoints.cms import ClouderaManager

CM_HOST = "nightly59-1.gce.cloudera.com"
CM_USERNAME = "admin"
CM_PASSWD = "admin"
CM_PORT = 7180
CLUSTER_NAME = "Cluster 1"
PARCEL_VERSION = "5.10.0-1.cdh5.10.0.p0.41"

api_handle = ApiResource(CM_HOST,CM_PORT,CM_USERNAME,CM_PASSWD,version=16) #Get the cm api resource

cluster = api_handle.get_cluster(CLUSTER_NAME)

upgrade_command = cluster.upgrade_cdh(deploy_client_config=True, 
										start_all_services=True, 
										cdh_parcel_version=PARCEL_VERSION, 
										cdh_package_version=None, 
										rolling_restart=False, 
										slave_batch_size=None, 
										sleep_seconds=None, 
										slave_fail_count_threshold=None)