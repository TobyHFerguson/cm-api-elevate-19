        
from cm_api.api_client import ApiResource
from cm_api.endpoints.types import ApiClusterTemplate
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.services import ApiServiceSetupInfo
import json

with open("mgmt.json", 'r') as f:
	cms_config = json.load(f)

with open("cluster_config.json", 'r') as f1:
	cls_config = json.load(f1)

CM_HOST = "cm-api-test-1.vpc.cloudera.com"
CM_USERNAME = "admin"
CM_PASSWD = "admin"
CM_PORT = 7180

api_handle = ApiResource(CM_HOST,CM_PORT,CM_USERNAME,CM_PASSWD,version=17)
cm = api_handle.get_cloudera_manager()
mgmt_setup_info = ApiServiceSetupInfo(name="MGMT", type="MGMT", config={})
mgmt_svc = cm.create_mgmt_service(mgmt_setup_info)

if 'services' in cms_config['mgmt']:
    for svc in cms_config['mgmt']['services']:
     svc_host = "cm-api-test-1.vpc.cloudera.com"
     rolename = "mgmt-%s" % svc['name']
     mgmt_svc.create_role(rolename, svc['name'], svc_host)
     svc_grp = mgmt_svc.get_role_config_group("mgmt-%s-BASE" % svc['name'])
     if 'config' in svc:
                svc_grp.update_config(svc['config'])
     for role in mgmt_svc.get_all_roles():
        if role.roleState != 'STARTED':
            mgmt_svc.role_command_by_name('start', role.name)
        if role.configStalenessStatus == 'STALE':
            mgmt_svc.role_command_by_name('restart', role.name)

cmd = cm.get_service().restart()	

template = ApiClusterTemplate(api_handle).from_json_dict(cls_config, api_handle)
cmd = cm.import_cluster_template(template)
