double calculate_cost(Vehicle vehicle, vector<Vehicle::Snapshot> trajectory, map<int, vector<vector<int>> > predictions){
	return 0.1;
}

/*
def calculate_cost(vehicle, trajectory, predictions, verbose=False):
	trajectory_data = get_helper_data(vehicle, trajectory, predictions)
	cost = 0.0
	for cf in [
		distance_from_goal_lane,
		inefficiency_cost,
		collision_cost,
		buffer_cost,
		change_lane_cost]:
		new_cost = cf(vehicle, trajectory, predictions, trajectory_data)
		if DEBUG or verbose:
			print "{} has cost {} for lane {}".format(cf.__name__, new_cost, trajectory[-1].lane)
			# pdb.set_trace()
		cost += new_cost
	return cost

	pass
	*/