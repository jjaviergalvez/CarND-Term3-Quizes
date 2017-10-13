import numpy as np
from scipy.linalg import solve
from helpers import Vehicle, show_trajectory
 
A = np.random.random((3, 3))
b = np.random.random(3)

x = solve(A, b)


def JMT(start, end, T):

	si = start[0]
	si_dot = start[1]
	si_double_dot = start[2]

	sf = end[0]
	sf_dot = end[1]
	sf_double_dot = end[2]


	A = [
		 [T**3	, T**4	 , T**5	  ],
		 [3*T**2, 4*T**3 ,  5*T**4],
		 [6*T	, 12*T**2, 20*T**3]
		]

	b = [sf - (si + si_dot*T + 0.5 * si_double_dot * T**2 ), 
		 sf_dot - (si_dot + si_double_dot*T), 
		 sf_double_dot - si_double_dot]

	x = solve(A,b)

	r = np.array([si, si_dot, 0.5*si_double_dot, x[0], x[1], x[2]])

	return r
	#return [si, si_dot, 0.5*si_double_dot, x[0], x[1], x[2]]



def close_enough(poly, target_poly, eps=0.01):
	if len(poly) != len(target_poly):
		print("your solution didn't have the correct number of terms")
		return False
	
	for i in range(len(poly)):
		diff = poly[i]-target_poly[i]
		if(abs(diff) > eps):
			print("at least one of your terms differed from target by more than ", eps )
			return False
	
	return True
	

answers = [[0.0, 10.0, 0.0, 0.0, 0.0, 0.0],[0.0,10.0,0.0,0.0,-0.625,0.3125],[5.0,10.0,1.0,-3.0,0.64,-0.0432]];

# create test cases


tc1 = [[0,10,0], [10,10,0], [1]]

tc2 = [[0,10,0],[20,15,20], [2]]

tc3 = [[5,10,2],[-30,-20,-4], [5]]

tc = [tc1,tc2,tc3]

i = 0;
total_correct = True
for test in tc:
	jmt = JMT(test[0], test[1], test[2][0])
	correct = close_enough(jmt, answers[i])
	total_correct &= correct
	i += 1



if total_correct:
	print("Nice work!")
else:
	print("Try again!")

jmt = JMT(tc1[0], tc1[1], tc1[2][0])
show_trajectory(jmt[0], jmt[1], jmt[2])
	
