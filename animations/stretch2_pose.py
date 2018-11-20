# Choregraphe bezier export in Python.
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.76, 1.84, 2.68, 3.24, 3.6, 4.32, 5.04, 5.64, 6.32, 7.12])
keys.append([0.174835, 0.265341, 0.355846, 0.259204, 0.345107, 0.381923, 0.223922, 0.320565, 0.326377, -0.15651])

names.append("HeadYaw")
times.append([0.76, 1.84, 2.68, 3.24, 3.6, 4.32, 5.04, 5.64, 6.32, 7.12])
keys.append([-0.268493, -0.48632, -0.529271, -0.477115, -0.50166, -0.589097, -0.536942, -0.570689, -0.495674, -0.023052])

names.append("LAnklePitch")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 6.2, 7])
keys.append([0.475497, 0.486237, 0.475497, 0.475497, 0.519984, 0.473963, 0.478566, 0.235619, 0.0735901])

names.append("LAnkleRoll")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([-0.440216, -0.394197, -0.440216, -0.440216, -0.401866, -0.437147, -0.437147, -0.107338])

names.append("LElbowRoll")
times.append([0.68, 1.76, 2.6, 3.16, 3.52, 4.24, 4.96, 5.56, 7.04])
keys.append([-1.21642, -0.424876, -0.378857, -0.463226, -0.458624, -0.406468, -0.427944, -0.42641, -0.42641])

names.append("LElbowYaw")
times.append([0.68, 1.76, 2.6, 3.16, 3.52, 4.24, 4.96, 5.56, 7.04])
keys.append([-0.986404, -1.34229, -1.35303, -1.33155, -1.32695, -1.34536, -1.32235, -1.23491, -1.18736])

names.append("LHand")
times.append([0.68, 1.76, 2.6, 3.16, 3.52, 4.24, 4.96, 5.56, 7.04])
keys.append([0.302, 0.5, 0.4988, 0.4988, 0.498, 0.4988, 0.4988, 0.4992, 0.3028])

names.append("LHipPitch")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([0.030722, -0.032172, 0.032256, 0.032256, -0.0705221, 0.00617796, -0.00609404, 0.205598])

names.append("LHipRoll")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([0.34826, 0.354396, 0.34826, 0.34826, 0.362067, 0.34826, 0.34826, 0.11049])

names.append("LHipYawPitch")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([-0.708667, -0.708667, -0.710201, -0.710201, -0.70253, -0.705598, -0.710201, -0.159494])

names.append("LKneePitch")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([-0.092082, -0.092082, -0.090548, -0.090548, -0.0859459, -0.090548, -0.0890139, -0.0890139])

names.append("LShoulderPitch")
times.append([0.68, 1.76, 2.6, 3.16, 3.52, 4.24, 4.96, 5.56, 7.04])
keys.append([1.41737, 1.49101, 1.49101, 1.47567, 1.4772, 1.36522, 1.38363, 1.3192, 1.53703])

names.append("LShoulderRoll")
times.append([0.68, 1.76, 2.6, 3.16, 3.52, 4.24, 4.96, 5.56, 7.04])
keys.append([0.345107, 0.302157, 0.29602, 0.29602, 0.269941, 0.25767, 0.202446, 0.145688, 0.130348])

names.append("LWristYaw")
times.append([0.68, 1.76, 2.6, 3.16, 3.52, 4.24, 4.96, 5.56, 7.04])
keys.append([0.288349, 0.36505, 0.345107, 0.343573, 0.34971, 0.42641, 0.446352, 0.450955, 0.147222])

names.append("RAnklePitch")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([-0.363515, -0.10427, -0.36505, -0.395731, -0.283749, -0.446352, -0.458624, 0.0614019])

names.append("RAnkleRoll")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([-0.0183661, 0.082878, -0.0183661, -0.0183661, 0.104354, -0.022968, -0.013764, 0.066004])

names.append("RElbowRoll")
times.append([0.6, 1.68, 2.52, 3.08, 3.44, 4.16, 4.88, 5.48, 6.16, 6.96])
keys.append([1.29474, 1.46501, 1.10759, 1.42973, 1.41132, 1.20883, 1.47268, 1.42973, 0.694641, 0.406552])

names.append("RElbowYaw")
times.append([0.6, 1.68, 2.52, 3.08, 3.44, 4.16, 4.88, 5.48, 6.96])
keys.append([0.918823, 0.466294, 0.302157, 0.478566, 0.489305, 0.265341, 0.406468, 0.299088, 1.16733])

names.append("RHand")
times.append([0.6, 1.68, 2.52, 3.08, 3.44, 4.16, 4.88, 5.48, 6.96])
keys.append([0.5728, 0.7912, 0.794, 0.79, 0.792, 0.7936, 0.7928, 0.7936, 0.3048])

names.append("RHipPitch")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([-0.903567, -0.630516, -0.905102, -0.934249, -0.731761, -0.94652, -0.94652, 0.18864])

names.append("RHipRoll")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([-0.144154, -0.156426, -0.144154, -0.153358, -0.200912, -0.145688, -0.162562, -0.068988])

names.append("RKneePitch")
times.append([1.72, 2.56, 3.12, 3.48, 4.2, 4.92, 5.52, 7])
keys.append([1.43893, 0.998676, 1.43893, 1.48649, 1.25179, 1.52637, 1.53558, -0.076658])

names.append("RShoulderPitch")
times.append([0.6, 1.68, 2.52, 3.08, 3.44, 4.16, 4.88, 5.48, 6.96])
keys.append([1.4282, 1.38064, 1.2886, 1.38064, 1.37144, 1.23951, 1.36223, 1.27633, 1.53558])

names.append("RShoulderRoll")
times.append([0.6, 1.68, 2.52, 3.08, 3.44, 4.16, 4.88, 5.48, 6.16, 6.96])
keys.append([-0.497058, -0.868286, -0.707216, -0.829935, -0.813062, -0.757838, -0.935783, -0.905102, -0.383972, -0.0859459])

names.append("RWristYaw")
times.append([0.6, 1.68, 2.52, 3.08, 3.44, 4.16, 4.88, 5.48, 6.96])
keys.append([0.207048, 0.220854, 0.300622, 0.233125, 0.253067, 0.306757, 0.440216, 0.415673, 0.168698])