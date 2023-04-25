# Vehicle-Motion-Prediction-in-Autonomous-Vehicles-using-an-FCN-based-Deep-Learning-Model

This project is focused on developing a Motion Prediction algorithm for Automated Vehicles. It involved analyzing a dataset consisting of vehicle trajectories recorded by a drone at various road intersections in Germany. The objective was to create a deep learning model based on this dataset, capable of accurately predicting vehicle motion while minimizing the prediction error.

Details regarding the Dataset:
The dataset is provided by https://www.ind-dataset.com/#. The inD dataset is a new dataset of naturalistic vehicle trajectories recorded at German intersections. Typical drawbacks of traditional traffic data collection methods, such as occlusions, are eliminated by using a drone. Traffic was recorded at four different locations. The trajectory for each road user and its type is extracted. The dataset includes the parameters recorded for Vehicles (car, truck, bus), Pedestrians and Bicyclists such as x and y co-cordinates for velocity and acceleration, heading direction, longitudinal and lateral accelerations and velocities, no. of tracks, no. of vehicles, no. of VRUS, frame and track IDs, duration, speed limits etc. 

The source code can be found in main.ipynb. However, to get an overview and gain a deeper sense of the project, please open the Presentation and Report.pdf files.

Project Objective

![project_focus](https://user-images.githubusercontent.com/18647382/234331087-3f650744-ccf3-49e7-87b5-5d7c398e41f4.png)

Fully convolutional Neural network model (FCN)

![NN](https://user-images.githubusercontent.com/18647382/234331408-c28a3af0-db2a-4682-9239-72a1462cde35.png)

Train test split 

![Train_test_split](https://user-images.githubusercontent.com/18647382/234331639-0fcdfaa8-90fd-4247-bcd0-46a30215c380.png)

Model validation with ensuring no overfitting and underfitting

![model validation](https://user-images.githubusercontent.com/18647382/234332376-3aa29286-e1da-4e27-ae37-9aa65f284553.png)

Hyperparameter Optimization using Random Search

![HPO](https://user-images.githubusercontent.com/18647382/234332538-c0fc2bf3-9758-4dc1-8d72-38db3c709c52.png)


