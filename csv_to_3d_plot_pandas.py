import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime
from matplotlib import style
style.use('fivethirtyeight')

def csv_to_df():
	df = pd.read_csv('bagfiles/drone_flight_setpoint/_slash_vrpn_client_node_slash_Drone_A_slash_pose.csv')
	df = df[['rosbagTimestamp', 'x', 'y', 'z', 'x.1', 'y.1', 'z.1', 'w']]
	df['rosbagTimestamp'] = pd.to_datetime(df['rosbagTimestamp'], unit='ns')
	df.set_index('rosbagTimestamp', inplace = True)
	df.columns = [['pos_x', 'pos_y', 'pos_z', 'quat_x', 'quat_y', 'quat_z', 'quat_w']]
	return df
	

def main():
	pose_df = csv_to_df()
	pose_df_resampled = pose_df.resample('30L').mean()
	print(pose_df_resampled.head())

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')


	ax.scatter(pose_df_resampled['pos_x'], pose_df_resampled['pos_y'], pose_df_resampled['pos_z'], marker='o', label='position')
	#ax.scatter(pose_df['pos_x'], pose_df['pos_y'], pose_df['pos_z'], marker='.', label='position')
	ax.scatter(0, 0, 0.5, marker="o", c="k", s=100, label='setpoint')

	ax.set_xlim(-0.5, 0.5)
	ax.set_ylim(-0.5, 0.5)
	ax.set_zlim(0, 0.7)
	ax.set_xlabel("x-axis [m]")
	ax.set_ylabel("y-axis [m]")
	ax.set_zlabel("z-axis [m]") 
	ax.set_title("Position of drone")
	plt.legend()
	plt.show()


if __name__ == "__main__":
	main()