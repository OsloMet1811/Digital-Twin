import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def main():
	csv_data = np.genfromtxt('test1/_slash_vrpn_client_node_slash_Drone_A_slash_pose.csv', delimiter=',')

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	cm = plt.get_cmap("RdYlBu")
	col = []

	arr_len = len(csv_data[1:, 9])

	#for i in xrange(arr_len):
	#	col.append(float(i)/(arr_len))
	col = [cm(float(i)/(arr_len)) for i in xrange(arr_len)]
	#print col

	ax.scatter(csv_data[1:, 9] , csv_data[1:, 10] , csv_data[1:, 11], c=col, marker="x")
	ax.scatter(0, 0, 0.5, marker="o", color="r", s=100)


	ax.set_xlim(-0.5, 0.5)
	ax.set_ylim(-0.5, 0.5)
	ax.set_zlim(0, 1)
	ax.set_xlabel("x-axis [m]")
	ax.set_ylabel("y-axis [m]")
	ax.set_zlabel("z-axis [m]") 
	ax.set_title("Position of drone")

	plt.show()


if __name__ == "__main__":
	main()