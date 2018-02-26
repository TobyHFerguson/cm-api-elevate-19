package com.cloudera.elevate.cmapidemo.more;

import com.cloudera.api.ClouderaManagerClientBuilder;
import com.cloudera.api.DataView;
import com.cloudera.api.model.ApiCluster;
import com.cloudera.api.model.ApiClusterList;
import com.cloudera.api.model.ApiHostRef;
import com.cloudera.api.model.ApiHostRefList;
import com.cloudera.api.v17.ClustersResourceV17;
import com.cloudera.api.v17.RootResourceV17;

/**
 * Simple example of using the CM API from Java.
 * This gets the list of clusters managed by CM, and then displays
 * the list of hosts for each cluster.
 */
public class GetHosts {

	public static void main(String[] args) {
		RootResourceV17 apiRoot = new ClouderaManagerClientBuilder()
				.withHost("localhost")
				.withUsernamePassword("cloudera", "cloudera").build()
				.getRootV17();

		ClustersResourceV17 clusters = apiRoot.getClustersResource();

		ApiClusterList clusterList = clusters.readClusters(DataView.SUMMARY);
		for (int i = 0; i < clusterList.size(); i++) {
			ApiCluster cluster = clusterList.get(i);

			String clusterName = cluster.getName();
			String info = String.format("Cluster #%d is called '%s'", i, clusterName);
			System.out.println(info);

			ApiHostRefList hostList = clusters.listHosts(clusterName);
			for (int j = 0; j < args.length; j++) {
				ApiHostRef host = hostList.get(j);
				String id = host.getHostId();
				System.out.println("ID " + id);
			}
		}
	}
}
