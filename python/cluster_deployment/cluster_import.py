#!/usr/bin/env python

from cm_api.api_client import ApiResource
from cm_api.endpoints.types import ApiClusterTemplate
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.services import ApiServiceSetupInfo
import json



with open("clsuter_config.json", 'r') as f1:
	clstr_config = json.load(f1)

api = ApiResource("cm_host",7180,cm_user,cm_passwd,version=17)

cm = api.get_cloudera_manager()

template = ApiClusterTemplate(api).from_json_dict(clstr_config, api)
cmd = cm.import_cluster_template(template)
