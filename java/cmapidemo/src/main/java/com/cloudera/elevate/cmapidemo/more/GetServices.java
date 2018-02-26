package com.cloudera.elevate.cmapidemo.more;

import java.util.List;

import com.cloudera.api.ClouderaManagerClientBuilder;
import com.cloudera.api.DataView;
import com.cloudera.api.model.ApiService;
import com.cloudera.api.model.ApiServiceList;
import com.cloudera.api.v17.ClustersResourceV17;
import com.cloudera.api.v17.RootResourceV17;
import com.cloudera.api.v17.ServicesResourceV17;

/**
 * Simple example of using the CM API from Java.
 * This retrieves a list of cluster services.
 */
public class GetServices {

	public static void main(String[] args) {
		RootResourceV17 apiRoot = new ClouderaManagerClientBuilder()
			.withHost("localhost")
			.withUsernamePassword("cloudera", "cloudera")
			.build()
			.getRootV17();
		
		ClustersResourceV17 clusters = apiRoot.getClustersResource();
		ServicesResourceV17 services = clusters.getServicesResource("Cloudera Quickstart");
		
		ApiServiceList serviceListWrapper = services.readServices(DataView.SUMMARY);
		List<ApiService> serviceList = serviceListWrapper.getServices();
		
		for (ApiService service : serviceList) {
			System.out.println(service.getName());
		}
	}
}
