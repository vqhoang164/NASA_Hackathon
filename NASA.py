import numpy as np
import matplotlib.pyplot as plt
import pyrebase

config = {
    "apiKey":"AIzaSyB7WT4290ZT62HKnTblU_LM0QVi060Rnnk",
    "authDomain": "iot-nasa.firebaseapp.com",
    "databaseURL": "https://iot-nasa-default-rtdb.firebaseio.com/",
    "storageBucket": "iot-nasa.appspot.com"
    }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

x = [0, 1, 2, 4]
y = [0, 0, 0, 0]
z = [0, 2, 3, 3]

hand_length = np.sqrt(np.square(x[3]-x[2])+np.square(y[3]-y[2])+np.square(z[3]-z[2]))

while True:
    try:
        plt.ion()
        r1 = np.sqrt(x[1] * x[1] + y[1] * y[1] + z[1] * z[1])
        r2 = np.sqrt(x[2] * x[2] + y[2] * y[2] + z[2] * z[2])
        r3 = np.sqrt(x[3] * x[3] + y[3] * y[3] + z[3] * z[3])

        shoulder_deg = db.child("Shoulder").get().val()
        t1 = np.deg2rad(shoulder_deg*10)
        t1 = t1 + np.arctan(y[1] / x[1])
        #calculate elbow angle
        elbow_deg = db.child("Elbow").get().val()
        t2 = np.deg2rad(elbow_deg * 10)
        dis_z3 = hand_length * np.sin(t2)

        p1 = np.arccos(z[1] / r1)
        p2 = np.arccos(z[2] / r2)
        p3 = np.arccos(z[3] / r3)

        x2 = [x[0], r1 * np.cos(t1) * np.sin(p1), r2 * np.cos(t1) * np.sin(p2), r3 * np.cos(t1) * np.sin(p3)]
        y2 = [y[0], r1 * np.sin(t1) * np.sin(p1), r2 * np.sin(t1) * np.sin(p2), r3 * np.sin(t1) * np.sin(p3)]
        z2 = [z[0], z[1], z[2], z[3]+dis_z3]

        #plt.figure(figsize=(10, 10))
        ax = plt.axes(projection='3d')
        ax.plot3D(x2, y2, z2, 'green', marker='o')
        ax.set_xlim3d([-5, 5])
        ax.set_ylim3d([-3, 3])
        ax.set_zlim3d([-0, 4])

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.draw()
        plt.pause(0.5)
        plt.clf()

    except KeyboardInterrupt:
        exit(0)


