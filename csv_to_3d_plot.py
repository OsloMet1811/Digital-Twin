import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.nan)

#def csv_to_np(file):
#	data = np.array([])
#
#	with open(file, 'rb') as csvfile:
#		reader = csv.reader(csvfile)
#		for row in reader:
#			data.append(row)
#
#	return data



def main():
	#pos_x = csv_to_np('test.csv')
	#pos_y = csv_to_np('test.csv')
	#pos_z = csv_to_np('test.csv')

	csv_data = np.genfromtxt('test1/_slash_vrpn_client_node_slash_Drone_A_slash_pose.csv', delimiter=',')

	#print csv_data

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	ax.scatter(csv_data[1:, 9] , csv_data[1:, 10] , csv_data[1:, 11], marker="x")
	ax.scatter(0, 0, 0.5, marker="o", color="r", s=100)
	#print "------------"
	#			 row | col
	#print csv_data[1:, 9] 


	ax.set_xlim(-0.5, 0.5)
	ax.set_ylim(-0.5, 0.5)
	ax.set_zlim(0, 1)

	ax.set_xlabel("x-axis [m]")
	ax.set_ylabel("y-axis [m]")
	ax.set_zlabel("z-axis [m]")

	plt.show()


if __name__ == "__main__":
	main()

