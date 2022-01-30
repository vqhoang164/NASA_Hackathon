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

plt.ion()

while True:
    try:

        r1 = np.sqrt(x[1] * x[1] + y[1] * y[1] + z[1] * z[1])
        r2 = np.sqrt(x[2] * x[2] + y[2] * y[2] + z[2] * z[2])
        r3 = np.sqrt(x[3] * x[3] + y[3] * y[3] + z[3] * z[3])

        deg_db = db.child("Shoulder").get()
        shoulder_deg = deg_db.val()
        sd = int(shoulder_deg)
        t1 = np.deg2rad(sd)
        t1 = t1 + np.arctan(y[1] / x[1])

        p1 = np.arccos(z[1] / r1)
        p2 = np.arccos(z[2] / r2)
        p3 = np.arccos(z[3] / r3)

        x2 = [x[0], r1 * np.cos(t1) * np.sin(p1), r2 * np.cos(t1) * np.sin(p2), r3 * np.cos(t1) * np.sin(p3)]
        y2 = [y[0], r1 * np.sin(t1) * np.sin(p1), r2 * np.sin(t1) * np.sin(p2), r3 * np.sin(t1) * np.sin(p3)]
        z2 = z

        #plt.figure(figsize=(10, 10))
        ax = plt.axes(projection='3d')
        ax.plot3D(x2, y2, z2, 'green', marker='o')
        ax.set_xlim3d([-5, 5])
        ax.set_ylim3d([-3, 3])
        ax.set_zlim3d([-0, 4])
        plt.draw()
        plt.pause(1)
        plt.clf()

    except KeyboardInterrupt:
        exit(0)


