package com.cloudera.elevate.cmapidemo;

import java.util.List;

import com.cloudera.api.ClouderaManagerClientBuilder;
import com.cloudera.api.DataView;
import com.cloudera.api.model.ApiCluster;
import com.cloudera.api.model.ApiClusterList;
import com.cloudera.api.v17.ClustersResourceV17;
import com.cloudera.api.v17.RootResourceV17;

/**
 * Very basic example of using the CM API from Java.
 * This retrieves the list of clusters managed by a given instance of CM.
 */
public class GetClusterNamesApp {

	public static void main(String[] args) {
        RootResourceV17 apiRoot = new ClouderaManagerClientBuilder()
        	.withHost("cmhost.example.com")
        	.withUsernamePassword("cloudera", "cloudera")
        	.build()
        	.getRootV17();
        
        ClustersResourceV17 clusterResource =  apiRoot.getClustersResource();
        ApiClusterList clusters = clusterResource.readClusters(DataView.SUMMARY);
        List<ApiCluster> actualListOfClusters = clusters.getClusters();
        
        for (ApiCluster cluster : actualListOfClusters) {
        	System.out.println(cluster.getName());			
		}
    }
}
