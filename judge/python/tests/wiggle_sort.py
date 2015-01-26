import copy

num_test = 50
in_0 = [[20, 13, 16, 18, 3, 10], [14, 12, 2, 18, 15], [5, 18, 15, 10, 17, 4, 8, 4, 15], [20, 10, 13, 9, 16, 7, 17, 19], [18, 8, 15, 12, 14], [0, 16, 72, 38, 50, -92, 83, 11, 92, 43, -49, 36, -50, -36, -48, -77, 99, -49, 26, 90, 29, 35, -34, 52, 88, -34, -43, 67, -8, 33, -67, 57, 95, 60, -54, 11, -74, -34, 31, -22, -47, -57, 54, 40, 95, 60, 83, 55, -58, -87], [-2, 97, -30, -13, 27, 91, 87, -71, -1, 26, 1, 59, -52, 65, 6, -28, -21, -42, 19, 51, 99, -93], [-68, 53, -65, -33, 72, 11, 29, 2, -21, 86, 45, 68, 43, -55, -66, -35, 20, -20, 12, -81, -71, -88, -40, -36, -83, 8, -17, 51, -88, -29, 65, 45, -99, -53, 84, 32, -10, 22, 91, 35, -2, -35, 100, -11, 64, -74, -100, -63, -64], [16, -28, -85, 49, 96, -80, -79, -32, 83, 48, -45, -3, -13, 82, 13], [71, -4, -36, 40, 51, 51, -21, 67, -13, -76, -95, 73, 74, -93, 61, -26, 52], [87, 53, 34, -7, 32, -70, -15, -6, -38, -57, -27, 5, -82, -32, 72, 75, -58, 80, 93, -81, 46, -81, -37, 7], [-26, -79, 53, -57, 48, -69, 48, 23, -11, -99, 23, 16, 38, -57, -76, -25, 37, 35, 33, -75, -88, -90, 45, 100, 89, 27], [24, 88, 22, 93, 64, -67, 12, -39, -47, -41, -3, -74, 22, 32, -28, 31, -62, -86, -53, 33, -74, 80, 23, -44, -12, -71, 48, 11, 39, -19, 4, -75, 12, -55, 15, 55, 65, -85, -8, -53, -1, -97, 40, -21, -38, 78], [89, 1, 85, 95, -64, -53, 48, 48, 65, -36, 74, -85, -20, 56, -69, -68, -60, 29, 77, -31, -63, 82], [49, -12, -31, -85, -68, -87, -39, -44, -80, -99, 93, -28, 57, 35, -12, -31], [-92, 45, 55, -20, 21, -56, 69, -56, 68, 36, -43, 59, 47, 52, -43, 13, -71, 75, -37, 24, -77, 74, 97, 30, 40, -29, -42, 49, 18, -55, -52, -90, -61, 7, 71, -94, -88, 16, -44, 49, 68, 20, 32, -48, -32, 46, 37, 64, -36, -76], [-98, 4, 10, 48, 25, -21, 100, -2, -15, 14, -22, 19, -70, 79, 50, -50, 7, 96, -39, 56, 47, -95, -71, -38], [86, -1, 10, 8, -19, 51, -75, 87, -34, 13, 69, 93, -41, -15], [43, 43, -25, -66, 32, -38, 66, 91, -84, 39, 36, -41, -42, 17, 4, -16, -69, -20, -85, -27, 68, 24], [-51, -50, -88, 49, 37, -89, -51, -94, 86, 54, 37, 39, 41], [400, -2337, -3099, 7427, -6315, -2984, 5521, -9852, 5250, -7193, 3753, -3038, -1280, -885, 6910, 3607, -8485, 3675, -8693, 9033, 2610, -6604, 849, 7955, -1384, -4123, 9131, -4731, 3196, -4719, -5824, 3312, 2276, -1151, -1087, 2619, 3200, -7621, 1622, 2529, 8522, -8522, -2630, -1350, -399, -302, -5116, -8964, -3008, 2923, -7343, -8261, -1425, 2123, 3177, -2995, -94, -3943, 5934, -1592, 8654, -4594], [-6033, 9146, 7007, -984, 9211, -8672, 823, 6703, 5538, -2278, 8135, 2595, 6621, 5693, -7900, -6844, 402, -4808, -6763, 9346, -7447, -3445, 9591, -6818, -1860, 4700, -3751, -3290, -6069, 3489, -9390, -3566, 1101, 351, -2131, 4101, 1838, -9704, -3376, -2563, -2038, 5868, 4776, -9502, 2855, 4021, 226, -7463, -2161, -8434, -9107, -8100, -7052, 2018, 7211, 1857, 8465, 7833, 1803, -3315, -4804, 7621, -8030, 2232, 8005, 5916, -8590, -3422, 4680, 6769, 157, 3706, -6403], [-827, 2332, 2021, -4522, -706, -7861, 9353, -2730, -2222, 5135, 6829, -8408, 6976, 8634, -2935, -2094, -9315, 1043, -7468, 5292, 511, -8268, 2882, 96, 6285, 4971, -3768, -2416, -6350, -4763, 1028, -5107, 3980, 5323, -8127, 9622, -9593, 7197, 5906, -152, -4731, -4265, -1414, -9214, 6537, 1502, 3080, -2438, 9111, 9631, 3902, 8476, 9077, -4164, -1990, -3176, 4373, 4517, -1804, 1581, 1280, -7765, -5550, 1385, 3890, -6445, -6483, 5742, -5145, 3767], [-2061, -1652, -9888, -7561, -1422, -3396, 7718, -8099, 4413, 4324, -5415, -7424, 164, -4511, 2343, -6483, 6197, -9064, 4664, 9807, 5480, -1770, 8140, 6128, -7104, -5261, -6358, 605, -2840, 8818, 3620, 6885, -4837, 2619, 560, 7900, -2170, 3727, -34, 767, -7816, 9555, -424, -9611, -4763, -9889, 8253, -9135, -3606, 3076, 8474, -6611, 979, -5853, -4533, -5524, -5111], [5431, 9386, 6059, 799, 3540, -4111, -4721, 2871, 6511, -4427, 1929, 1557, -2291, -7312, 4069, -9589, 1, 213, -6271, -5933, -1029, 9461, 4183, -9033, -6776, 3431, -3988, -7897, 4046, -2358, 6231, 7963, 2711, 6609, -3609, 9726, -5598, -5376, 8980, 9425, -6733, -5766, 7604, -6292, 2290, -1388, 3153, 4646, 629, -4859, -3871, -5926, -3433, -4740, 6545, 8649, 422, -3462, -4808, -2300, 5743, 2806, 3451, 7733, 963, -8955, 3528, -2269, 7835, 8145, 6919, 6815, -5890, -2193, 8334, 1547, -5039, 6022, -2514, 4859, -4044, 9254, 921, -5108, 3796, 254, 4906, 9048], [-8969, -7593, -3157, 8610, 1464, 9673, 9077, -109, 706, 4883, 3951, 7558, -3611, -220, 8717, -2239, 2753, 2056, -7600, -1872, -2767, 5579, 6788, -5783, 4049, 4798, 5777, 7606, -9786, 1075, -4231, 4463, 4118, -7784, 7536, 6558, -2873, 6411, 766, 6034, -9408, 4018, 7078, 4046, -9881, -2934, 7024, 5089, -7565, -3347, 9213, 2752, -4869, -6244, 3837, 1455, 561, 9160, 7294, -5928, -215, 7265, -4105, -3170, 4213, -9878, -6340, -9873, 9555, 6355, -1163, 160, 2967], [-5849, -4731, -2343, 6243, 2820, -6677, -5774, 3140, 7978, -9563, -437, 4263, 5171, -314, -7721, -6299, -7812, -813, 4626, -3199, 2827, -6965, 2422, 204, -7898, -9301, 7722, -5563, 3129, 7037, 1400, 722, -2954, -1491, 5457, -3571, -83, -2727, -6558, -319, 7285, -6845, 5794, 1740, 5700, -2048, 7894, 435, -5739, -7581, 5817, -384, 4635, -4688, -7663, -2666, -9746, 8455, -2216, 2687, 5503, 2001, 1227, 5814, -8300, 2543, -2986, -6451, -8081, 6705, -5337, 2767, -6748, -5515, -7680, -3961, 3603, 3638, -8652, -3416, -8932], [6533, -632, -5889, -1370, -5221, 9812, 2521, 1639, -1977, -5239, -6221, -6248, 8657, 6550, -3929, 1734, 4605, -9555, -348, 859, -1300, 1071, -3651, 8505, -8297, 4982, -756, 3171, 2053, 9900, 5308, -9967, 5173, -8360, -8007, -5672, 1796, -3070, 8172, -144, 3039, -1644, 592, 2852, -22, -9642, -4166, 9227, -8141, 8744, -7332, -8370, 8087, 7917, 4476, 2777, -3742, 265, -1408, 2669, 3388, 318, -2516, 9030, 2225, -1455, -3448, -1307, -5067], [-1827, -4501, -1559, -7829, -370, 8633, 82, 1979, -8221, 7871, 5097, 4382, -7802, -8158, 8624, 2350, -5893, -3151, -7212, 7894, -9616, 4692, -257, 3333, 4824, 3794, 551, 9210, -975, 7990, -9953, -9476, 6398, -6277, 35, 6872, 3454, 2975, -4470, -5016, -324, 4057, 1397, 2347, 8501, 3556, 4045, 5630, -7102, -2379, -1235, 5300, 8597], [-9018, -65, 558, 1473, -8363, 5037, -1320, 5694, -9576, 5102, -2696, -8190, 7463, 3752, 7712, 1152, -6588, 2324, -8565, 6867, 5672, -4807, -7409, -2032, 1636, -2560, -4152, -4418, 1522, -4225, -3971, 834, -6749, -2374, -7202, 7032, 7999, -1995, 6879, -354, 784, -1839, 330, 6839, 7178, 7576, 2419, 3976, 9054, 4781, -8682, 5726, 8353, -3275, -1930, 9245, 9433, -1164, -4914, 9116, -6984, 4991, 8247, -9845, -8495, 8146, -8882, -6301, -9607, -8205, -7098, -2222, -4213, -4317, -5110, -1084, 519, 3869, 8149, -5483, 7579], [8120, -4237, -9622, -1289, 6427, -5407, 397, 2144, -9397, 7721, 9532, 899, 8957, 9749, -9603, -4960, 9358, -1817, 5202, 5933, 1143, 3631, -6496, 2606, -96, -6368, -191, -6765, 8167, 7496, 9062, 288, 4243, 7975, -563, 5659, 8563, 3504, 4473, -6889, -2061, -3014, 1165, -4180, 4604, -110, -2967, 3578, 650, 8956, -5350, 1626, 3108, -4676, 1823, -4105, 2330, 1923, -1224, -5624, -6828, -100, -6664, 7683, -9932, -860, -1968, 1100, 5038, -5655, -3657, -8069, 8913, -6247, 7216, -9731, 9959], [-3501, 9869, 9672, 1100, -7304, 6621, 5214, 6027, -1302, -28, 515, -6301, -5739, -4084, 8017, 2655, 2837, 9098, 9982, 7106, -2905, -6502, 5270, -4304, 6572, -7807, 2485, -6922, -3907, 762, 3558, 5571, 8046, 118, 6344, 1627, 9758, 5669, 5526, -7923, 8770, 5281, -5287, -6044, 9462, -5386, -3590, 7155, -2233, 3796, -3840, 4730, 8373, -8216, -2581, -6084, -5049, 8089, 4623, -8877, 3445, 927, 1445, -1577, 569, -5673, 5057, 6277, 9361, 1305, 4587, 1410, -453, 9024, 838, -2099], [-7963, 3772, 3803, 7410, -9674, 3652, -5258, 392, 6993, 3800, -962, 3012, 5279, 615, 2365, -1127, -1641, 1977, 453, 3191, -970, -4841, -1016, -1027, -2800, -1730, 3318, 1671, -831, -7707, 55, -8196, -2383, -3900, -8794, 8543, -7095, -8228, -659, -2148, -4352, -6131, -4616, -9998, -8865, 2892, -2112, -887, -1127, -674, -9421, -3311, 7221, -4365, 2961, 7800, 8965, -8348, -9911, -6253, 5874, 9687, 1011, 9834, -2531, -2067, -378, 5160, -3136, -182, 6509, 6045, -9981, 7499, 1059, -7374, -1997, 7945, -3627, -8669, 1525, 3884, -1959, 3088, 5710, -5636, 2528, -3747, 6680, 1836, -9883, 5899, -7142], [4444, 2688, 6698, -1003, -6396, 7748, 1355, 732, 9149, -2793, 9466, 772, -5822, -4311, -1268, -5716, 4575, -982, -9519, 962, -4609, 1900, -8908, 3471, -3596, 3838, -8591, -7349, -9834, -3792, 3968, 1995, -1621, -3003, 6386, -8769, -5367, -6594, 6375, -5707, -2853, 6181, -7297, -8786, -6814, -475, -8705, 6904, -449, -7400, 9026, -467, 7311, -9859, -524], [2850, 9152, 8330, -833, -5822, -6320, 4093, -8622, 8923, 9012, 367, 5617, 4846, -50, 3681, -5658, 2726, 6057, -3442, -7375, -172, -9566, 4400, -1578, 8041, -3576, 6280, 8108, 7036, -6708, -9900, -6400, -1986, -6672, 5394, 7280, 6689, 1775, -8296, -3844, -3773, -7783, 2002, 1993, -8373, 8914, -2519, -5865, 840, -6671, -9634, 3161, 2508, 7647, 9422, -5240, -4777, -1310, -7116, -4430, 3249, 589, 8401, -5806, 3426, 4392, -1575, -4683, 5964], [-1933, -1204, 7155, 8913, 1101, -1563, 111, 1387, 7812, 8475, 8798, -3844, 6378, 444, 2458, 918, -6743, -6930, 3869, -126, 6076, -3516, -9106, -5427, -7389, -1039, 201, 681, -5716, 1515, 9607, -3231, 4168, 6754, 7421, 6099, 6179, 464, -1145, 4516, 8777, 1529, 8862, -3655, -7888, -4292, 9559, 3793, -3323, -7794, -7753, -6930, 8193, -3722, -8390, -4236, -8411, 4596, 3338, 2720, 245, 3379, 7576, 8575, -4999, -2390, -6496, 3879, 2300, 7103, -7049, -5192, -4995, -8222, 7429, 6885, -3535, 5101, -1882, -9947, 7420, 5740, 6831, 3728], [-1106, -370, 3752, -7797, -1320, -4486, -4197, -1125, 3192, 3709, -7568, 746, -291, -7917, -170, -7362, 4018, -3529, 8819, 7304, 2415, -8322, -3464, 6574, 3272, -3986, -7951, 6765, 8644, 3835, -2473, 1326, 9065, 65, 6841, -3584, -4057, 810, -1690, -9301, -4009, -1696, 9734, -8068, -9908, -9401, -5279, -2902, 4620, 1870, -8419, 5606, 461, 3342, 6718, -2391, -5983, 1305, -485, 1166, 3931, 5097, 5144, -6045, -5418, 6630, 3331, 3082, -7705, 7213, -3609, 4593, -2304, -9450, -9675, -2589, -52, -4532], [-1506, 9243, -9641, 929, 5416, -5295, -329, -1618, 4018, 4199, 6259, 7261, -3296, -5034, 7052, -6533, -6652, -3206, 5678, 3760, 3401, 6821, 4494, -3792, 1694, 2782, 7203, 9987, 2309, 1066, 6239, 9034, -1739, -8620, -2771, 6865, -7625, 3123, -2686, -3622, 2026, 3997, -5728, -2542, 753, -8556, -8514, 4726, -7033, 2072, 507, 6074, -1195, -9547, 6342, -4122, -2150, 5530, 4233, -2243, -2006, 9257, 4458, 7510], [3626, -867, 9499, 9442, -5281, 299, -9060, 7064, -2486, -1834, 801, 6703, 6007, 3390, -9679, 8999, -5912, 830, 8398, -6960, 3924, 3113, 467, 8880, -2867, 7191, 6441, 9034, 3397, -1115, -9385, -4486, -3312, -4015, -9506, -8976, 6224, -2532, -2000, -1751, 804, 4694, 6789, -1294, -2411, 5990, -1069, -5140, 7779, 9836, -6345, -2913, 8515, -2579, 2450, 7059, -9087, 3094, 7074, 169, -3894, 9915, 7368, -2030, 9486, 8611, 870, -7203, 3976, 1299, 3195, -5126, -5071, 1034, 7096, 4950, -8200, 9488, 5241, -2935, -4229, -1039, 4728, -8740, 1758, -8482, 6626, 7155, -8726, -8300, -2961, 8967, 1109, 312, -7339, 719, 4979, 7425, 8407], [8304, 7880, -4942, 796, -2612, -6779, -5427, 1598, -5037, 9552, -2682, 2125, 9147, 5394, 8375, 444, -6084, -5756, 7097, 4955, 7951, 4021, 7976, 363, 2615, -8486, 1997, 7301, 7121, 6988, -9738, 499, -785, 1232, -724, 8862, 5147, -6249, -4473, -5468, 8904, 7445, 5259, 2002, 5262, -9957, -1137, -2511, 2097, 7149, 7630, -1483, 1796, -7688, -8217, 5120, -1730, -367, -1520, 1936, 3662, -1008, -511, -7338, -1048, -250, 6012, 7351, 4922, -9290, 7881, -9008, -2254, 8097, -5543, 202, 5752, -7153, -2963, 5281, 4844, 5365, 6012, 1378, 3724, -6422, -386, 5362, 6865, 2929, 4077, -7597, 5048, 2334, -9668, -631, -2216, 2972], [-2122, 682, -7538, 2201, -5972, 2468, -5142, 5652, -7958, 2228, 2256, 1472, -6424, 5595, 6967, 6464, -9926, -1832, 5808, -1479, -2370, -8000, 121, 3097, 8413, 2219, -2784, 7907, -4912, 8006, 329, 9659, -2570, -9659, -3979, 2033, -1308, -2188, 6208, -7767, -6036, 2987, 1139, 2600, 6842, -6613, 9394, -676, 5031, -215, 9166, 191, -8867, 8477, -7078, 6334, 7244, -3457, 5368, 1524, 205, 2691, 5124, -7435, 3993, -8986, 4448, -2538, -4652, 6207, 4550, -8754, -8084, 3657, 7665, -516, 9162, 3032, 3913, -1958, 6634, 6226, 3029, 9284, -2448, -8680], [-6836, -3266, -2538, 8514, -3919, -845, -1344, -9969, -1557, 1505, 3254, 5453, 1642, 3434, -67, 939, -2093, 8768, 1826, -6489, -7325, 8254, 3037, -788, -5551, -2197, 9955, 402, -92, 1872, 5792, 5175, -4508, -3241, -5503, -7415, -2027, 3157, 3537, -7813, 4149, 4175, 5362, 109, 155, -7333, -4913, -8990, 8704, 2951, -1426, -8505, -241, 8867, 5637, -8831, 2433, 4418, 4735, -8375, 5620, 5195, -3659, 8011, -4643, 7755, 6678, 4903, 6031, 8463, 8402, 313, 1929, -6104, 9219, 3616, -1969, 1905, -6130, -9723, 1991, 131, 5172, 6273, -9477, 2227, -7850, 5753, 495], [4931, 45, 6295, -5565, -7578, -7213, -5853, -1265, -2639, -8331, 8848, -4462, 5439, 6274, -8670, -1347, -4398, -7106, 7676, 6099, -8039, 6681, 6248, 6599, 3905, -3230, -317, -2382, -8132, -8421, -7355, 8127, 1118, -8294, -8183, 8848, -8583, 2005, -4952, 7811, -4098, -780, 4394, -8757, -5104, 8182, -1221, -2655, -9779, 8989, 6026, -8823, -1116, -1804, -9204, -6690, 2733, 4865, -8167, -6448, -9337, -7916, 5131, -3076, -8455, -3666, 2188, -8793, 8682, -8356, 8250, -1052, 2888, -9815, 2060, -3023, -895, -6008, -3698, -5974, -2578, -8757, 4253, 3109, 4102, -2579, 3255, -6095], [-7651, 7066, 2375, -3927, -1752, -8951, -7199, 9348, 1372, -1524, -2382, -2382, 5586, 4825, -4839, 5706, 6495, -2519, 1263, -5401, -8809, -4484, -7607, 5119, -7206, 8961, -6947, 8208, 8859, 9461, 954, 1635, -2855, -9897, 2429, 6706, 1952, 9645, 1826, -5425, -5894, 5822, 7647, -5201, -5795, -563, -9999, 3520, -8693, 5765, -1452, 8093, 4520, 4343, 6543, 4238, 7711, -6813, 7361, 5424, -4552, -7303], [-8481, -6967, -6836, -6311, 7023, -7452, -2360, -3611, 5629, -9893, 6318, -8825, -2125, 7283, -6875, 9584, 4200, 630, -2555, 1727, -6547, -2549, 4701, 339, 1655, 1493, 8396, 3539, 9922, 4608, 374, 3639, 8645, -4705, 9010, 3226, -2433, -9779, -7813, -1615, -4634, -6515, 3473, -285, -9115, 5902, 3873, 5788, 105, -8782, -6858, -6670, 6175, -7866, 6472, -836, -9673], [400, -8108, 9819, 8481, -3511, 9865, -6400, -4635, -1208, -8693, -9109, -7544, -6106, -8929, -3552, -1270, -411, 3037, -2372, 9935, -2146, -1083, 9438, 3340, -8427, -227, 44, -3981, 6037, 445, 8000, -8558, 5678, 4977, -6510, 1459, 928, -1103, 5435, 4488, 2751, 7863, 3274, 284, -8034, 4371, 6063, 5422, 1231, 5103, -9145, -6565, 6263, -7189, -2145, -5232, -8067, -6924, 6733, -2577], [713, -5878, -4169, 8289, 9694, -2841, -1018, 2622, -6111, -7986, 7485, -864, 7536, -5609, 1227, -9153, 4423, 3025, 5105, -8016, -62, -7087, -7282, 2030, -3676, 3579, 5731, -4093, -8313, -3916, 8646, -5937, 5595, 5382, -3333, 8443, 6453, 6096, -6304, -4709, 4329, 2924, -4846, -7961, 5284, -2353, -8484, -5834, -3409, -9222, -9769, 1842, -2665, 8128, 6071, -9047, 4909, -6880, -7287, -4998, -5762, 1704, 5889, 9554, -2871, -1745, -3867, 9796, 5612, -7718, -4328, -2619, 7271, -8608, -6024, 3713, 2166, 8923, -8368, -8980, -641], [4610, 6129, 9210, -5, -2388, -1260, -8999, 7972, 2003, -7903, -6362, 4457, 6360, 5522, 9133, -4929, -8604, 1044, -3252, 1354, -8979, 5846, -8095, 8873, 9738, -3710, 463, -9133, 6532, -8957, 2444, 3051, 1338, 5251, 2596, -423, 2745, 2733, 9711, 4657, -8025, 5985, 2548, 2802, 6812, -1097, 5950, -296, -6341, 1462, 7200, 8245, 5877, -3951, 1156, -8879, 259, 2024, 2522, -9203, 5371, 7496, -7646, 7278, -9165, -3096, 4721, 8305, -1055, -4636, -2366, 9554, -9970, -8759, -9948, -3704, -8147, -5740, 6257, -817, 2013, -5846, -7768, -4288, 778, 7168, -8072, 7087, 5507, 7921], [5831, -4842, -4667, 4738, 5514, 2813, -5112, 6678, -4677, -1274, -8102, -7137, 5940, -7037, -5743, -7164, 8354, 8050, 948, 8869, -7741, -5416, 1449, -2166, 477, 9641, 5916, 2206, -9258, 5514, 3262, 3599, 7927, -7799, 7160, -3777, -4287, -4183, -7390, -2960, -630, -7527, -7281, -8674, -2596, -3910, -8111, 9138, -6117, 7549, 6941, 9078, 8265, 9527, 6288, -5204, -1112, 2596, 8081, -2649, -6266, 9990, -6270, -5643, -6533, -187, 2868, -7601, 7442, 4155, 5884, 3714, 9122, -4171, -238], [-5694, -4252, 5475, -8566, -5648, -6865, 7632, -4526, -3871, -9378, 4245, 2482, 4299, -8958, -4201, -1992, 1401, 7901, 7407, 2063, -187, 2015, -712, 6881, -2887, -7776, 5700, -6142, 7887, -24, -4244, -6754, 1184, -5016, -1394, 1385, 8386, -5019, 6713, 867, -8626, 7455, 1646, -3811, -1104, -3756, -4294, -1293, 1641, 9182, 6737, 9227, 3835, 2039]]
in_org_0 = copy.deepcopy(in_0)
out = [[13, 20, 16, 18, 3, 10], [12, 14, 2, 18, 15], [5, 18, 10, 17, 4, 15, 4, 15, 8], [10, 20, 9, 16, 7, 17, 13, 19], [8, 18, 12, 15, 14], [0, 72, 16, 50, -92, 83, 11, 92, 38, 43, -49, 36, -50, -36, -77, 99, -49, 26, -48, 90, 29, 35, -34, 88, -34, 52, -43, 67, -8, 33, -67, 95, 57, 60, -54, 11, -74, 31, -34, -22, -57, 54, -47, 95, 40, 83, 55, 60, -87, -58], [-2, 97, -30, 27, -13, 91, -71, 87, -1, 26, 1, 59, -52, 65, -28, 6, -42, 19, -21, 99, -93, 51], [-68, 53, -65, 72, -33, 29, 2, 11, -21, 86, 45, 68, -55, 43, -66, 20, -35, 12, -81, -20, -88, -40, -71, -36, -83, 8, -17, 51, -88, 65, -29, 45, -99, 84, -53, 32, -10, 91, 22, 35, -35, 100, -11, 64, -74, -2, -100, -63, -64], [-28, 16, -85, 96, -80, 49, -79, 83, -32, 48, -45, -3, -13, 82, 13], [-4, 71, -36, 51, 40, 51, -21, 67, -76, -13, -95, 74, -93, 73, -26, 61, 52], [53, 87, -7, 34, -70, 32, -15, -6, -57, -27, -38, 5, -82, 72, -32, 75, -58, 93, -81, 80, -81, 46, -37, 7], [-79, 53, -57, 48, -69, 48, -26, 23, -99, 23, -11, 38, -57, 16, -76, 37, -25, 35, -75, 33, -90, 45, -88, 100, 27, 89], [24, 88, 22, 93, -67, 64, -39, 12, -47, -3, -74, 22, -41, 32, -28, 31, -86, -53, -62, 33, -74, 80, -44, 23, -71, 48, -12, 39, -19, 11, -75, 12, -55, 15, 4, 65, -85, 55, -53, -1, -97, 40, -21, -8, -38, 78], [1, 89, 85, 95, -64, 48, -53, 65, -36, 74, -85, 48, -20, 56, -69, -60, -68, 77, -31, 29, -63, 82], [-12, 49, -85, -31, -87, -39, -68, -44, -99, 93, -80, 57, -28, 35, -31, -12], [-92, 55, -20, 45, -56, 69, -56, 68, 21, 36, -43, 59, 47, 52, -43, 13, -71, 75, -37, 24, -77, 97, 30, 74, -29, 40, -42, 49, -55, 18, -90, -52, -61, 71, -94, 7, -88, 16, -44, 68, 20, 49, -48, 32, -32, 46, 37, 64, -76, -36], [-98, 10, 4, 48, -21, 100, -2, 25, -15, 14, -22, 19, -70, 79, -50, 50, 7, 96, -39, 56, -95, 47, -71, -38], [-1, 86, 8, 10, -19, 51, -75, 87, -34, 69, 13, 93, -41, -15], [43, 43, -66, 32, -38, 66, -25, 91, -84, 39, -41, 36, -42, 17, -16, 4, -69, -20, -85, 68, -27, 24], [-51, -50, -88, 49, -89, 37, -94, 86, -51, 54, 37, 41, 39], [-2337, 400, -3099, 7427, -6315, 5521, -9852, 5250, -7193, 3753, -3038, -1280, -2984, 6910, -885, 3607, -8485, 3675, -8693, 9033, -6604, 2610, 849, 7955, -4123, 9131, -4731, 3196, -4719, -1384, -5824, 3312, -1151, 2276, -1087, 3200, -7621, 2619, 1622, 8522, -8522, 2529, -2630, -399, -1350, -302, -8964, -3008, -5116, 2923, -8261, -1425, -7343, 3177, -2995, 2123, -3943, 5934, -1592, 8654, -4594, -94], [-6033, 9146, -984, 9211, -8672, 7007, 823, 6703, -2278, 8135, 2595, 6621, 5538, 5693, -7900, 402, -6844, -4808, -6763, 9346, -7447, 9591, -6818, -1860, -3445, 4700, -3751, -3290, -6069, 3489, -9390, 1101, -3566, 351, -2131, 4101, -9704, 1838, -3376, -2038, -2563, 5868, -9502, 4776, 2855, 4021, -7463, 226, -8434, -2161, -9107, -7052, -8100, 7211, 1857, 8465, 2018, 7833, -3315, 1803, -4804, 7621, -8030, 8005, 2232, 5916, -8590, 4680, -3422, 6769, 157, 3706, -6403], [-827, 2332, -4522, 2021, -7861, 9353, -2730, -706, -2222, 6829, -8408, 6976, 5135, 8634, -2935, -2094, -9315, 1043, -7468, 5292, -8268, 2882, 96, 6285, 511, 4971, -3768, -2416, -6350, 1028, -5107, 3980, -4763, 5323, -8127, 9622, -9593, 7197, -152, 5906, -4731, -1414, -9214, 6537, -4265, 3080, -2438, 9111, 1502, 9631, 3902, 9077, -4164, 8476, -3176, 4373, -1990, 4517, -1804, 1581, -7765, 1280, -5550, 3890, -6445, 1385, -6483, 5742, -5145, 3767], [-2061, -1652, -9888, -1422, -7561, 7718, -8099, 4413, -3396, 4324, -7424, 164, -5415, 2343, -6483, 6197, -9064, 4664, -4511, 9807, -1770, 8140, 5480, 6128, -7104, -5261, -6358, 605, -2840, 8818, 3620, 6885, -4837, 2619, 560, 7900, -2170, 3727, -34, 767, -7816, 9555, -9611, -424, -9889, 8253, -9135, -3606, -4763, 8474, -6611, 3076, -5853, 979, -5524, -4533, -5111], [5431, 9386, 799, 6059, -4111, 3540, -4721, 6511, -4427, 2871, 1557, 1929, -7312, 4069, -9589, 1, -2291, 213, -6271, -1029, -5933, 9461, -9033, 4183, -6776, 3431, -7897, 4046, -3988, 6231, -2358, 7963, 2711, 6609, -3609, 9726, -5598, 8980, -5376, 9425, -6733, 7604, -6292, 2290, -5766, 3153, -1388, 4646, -4859, 629, -5926, -3433, -4740, 6545, -3871, 8649, -3462, 422, -4808, 5743, -2300, 3451, 2806, 7733, -8955, 3528, -2269, 7835, 963, 8145, 6815, 6919, -5890, 8334, -2193, 1547, -5039, 6022, -2514, 4859, -4044, 9254, -5108, 3796, 254, 4906, 921, 9048], [-8969, -3157, -7593, 8610, 1464, 9673, -109, 9077, 706, 4883, 3951, 7558, -3611, 8717, -2239, 2753, -220, 2056, -7600, -1872, -2767, 6788, -5783, 5579, 4049, 5777, 4798, 7606, -9786, 1075, -4231, 4463, -7784, 7536, 4118, 6558, -2873, 6411, 766, 6034, -9408, 7078, 4018, 4046, -9881, 7024, -2934, 5089, -7565, 9213, -3347, 2752, -6244, 3837, -4869, 1455, 561, 9160, -5928, 7294, -215, 7265, -4105, 4213, -9878, -3170, -9873, 9555, -6340, 6355, -1163, 2967, 160], [-5849, -2343, -4731, 6243, -6677, 2820, -5774, 7978, -9563, 3140, -437, 5171, -314, 4263, -7721, -6299, -7812, 4626, -3199, 2827, -6965, 2422, -813, 204, -9301, 7722, -7898, 3129, -5563, 7037, 722, 1400, -2954, 5457, -3571, -83, -2727, -1491, -6558, 7285, -6845, 5794, -319, 5700, -2048, 7894, 435, 1740, -7581, 5817, -5739, 4635, -4688, -384, -7663, -2666, -9746, 8455, -2216, 5503, 2001, 2687, 1227, 5814, -8300, 2543, -6451, -2986, -8081, 6705, -5337, 2767, -6748, -5515, -7680, 3603, -3961, 3638, -8652, -3416, -8932], [-632, 6533, -5889, -1370, -5221, 9812, 1639, 2521, -5239, -1977, -6248, 8657, -6221, 6550, -3929, 4605, -9555, 1734, -348, 859, -1300, 1071, -3651, 8505, -8297, 4982, -756, 3171, 2053, 9900, -9967, 5308, -8360, 5173, -8007, 1796, -5672, 8172, -3070, 3039, -1644, 592, -144, 2852, -9642, -22, -4166, 9227, -8141, 8744, -8370, 8087, -7332, 7917, 2777, 4476, -3742, 265, -1408, 3388, 318, 2669, -2516, 9030, -1455, 2225, -3448, -1307, -5067], [-4501, -1559, -7829, -370, -1827, 8633, 82, 1979, -8221, 7871, 4382, 5097, -8158, 8624, -7802, 2350, -5893, -3151, -7212, 7894, -9616, 4692, -257, 4824, 3333, 3794, 551, 9210, -975, 7990, -9953, 6398, -9476, 35, -6277, 6872, 2975, 3454, -5016, -324, -4470, 4057, 1397, 8501, 2347, 4045, 3556, 5630, -7102, -1235, -2379, 8597, 5300], [-9018, 558, -65, 1473, -8363, 5037, -1320, 5694, -9576, 5102, -8190, 7463, -2696, 7712, 1152, 3752, -6588, 2324, -8565, 6867, -4807, 5672, -7409, 1636, -2560, -2032, -4418, 1522, -4225, -3971, -4152, 834, -6749, -2374, -7202, 7999, -1995, 7032, -354, 6879, -1839, 784, 330, 7178, 6839, 7576, 2419, 9054, 3976, 4781, -8682, 8353, -3275, 5726, -1930, 9433, -1164, 9245, -4914, 9116, -6984, 8247, -9845, 4991, -8495, 8146, -8882, -6301, -9607, -7098, -8205, -2222, -4317, -4213, -5110, 519, -1084, 8149, -5483, 7579, 3869], [-4237, 8120, -9622, 6427, -5407, 397, -1289, 2144, -9397, 9532, 899, 8957, 7721, 9749, -9603, 9358, -4960, 5202, -1817, 5933, 1143, 3631, -6496, 2606, -6368, -96, -6765, 8167, -191, 9062, 288, 7496, 4243, 7975, -563, 8563, 3504, 5659, -6889, 4473, -3014, 1165, -4180, 4604, -2061, -110, -2967, 3578, 650, 8956, -5350, 3108, -4676, 1823, -4105, 2330, 1626, 1923, -5624, -1224, -6828, -100, -6664, 7683, -9932, -860, -1968, 5038, -5655, 1100, -8069, 8913, -6247, 7216, -9731, 9959, -3657], [-3501, 9869, 1100, 9672, -7304, 6621, 5214, 6027, -1302, 515, -6301, -28, -5739, 8017, -4084, 2837, 2655, 9982, 7106, 9098, -6502, 5270, -4304, 6572, -7807, 2485, -6922, -2905, -3907, 3558, 762, 8046, 118, 6344, 1627, 9758, 5571, 5669, -7923, 8770, 5281, 5526, -6044, 9462, -5386, -3590, -5287, 7155, -2233, 3796, -3840, 8373, -8216, 4730, -6084, -2581, -5049, 8089, -8877, 4623, 927, 3445, -1577, 1445, -5673, 5057, 569, 9361, 1305, 6277, 1410, 4587, -453, 9024, -2099, 838], [-7963, 3803, 3772, 7410, -9674, 3652, -5258, 6993, 392, 3800, -962, 5279, 615, 3012, -1127, 2365, -1641, 1977, 453, 3191, -4841, -970, -1027, -1016, -2800, 3318, -1730, 1671, -7707, 55, -8196, -831, -3900, -2383, -8794, 8543, -8228, -659, -7095, -2148, -6131, -4352, -9998, -4616, -8865, 2892, -2112, -887, -1127, -674, -9421, 7221, -4365, 2961, -3311, 8965, -8348, 7800, -9911, 5874, -6253, 9687, 1011, 9834, -2531, -378, -2067, 5160, -3136, 6509, -182, 6045, -9981, 7499, -7374, 1059, -1997, 7945, -8669, 1525, -3627, 3884, -1959, 5710, -5636, 3088, -3747, 6680, 1836, 2528, -9883, 5899, -7142], [2688, 6698, -1003, 4444, -6396, 7748, 732, 9149, -2793, 9466, 772, 1355, -5822, -1268, -5716, 4575, -4311, -982, -9519, 962, -4609, 1900, -8908, 3471, -3596, 3838, -8591, -7349, -9834, 3968, -3792, 1995, -3003, 6386, -8769, -1621, -6594, 6375, -5707, -2853, -5367, 6181, -8786, -6814, -7297, -475, -8705, 6904, -7400, 9026, -467, 7311, -9859, -449, -524], [2850, 9152, -833, 8330, -6320, 4093, -8622, 8923, -5822, 9012, 367, 5617, -50, 4846, -5658, 3681, 2726, 6057, -7375, -172, -9566, 4400, -3442, 8041, -3576, 6280, -1578, 8108, -6708, 7036, -9900, -1986, -6672, 5394, -6400, 7280, 1775, 6689, -8296, -3773, -7783, 2002, -3844, 1993, -8373, 8914, -5865, 840, -6671, -2519, -9634, 3161, 2508, 9422, -5240, 7647, -4777, -1310, -7116, 3249, -4430, 8401, -5806, 3426, 589, 4392, -4683, 5964, -1575], [-1933, 7155, -1204, 8913, -1563, 1101, 111, 7812, 1387, 8798, -3844, 8475, 444, 6378, 918, 2458, -6930, 3869, -6743, 6076, -3516, -126, -9106, -5427, -7389, 201, -1039, 681, -5716, 9607, -3231, 4168, 1515, 7421, 6099, 6754, 464, 6179, -1145, 8777, 1529, 8862, -3655, 4516, -7888, 9559, -4292, 3793, -7794, -3323, -7753, 8193, -6930, -3722, -8390, -4236, -8411, 4596, 2720, 3338, 245, 7576, 3379, 8575, -4999, -2390, -6496, 3879, 2300, 7103, -7049, -4995, -8222, 7429, -5192, 6885, -3535, 5101, -9947, 7420, -1882, 6831, 3728, 5740], [-1106, 3752, -7797, -370, -4486, -1320, -4197, 3192, -1125, 3709, -7568, 746, -7917, -170, -7362, 4018, -3529, 8819, -291, 7304, -8322, 2415, -3464, 6574, -3986, 3272, -7951, 8644, 3835, 6765, -2473, 9065, 65, 6841, -3584, 1326, -4057, 810, -9301, -1690, -4009, 9734, -8068, -1696, -9908, -5279, -9401, 4620, -2902, 1870, -8419, 5606, 461, 6718, -2391, 3342, -5983, 1305, -485, 3931, 1166, 5144, -6045, 5097, -5418, 6630, 3082, 3331, -7705, 7213, -3609, 4593, -9450, -2304, -9675, -52, -4532, -2589], [-1506, 9243, -9641, 5416, -5295, 929, -1618, 4018, -329, 6259, 4199, 7261, -5034, 7052, -6533, -3296, -6652, 5678, -3206, 3760, 3401, 6821, -3792, 4494, 1694, 7203, 2782, 9987, 1066, 6239, 2309, 9034, -8620, -1739, -2771, 6865, -7625, 3123, -3622, 2026, -2686, 3997, -5728, 753, -8556, -2542, -8514, 4726, -7033, 2072, 507, 6074, -9547, 6342, -4122, -1195, -2150, 5530, -2243, 4233, -2006, 9257, 4458, 7510], [-867, 9499, 3626, 9442, -5281, 299, -9060, 7064, -2486, 801, -1834, 6703, 3390, 6007, -9679, 8999, -5912, 8398, -6960, 3924, 830, 3113, 467, 8880, -2867, 7191, 6441, 9034, -1115, 3397, -9385, -3312, -4486, -4015, -9506, 6224, -8976, -2000, -2532, 804, -1751, 6789, -1294, 4694, -2411, 5990, -5140, 7779, -1069, 9836, -6345, 8515, -2913, 2450, -2579, 7059, -9087, 7074, 169, 3094, -3894, 9915, -2030, 9486, 7368, 8611, -7203, 3976, 870, 3195, -5126, 1299, -5071, 7096, 1034, 4950, -8200, 9488, -2935, 5241, -4229, 4728, -8740, 1758, -8482, 6626, -1039, 7155, -8726, -2961, -8300, 8967, 312, 1109, -7339, 4979, 719, 8407, 7425], [7880, 8304, -4942, 796, -6779, -2612, -5427, 1598, -5037, 9552, -2682, 9147, 2125, 8375, 444, 5394, -6084, 7097, -5756, 7951, 4021, 7976, 363, 4955, -8486, 2615, 1997, 7301, 6988, 7121, -9738, 499, -785, 1232, -724, 8862, -6249, 5147, -5468, 8904, -4473, 7445, 2002, 5262, -9957, 5259, -2511, 2097, -1137, 7630, -1483, 7149, -7688, 1796, -8217, 5120, -1730, -367, -1520, 3662, -1008, 1936, -7338, -511, -1048, 6012, -250, 7351, -9290, 7881, -9008, 4922, -2254, 8097, -5543, 5752, -7153, 202, -2963, 5281, 4844, 6012, 1378, 5365, -6422, 3724, -386, 6865, 2929, 5362, -7597, 5048, 2334, 4077, -9668, -631, -2216, 2972], [-2122, 682, -7538, 2201, -5972, 2468, -5142, 5652, -7958, 2256, 1472, 2228, -6424, 6967, 5595, 6464, -9926, 5808, -1832, -1479, -8000, 121, -2370, 8413, 2219, 3097, -2784, 7907, -4912, 8006, 329, 9659, -9659, -2570, -3979, 2033, -2188, 6208, -7767, -1308, -6036, 2987, 1139, 6842, -6613, 9394, -676, 5031, -215, 9166, 191, 2600, -8867, 8477, -7078, 7244, -3457, 6334, 1524, 5368, 205, 5124, -7435, 3993, -8986, 4448, -2538, 2691, -4652, 6207, -8754, 4550, -8084, 7665, -516, 9162, 3032, 3913, -1958, 6634, 3657, 6226, 3029, 9284, -8680, -2448], [-6836, -2538, -3266, 8514, -3919, -845, -9969, -1344, -1557, 3254, 1505, 5453, 1642, 3434, -67, 939, -2093, 8768, -6489, 1826, -7325, 8254, -788, 3037, -5551, 9955, -2197, 402, -92, 5792, 1872, 5175, -4508, -3241, -7415, -2027, -5503, 3537, -7813, 4149, 3157, 5362, 109, 4175, -7333, 155, -8990, 8704, -4913, 2951, -8505, -241, -1426, 8867, -8831, 5637, 2433, 4735, -8375, 5620, 4418, 5195, -3659, 8011, -4643, 7755, 4903, 6678, 6031, 8463, 313, 8402, -6104, 9219, 1929, 3616, -1969, 1905, -9723, 1991, -6130, 5172, 131, 6273, -9477, 2227, -7850, 5753, 495], [45, 6295, -5565, 4931, -7578, -5853, -7213, -1265, -8331, 8848, -4462, 5439, -2639, 6274, -8670, -1347, -7106, 7676, -4398, 6099, -8039, 6681, 6248, 6599, -3230, 3905, -2382, -317, -8421, -7355, -8132, 8127, -8294, 1118, -8183, 8848, -8583, 2005, -4952, 7811, -4098, 4394, -8757, -780, -5104, 8182, -2655, -1221, -9779, 8989, -8823, 6026, -1804, -1116, -9204, 2733, -6690, 4865, -8167, -6448, -9337, 5131, -7916, -3076, -8455, 2188, -8793, 8682, -8356, 8250, -3666, 2888, -9815, 2060, -3023, -895, -6008, -1052, -5974, -2578, -8757, 4253, -3698, 4102, -2579, 3255, -6095, 3109], [-7651, 7066, -3927, 2375, -8951, -1752, -7199, 9348, -1524, 1372, -2382, 5586, -2382, 4825, -4839, 6495, -2519, 5706, -5401, 1263, -8809, -4484, -7607, 5119, -7206, 8961, -6947, 8859, 8208, 9461, 954, 1635, -9897, 2429, -2855, 6706, 1952, 9645, -5425, 1826, -5894, 7647, -5201, 5822, -5795, -563, -9999, 3520, -8693, 5765, -1452, 8093, 4343, 6543, 4238, 7711, -6813, 7361, 4520, 5424, -7303, -4552], [-8481, -6836, -6967, 7023, -7452, -2360, -6311, 5629, -9893, 6318, -8825, -2125, -3611, 7283, -6875, 9584, 630, 4200, -2555, 1727, -6547, 4701, -2549, 1655, 339, 8396, 1493, 9922, 3539, 4608, 374, 8645, -4705, 9010, 3226, 3639, -9779, -2433, -7813, -1615, -6515, 3473, -4634, -285, -9115, 5902, 3873, 5788, -8782, 105, -6858, 6175, -7866, 6472, -6670, -836, -9673], [-8108, 9819, 400, 8481, -3511, 9865, -6400, -1208, -8693, -4635, -9109, -6106, -8929, -3552, -7544, -411, -1270, 3037, -2372, 9935, -2146, 9438, -1083, 3340, -8427, 44, -3981, 6037, -227, 8000, -8558, 5678, 445, 4977, -6510, 1459, -1103, 5435, 928, 4488, 2751, 7863, 284, 3274, -8034, 6063, 4371, 5422, 1231, 5103, -9145, 6263, -7189, -2145, -6565, -5232, -8067, 6733, -6924, -2577], [-5878, 713, -4169, 9694, -2841, 8289, -1018, 2622, -7986, 7485, -6111, 7536, -5609, 1227, -9153, 4423, -864, 5105, -8016, 3025, -7087, -62, -7282, 2030, -3676, 5731, -4093, 3579, -8313, 8646, -5937, 5595, -3916, 5382, -3333, 8443, 6096, 6453, -6304, 4329, -4709, 2924, -7961, 5284, -4846, -2353, -8484, -3409, -9222, -5834, -9769, 1842, -2665, 8128, -9047, 6071, -6880, 4909, -7287, -4998, -5762, 5889, 1704, 9554, -2871, -1745, -3867, 9796, -7718, 5612, -4328, 7271, -8608, -2619, -6024, 3713, 2166, 8923, -8980, -641, -8368], [4610, 9210, -5, 6129, -2388, -1260, -8999, 7972, -7903, 2003, -6362, 6360, 4457, 9133, -4929, 5522, -8604, 1044, -3252, 1354, -8979, 5846, -8095, 9738, -3710, 8873, -9133, 6532, -8957, 2444, 463, 3051, 1338, 5251, -423, 2745, 2596, 9711, 2733, 4657, -8025, 5985, 2548, 6812, -1097, 5950, -296, 2802, -6341, 7200, 1462, 8245, -3951, 5877, -8879, 1156, 259, 2522, -9203, 5371, 2024, 7496, -7646, 7278, -9165, 4721, -3096, 8305, -4636, -1055, -2366, 9554, -9970, -8759, -9948, -3704, -8147, 6257, -5740, 2013, -5846, -817, -7768, 778, -4288, 7168, -8072, 7087, 5507, 7921], [-4842, 5831, -4667, 5514, 2813, 4738, -5112, 6678, -4677, -1274, -8102, 5940, -7137, -5743, -7164, 8354, -7037, 8050, 948, 8869, -7741, 1449, -5416, 477, -2166, 9641, 2206, 5916, -9258, 5514, 3262, 7927, -7799, 7160, -3777, 3599, -4287, -4183, -7390, -630, -7527, -2960, -8674, -2596, -7281, -3910, -8111, 9138, -6117, 7549, 6941, 9078, 8265, 9527, -5204, 6288, -1112, 8081, -2649, 2596, -6266, 9990, -6270, -5643, -6533, 2868, -7601, 7442, -187, 5884, 3714, 9122, -4171, 4155, -238], [-5694, 5475, -8566, -4252, -6865, 7632, -5648, -3871, -9378, 4245, -4526, 4299, -8958, 2482, -4201, 1401, -1992, 7901, 2063, 7407, -187, 2015, -712, 6881, -7776, 5700, -6142, 7887, -2887, -24, -6754, 1184, -5016, -1394, -4244, 8386, -5019, 6713, 867, 1385, -8626, 7455, -3811, 1646, -3756, -1104, -4294, 1641, -1293, 9182, 6737, 9227, 2039, 3835]]
