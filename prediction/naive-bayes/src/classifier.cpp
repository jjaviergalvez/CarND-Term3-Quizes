#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>
#include "classifier.h"
#include <numeric>

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

	mean_.resize(k, vector<double>(n)); // n col and k row
	var_.resize(k, vector<double>(n)); // n col and k row

	// Separate data by class
	// separated[0] will contain all the instances for left turn
	// separated[1] will contain all the instances for keep going
	// separated[2] will contain all the instances for right turn
	vector< vector< vector<double >>> separated (k);
	for(int i = 0; i < m; i++)
		for(int j = 0; j < k; j++)
			if(labels[i] == possible_labels[j])
    			separated[j].push_back(data[i]);

    // Calculate Mean
    for(int ik = 0; ik < k; ik++){
    	for(int in = 0; in < n; in++){
			for(int im = 0; im < separated[ik].size(); im++){
				mean_[ik][in] += separated[ik][im][in];
			}
			mean_[ik][in] /= separated[ik].size();
		}
    }

    // Calculate the variance
    for(int ik = 0; ik < k; ik++){
    	for(int in = 0; in < n; in++){
			for(int im = 0; im < separated[ik].size(); im++){
				var_[ik][in] += pow(separated[ik][im][in] - mean_[ik][in], 2);
			}
			var_[ik][in] /= separated[ik].size();
		}
    }

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


	vector<double> posterior(possible_labels.size());

	// calculate the posteriori for belong to each class
	for(int i = 0; i < possible_labels.size(); i++){
		posterior[i] = 0.33;
		for(int j = 0; j < sample.size(); j++){
			double x = sample[j];
			double gauss = exp(-pow(x - mean_[i][j], 2) / (2*var_[i][j])) / sqrt(2*M_PI*var_[i][j]);
			posterior[i] *= gauss;
		}
	}

	// take the maximum
	double max = 0;
	int r = 0;
	for(int i = 0; i < possible_labels.size(); i++){
		if(posterior[i] > max){
			max = posterior[i];
			r = i;
		}
	}

	return this->possible_labels[r];

}