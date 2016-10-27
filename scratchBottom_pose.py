# Choregraphe bezier export in Python.
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.72, 1.24, 1.72, 2.12, 2.52, 2.96, 3.84, 4.44, 5.04, 5.52])
keys.append([0.317496, 0.20398, -0.363599, -0.513931, -0.266959, -0.314512, -0.323717, -0.323717, -0.04913, -0.261799])

names.append("HeadYaw")
times.append([0.72, 1.24, 1.72, 2.12, 2.52, 2.96, 3.84, 4.44, 5.04, 5.52])
keys.append([0.297554, 0.358915, 0.352778, 0.314428, 0.302157, 0.326699, 0.306757, 0.31136, 0.067454, -0.0445279])

names.append("LAnklePitch")
times.append([1.48, 3.6, 5.28])
keys.append([-0.241683, -0.407355, -0.0296706])

names.append("LAnkleRoll")
times.append([1.48, 3.6, 5.28])
keys.append([-0.0349066, -0.0174533, -0.10472])

names.append("LElbowRoll")
times.append([0.56, 1.08, 1.56, 1.96, 2.36, 2.8, 3.2, 3.68, 4.28, 4.88, 5.36])
keys.append([-0.496974, -0.414139, -0.834454, -1.31153, -0.747017, -1.20261, -0.682588, -1.11057, -0.472429, -0.45709, -0.58748])

names.append("LElbowYaw")
times.append([0.56, 1.08, 1.56, 1.96, 2.36, 2.8, 3.2, 3.68, 4.28, 4.88, 5.36])
keys.append([-1.26252, -0.492455, -0.506262, -0.349794, -0.570689, -0.360533, -0.541544, -0.337522, 0.343573, -1.11526, -0.81613])

names.append("LHand")
times.append([0.56, 1.08, 1.56, 1.96, 2.36, 2.8, 3.68, 4.28, 4.88, 5.36])
keys.append([0.272727, 0.309091, 0.732387, 0.654545, 0.454545, 0.636364, 0.616387, 0.327273, 0.254545, 0.268389])

names.append("LHipPitch")
times.append([1.48, 3.6, 5.28])
keys.append([0.14966, -0.1418, 0.0959699])

names.append("LHipRoll")
times.append([1.48, 3.6, 5.28])
keys.append([0.15708, 0.161886, 0.1174])

names.append("LHipYawPitch")
times.append([1.48, 3.6, 5.28])
keys.append([-0.386344, -0.435432, -0.29277])

names.append("LKneePitch")
times.append([1.48, 3.6, 5.28])
keys.append([0.479093, 0.815037, 0.173826])

names.append("LShoulderPitch")
times.append([0.56, 1.08, 1.56, 1.96, 2.36, 2.8, 3.2, 3.68, 4.28, 4.88, 5.36])
keys.append([1.76866, 2.07853, 2.0944, 2.0944, 2.0944, 2.0944, 2.07392, 2.0908, 1.60606, 1.4726, 1.49101])

names.append("LShoulderRoll")
times.append([0.56, 1.08, 1.56, 1.96, 2.36, 2.8, 3.2, 3.68, 4.28, 4.88, 5.36])
keys.append([0.409536, 0.299088, 0.337438, 0.62583, 0.28068, 0.54146, 0.248467, 0.527653, 0.496974, 0.392662, 0.176367])

names.append("LWristYaw")
times.append([0.56, 1.08, 1.56, 1.96, 2.36, 2.8, 3.68, 4.28, 4.88, 5.36])
keys.append([-0.645772, -1.8326, -1.79483, -1.8326, -1.69297, -1.8326, -1.79176, -1.25664, -0.642281, -0.662729])

names.append("RAnklePitch")
times.append([1.48, 3.6, 5.28])
keys.append([-0.20944, -0.191986, 0.0174533])

names.append("RAnkleRoll")
times.append([1.48, 3.6, 5.28])
keys.append([0.0523599, 0.0523599, 0.0174533])

names.append("RElbowRoll")
times.append([0.4, 0.92, 1.4, 1.8, 2.64, 3.52, 4.12, 4.72, 5.2])
keys.append([0.454107, 0.469446, 0.431096, 0.533873, 0.38661, 0.469446, 0.567621, 0.464844, 0.622845])

names.append("RElbowYaw")
times.append([0.4, 0.92, 1.4, 1.8, 2.64, 3.52, 4.12, 4.72, 5.2])
keys.append([1.14432, 1.15199, 1.52322, 1.55543, 1.90979, 2.08773, 1.34374, 1.63367, 0.837522])

names.append("RHand")
times.append([0.92, 1.4, 2.64, 3.52, 5.2])
keys.append([0.181818, 0.185116, 0.184025, 0.18148, 0.364025])

names.append("RHipPitch")
times.append([1.48, 3.6, 5.28])
keys.append([0.245522, 0.0767824, 0.0691124])

names.append("RHipRoll")
times.append([1.48, 3.6, 5.28])
keys.append([-0.0698132, 0.0349066, -0.022908])

names.append("RKneePitch")
times.append([1.48, 3.6, 5.28])
keys.append([0.368275, 0.45111, 0.171922])

names.append("RShoulderPitch")
times.append([0.4, 0.92, 1.4, 1.8, 2.64, 3.52, 4.12, 4.72, 5.2])
keys.append([1.53864, 1.52944, 1.64296, 1.62915, 1.67517, 1.6, 1.48649, 1.51717, 1.48495])

names.append("RShoulderRoll")
times.append([0.4, 0.92, 1.4, 1.8, 2.64, 3.52, 4.12, 4.72, 5.2])
keys.append([-0.196393, -0.199461, -0.220938, -0.090548, -0.0890139, -0.067538, -0.016916, -0.038392, -0.205598])

names.append("RWristYaw")
times.append([0.92, 1.4, 2.64, 3.52, 5.2])
keys.append([0.10472, 0.108872, 0.118076, 0.116542, 0.94797])