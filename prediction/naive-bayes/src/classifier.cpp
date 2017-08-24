#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>
#include "classifier.h"

/**
 * Initializes GNB
 */
GNB::GNB() {

}

GNB::~GNB() {}

void GNB::train(vector<vector<double>> data, vector<string> labels)
{

	/*
		Trains the classifier with N data points and labels.

		INPUTS
		data - array of N observations
		  - Each observation is a tuple with 4 values: s, d, 
		    s_dot and d_dot.
		  - Example : [
			  	[3.5, 0.1, 5.9, -0.02],
			  	[8.0, -0.3, 3.0, 2.2],
			  	...
		  	]

		labels - array of N labels
		  - Each label is one of "left", "keep", or "right".
	*/

	int n = data[0].size(); // number of features
	int m = data.size(); // number of instances
	int k = possible_labels.size(); // number of classes

	double mean[3][n]; // to store the means 
	double var[3][n]; // to store the variances

	// Separate data by class
	// separated[0] will contain all the instances for left turn
	// separated[1] will contain all the instances for keep going
	// separated[2] will contain all the instances for right turn
	vector< vector< vector<double >>> separated (k);

	for(int i = 0; i < m; i++)
		for(int j = 0; j < k; j++)
			if(labels[i] == possible_labels[j])
    			separated[j].push_back(data[i]);

    

    cout << "data: " << separated[0][0][3] << endl;
    cout << "data: " << separated[0][1][3] << endl;

    cout << "data: " << separated[1][0][3] << endl;
    cout << "data: " << separated[1][1][3] << endl;

    cout << "data: " << separated[2][0][3] << endl;
    cout << "data: " << separated[2][1][3] << endl;
    	
}

string GNB::predict(vector<double> sample)
{
	/*
		Once trained, this method is called and expected to return 
		a predicted behavior for the given observation.

		INPUTS

		observation - a 4 tuple with s, d, s_dot, d_dot.
		  - Example: [3.5, 0.1, 8.5, -0.2]

		OUTPUT

		A label representing the best guess of the classifier. Can
		be one of "left", "keep" or "right".
		"""
		# TODO - complete this
	*/

	return this->possible_labels[1];

}