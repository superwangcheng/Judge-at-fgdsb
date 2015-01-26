package tests;
import java.util.*;
import java.lang.*;
import java.io.*;

public class two_difference {
    public static int num_test = 50;
    public static int[][] in_0 = {{15, 18, 12, 22, -24, -13, -8, 0}, {-8, 10, 18, 17, 8, 16, -3, 15, -21, 22, -25}, {-28, -30, -23, 15, 2, -26, -27, 23, -3, 6, -24}, {22, 8, -6, -10, 9, -7, -18, 6, 24, 13}, {26, 4, -25, -24, 27}, {-409, -319, 334, -65, -156, -291, -40, 310, -92, -423, 155, 277, -111, 236, -473, 107, -416, 231, 314, 230, 440, 68, 191, -387, -19, -275, 301, 131, 119, -294, 222, -115, -127, -59, -213, 381, 247, 154, 348, -211, 463, -335, 285, 405, -410, -343, 174, 53, -151, 39, 177, -150, -170, 128, -322, -16, -386, -7, -351, 135, -376, 474, -485, -123, 150, 327, 464, 74, 443, 197, -420, 241, 75, -186, -118, 344, -460, 1, -317, 214, -326, -100, -63, 294, -71, 37, -455, 69, -41, -360, 225, 427, -61, 19, 182, -350, 352, 267, -329, 117, 355, 57, -309, 320, 87, -448, 475, -62, -271, 385, 394, -467, -458, 46, -393, 94, -327, -324, 397, 349, 112, 404, 176, 290, 411, -133, -430, -195, -74, -44, 296, -340, 50, 14, -476, -341, 100, -99, 361, 160, -230, -148, 30, -454, -78, -445, -89, 22, -404, 426, 157, -463, -252, 303}, {-178, -468, 298, 371, 317, 141, -155, 473, -139, -416, -262, 150, -357, 263, -137, -470, -5, 233, 120, -85, 387, -271, 167, 153, -8, -280, -93, -487, -207, -118, -173, 384, 466, 403, -35, -462, -188, 248, 274, 302, -168, -113, -129, 465, 336, 70, -248, -87, -423, 38, -106, -214, 385, 277, -6, 378, 445, -490, -198, 104, -285, -429, 30, 234, -225, -323, 489, -295, -481, -374, 1, 348, 420, -195, 219, -91, -96, -28, 2, -451, 227, -330, 103, -486, -254, -57, -361, -331, 157, -81, -231, -2, 27, -55, 265, -467, 488, 173, -171, 342, 147, 215, -492, -408, 320, -165, -465, 73, -363, -20, -450, -320, 218, 92, -308, 354, -365, 367, -283, -239, 290, 402, -393, 57, -180, 458, 33, -482, 383, -94, 490, 382, 18, 88, -74, 204, -23, 209, -495, 292, 369, 175, 471, 126}, {-333, 315, -66, 352, -53, -372, -304, -242, 71, -494, -280, 128, -270, 104, -164, 344, -195, -463, -233, 389, -383, 297, -405, 3, 182, 216, 341, 433, 435, -388, -446, 64, -498, 167, 160, 307, -135, -470, -211, -3, 90, 355, 218, -267, -328, 97, -205, 161, 221, 185, -252, -230, -311, 19, -234, -438, -264, -250, 34, 460, 154, -277, -216, -374, 459, -184, -89, -290, -338, 499, -8, 248, 198, -493, -379, -48, 196, 169, -236, 316, 65, -228, -198, 115, 310, 448, 317, 485, -188, -215, -344, -355, -320, 346, -480, -213, -352, -83, 380, -420, -468, 12, -258, 149, 274, 21, -227, 476, 308, -36, 100, 421, 168, 69, 478, -6, -71, -386, 480, 40, -345, -389, -444, -401, 304, 397, 101, -325, 252, -268, -392, 206, -15, -201, -94, -476, -362, 162, 458, -450, -237, 139, 42, 148, -351, -177}, {212, -459, 375, 155, 228, -199, 204, 299, -55, -473, -358, 39, 12, -311, 489, 115, -107, -109, -42, 32, -224, 172, -135, 25, 229, 5, 462, -397, -468, -23, -41, -410, -139, 288, 306, 37, 136, 327, -248, -310, 189, 425, 480, 187, 235, -213, -58, -476, -423, 325, -178, -192, 357, -338, -267, -18, -74, 81, -257, 248, 124, -411, 35, -487, -484, -350, -405, -26, -346, -381, -360, -245, 492, -312, -22, -91, 275, -453, -28, -345, 287, 51, -425, -16, -175, 303, -203, 141, 143, -186, 418, -369, -136, 286, 209, -456, -1, -157, 190, 77, -349, 232, -467, 442, -320, -66, -327, 421, -106, -374, -292, -401, -7, 58, 334, 330, 298, -271, 188, 262, -147, -123, 344, -382, 131, 26, -498, 123, 207, 169, 98, -485, 194, 104, 120, 199, 379, 304, -375, -276, -404, -30, -38, -61, 138, -424, 154, 82, 160, 239, 388, 435, -421, 477, -355, 323, 244, 413, -400, 457, -493, 281, -455, -13, -399, -499, -258, -275, -452, -445, 20, 268, -212, 122, 372, -29, -282, 476, -435, -124, -4, -394, -259, -227}, {-179, -325, -309, 303, -321, 468, 478, 267, 432, -130, 412, 122, 470, 166, -372, -156, -43, 343, 68, 408, 455, 283, -370, 145, -210, -237, -170, -293, -189, 194, -398, 187, -473, -361, -290, -468, 258, 381, 139, 152, 444, 104, -47, -6, 335, -318, -41, -12, -371, -217, 239, 488, -413, -116, -474, -34, -51, 243, 82, -215, 76, 84, 112, 317, 486, -437, 277, 38, 302, 43, -264, 125, 331, -397, 489, -31, 347, -456, 257, 338, 340, 440, 271, -459, 83, 425, -281, -106, 98, -303, 23, -486, 327, -440, 10, 171, -355, 399, -90, -181, 45, 371, 403, -121, 287, 155, -472, 129, 276, 53, 37, -365, 224, -425, 133, 233, -446, 99, -341, -84, -414, 352, 69, 200, 179, -368, -52, 101, -64, 182, -115, -478, -247, 118, 496, 192, -432, 456, -279, 110, -278, -337, -426, 46, 130, -326, 235, -186, 394, -119, 358, 14, -483, -129, 382, -1, 105, -118, -160, -496, -388, 79, 18, -125, 108, -199, 140, 92, 231, 111, 434, 117, -465, -378, 36}, {54, -210, -425, -359, -454, -49, -161, -255, -405, -453, 308, -293, -218, -76, 346, 113, 391, 64, 357, 142, -309, -86, -273, -498, -169, 207, 394, 111, 478, -30, 483, -348, -31, 334, -380, 411, 421, -51, -22, -272, 387, -461, 89, -194, -267, -152, 345, 149, -27, -155, 63, -62, 271, -358, 254, -184, 217, -368, -182, -326, -263, 73, -379, -303, 172, 23, -71, 465, 361, -72, -446, -407, -63, -275, 444, -150, -369, 154, 370, -307, 59, -431, -65, 367, 24, 300, 354, 147, 253, -247, 11, 372, 350, -45, -261, 265, 170, 103, -104, 263, 4, 293, 374, -489, -282, -343, 445, -206, -140, 209, -373, 442, 355, -178, 493, -289, 26, 476, 399, -238, 435, 320, 185, -250, 218, 192, -376, -221, 250, -69, 284, 20, -143, -443, 331, -64, -16, 83}, {-207, 438, 119, -468, 351, 33, -397, 163, -69, -316, -258, 244, -359, 210, 462, -41, 191, 340, 400, -148, 308, 203, -488, -379, -42, -136, 230, -408, -325, -53, -457, 497, -262, 350, -74, -246, 374, 451, -362, 487, 155, -418, 232, -86, -333, 382, 260, -475, -94, -465, -255, 187, 463, -216, 427, -79, -157, 200, -243, -340, 138, 20, 477, -16, -410, 420, 12, -444, 72, -5, -481, -59, -10, 79, 482, -75, 41, -3, -55, -65, -140, 378, 13, 366, -414, -82, -33, -184, 298, -117, 87, 221, 429, -388, 172, -17, 370, 379, 335, -477, 32, 167, 132, 394, 327, 426, -196, -461, -240, -492, 65, -273, -143, -25, 144, 422, -91, -404, -311, -81, -434, -237, 240, -218, 157, 375, 268, -378, -296, 324, 73, -19, -170, 255, -307, -421, -130, -386, -318, 59, 282, -297, 53, -387, 315, 307, 465, -345, 253, 287, 297, 164, 263, 241, 474, 312, 150, -436, -96, 498, -72, 367, -445}, {107, 256, -20, 245, -30, -386, -473, 69, -135, -464, 106, -492, 270, -74, 497, -361, 210, -158, -410, -93, 439, -357, -116, -136, 376, -9, 368, -235, -271, 328, -364, 30, 123, 169, -316, 390, -123, 367, 456, -153, -459, -161, -208, -171, 173, -40, -494, -289, -379, -41, 345, -424, -300, 233, 401, -109, 265, -368, -467, -441, 50, -166, -26, 122, -260, 450, 365, 206, -89, 154, 198, -244, 481, -284, 377, 7, -470, 104, -328, 101, 264, 74, 480, 168, 468, 305, -344, -297, 416, 276, -137, 17, 142, -480, -67, -484, 105, 463, 392, 49, 190, 339, -243, -212, -369, -308, 90, -272, -188, 108, 373, 310, -461, -177, -131, 66, -121, -409, -195, -78, -385, 277, 490, -128, 11, 290, -307, -381, -16, -425, -293, 45, -266, -346, -475, -378, -430, 204, 383, -15, 170, -452, -57, -321, 87, 75, 133, 111, -442, -406, 381, -490, -479, -210, 295, 425, 334, -105, -451, 340, 155, 156, -84, 221, 236, 15, 359, -278, 322, -21, -283, -270, -106, 220, 326, 29, 318, -233, -118, -443, 251}, {314, -1, 180, 287, 257, -211, 403, 47, 466, -49, 104, 118, 172, -281, 486, -311, 390, 357, 294, -151, 247, 195, -440, 81, 64, -271, -47, 484, 226, -383, -369, -445, 492, 270, 439, -122, 44, -17, 453, -412, -421, -320, -418, 2, -178, -110, 464, 91, -117, -488, -53, 167, -9, 489, -468, 445, -392, -89, 335, -482, -195, 144, -473, -431, -58, 392, -209, -341, 336, 55, -7, 407, -396, -215, -345, 82, -457, -321, 435, -93, 280, -416, 15, 262, 253, -415, 304, -97, -295, -347, -130, 192, 1, -204, 160, 462, -298, 93, 307, 418, 290, -52, 74, -288, -328, -27, 375, 19, -26, -443, -237, 460, 384, -11, 477, -141, 347, 191, -252, -486, 342, 321, 181, 143, -454, 116, -397, -206, -487, -326, -354, -143, -291, -104, -422, 154, -70, 349, -497, -2, 239, -376, -456, -363, -60, -314, 206, 189, -479, -207}, {-358, -316, 497, -14, -378, 379, 189, -482, -475, -346, -119, 9, 4, -321, -40, -278, -255, 187, 258, 144, 485, -223, -251, -500, -153, 419, -72, 387, 500, 255, 171, -488, -122, 41, -467, 426, 130, 162, 117, 340, 224, 141, -315, -386, 494, 78, -371, -188, -137, 226, -179, -100, -411, 104, 238, 266, -80, 75, -415, -498, -298, 134, -425, -287, -32, 276, 242, 158, 272, -13, 294, 1, 155, 209, 46, 336, -367, 367, -96, -183, 14, -36, -381, 463, 476, 69, -388, -362, -302, 385, 362, 427, 63, -282, 74, -434, -77, 358, -354, 467, -104, 179, -9, -350, -105, -54, 458, 35, 101, 160, -432, -110, -438, -374, -236, 87, -275, -343, -478, 237, -24, -45, 373, -52, 376, 282, -441, -97, -308, -297, 337, 388, 298, -76, -427, -420, -160, -221, -142, -237, 390, 181, -326, -20, -86, 48, 45, 28, 279, -58, -243, -466, 318, 131, 236, 249, 17, -380, -459, -65, -296, 271, 142}, {-403, -99, 156, 431, -26, 455, -467, -286, -72, -306, 35, 311, -187, -194, 151, -435, 304, -169, -478, 207, 67, -161, -321, -154, -357, 494, -146, -176, -336, 389, -481, -277, -438, -431, 135, 281, -230, 20, -198, 12, -140, 405, 71, 85, 274, 215, 17, 107, 53, 249, -333, -81, -57, -388, -16, 187, -142, 294, -407, -192, 220, 265, -384, 213, -471, -305, -59, -385, -106, -327, 333, 370, 206, -56, 386, 165, 315, 155, 199, -457, -111, -344, 471, -450, -366, 245, -63, 246, 11, -129, 423, -217, -151, 447, 273, 302, 242, 279, 252, 113, 443, -325, -229, -443, -415, -417, 403, -322, 402, -155, -202, -433, 41, -301, 262, -214, -40, 65, -83, 407, 233, -91, -152, -128, 204, -121, -31, -82, 150, 81, -71, -253, 295, 170, 322, -149}, {187, -272, -166, 65, -475, 479, 461, 440, -140, -259, 307, -36, -86, -170, 319, 346, 439, -223, -101, 356, -478, -159, 199, -311, -70, -104, 396, 342, -308, -395, -235, -452, 228, 453, 159, -24, 254, -98, 41, 86, 256, -291, -445, 430, 109, -369, -325, -457, 149, 143, -5, -194, -206, -152, 420, -92, 377, 418, 286, -335, -16, 345, 314, 402, 267, -72, -337, -292, -459, 288, 467, -84, 387, 261, 191, -461, -495, 137, -126, 3, -330, 234, -137, -238, -492, 7, -406, -134, -480, 329, -102, 40, 310, -417, -274}, {182, -311, -282, 351, -214, -476, -336, -499, 1, 120, 212, 297, 78, -217, 444, 412, 107, -106, -314, 205, -242, 228, -257, 271, 237, -448, -102, 289, 136, 113, 242, -18, 414, 28, -297, -425, 191, 277, 479, -171, -190, 131, 471, -23, -492, 235, -93, 288, -333, -95, 443, -386, 170, -56, 160, -374, 46, -316, 99, 430, 464, 376, 168, 83, -9, 152, 231, 437, 347, -134, -288, 362, 387, 284, -138, -423, -146, 281, 485, -393, 449, -229, -416, 4, 475, 332, 209, 141, 3, -477, 27, -192, 349, -279, -402, 313, -87, 500, -296, 269, -97, 248, 188, 300, -35, -463, 103, -269, 219, -238, -203, -339, -153, -189, 314, 225, -79, 22, -397, -202, -272, 302, -66, -435, 166, 421, -182, 45, 84, 148, 245, 255, -128, 353, -65, -172, -181, -464, 158, 147, -121, -51, 440, -496, -64, -398, -204, -248, 407, 498, -473, 396, -46, -5, -88, -1, 342, -126, 426, -362, -347, 32, 346, 334, -266, -385, 156, -205, 42, -268, 227, -114, -361, 159, 106, -450, -148, 374, 184}, {132, 136, -6, -242, -361, 119, 354, -342, -336, -326, -487, -83, 246, -109, -255, 153, -393, -384, 361, -137, -67, -321, -135, -349, 384, -18, -439, -459, -154, 145, -156, -276, 374, -111, -75, 63, 497, 97, 349, -283, -423, -165, -80, -500, 488, 31, -203, -19, 90, 269, 263, -25, -488, 340, 71, -496, 338, -484, 140, -90, -115, 3, 152, -162, 113, 298, -198, 304, -317, -388, -356, 386, -385, -14, -215, 240, 188, 211, -220, 356, -166, 133, -193, 36, -28, -157, -345, 346, 193, -449, 285, -94, -362, 389, 208, -429, -300, -469, -302, 262, 307, -292, 229, 111, -121, -103, 187, 30, -117, 185, -77, 456, 55, 493}, {329, 376, -95, -455, 18, -427, -38, -224, -467, 330, 178, -37, -352, 378, 41, -44, 305, -11, 438, -431, -264, -176, -268, -466, 39, -143, 499, 443, -192, -403, 157, -216, -307, -34, -57, -271, 488, 135, 152, 464, 474, 258, -12, 452, 407, 362, -488, 24, -302, 143, -401, 393, -180, -412, -24, -119, 436, -208, 417, -323, -94, 444, 482, 11, -132, 497, -190, -298, 83, -203, 318, 203, 130, 81, -145, 311, 377, -98, 498, 63, 256, -453, -250, 164, 51, -496, 352, 103, 241, 177, -162, -234, -166, -81, 349, 433, -497, 441, -65, -123, 418, -243, 253, -72, 481, -138, -417, -470, -195, -236, -377, 74, -290, -5, -471, -35, 175, -329, 466, 145, 392, -220, 462, -410, 4, 284, -186, 331, 351, 475, -227, -440, -371, 431, 57, 254, 95, -285, -480, -491, 105, 272, 199, 487, -112, -173, 89, 111, -393, -251, -369, 427, -490, 115, -199, -450, 163, -346, -18, -104, -3, -22, 196, 73, 382, 149, 366, 125, 496, -305, 259, 118, -150, -233, -392, 202, 72, 71, 222, 68, 32}, {307, 130, 498, -133, -306, 364, 280, -260, 237, -368, 143, 408, -65, -115, -492, -318, -495, -376, -452, -189, 6, -402, -7, -35, 158, 1, -389, -234, -178, 402, -291, -412, -163, 31, 236, -352, -470, 176, -330, -312, -494, -436, -363, 179, 319, -300, 155, 363, 406, 52, 160, -39, 432, -64, -8, -396, 140, 348, 234, -96, 449, 430, 91, 245, 242, 397, 126, -191, 77, 496, 123, -155, 180, -37, -2, -401, 216, 15, 445, 412, -197, -437, 63, 421, -271, -77, 9, 70, 190, 491, 58, -440, -356, -485, -438, 425}, {-334, 99, -264, -259, 381, -129, -398, 448, 165, 174, -426, -471, 463, 371, 290, 114, -473, -37, -321, -353, 191, 288, -354, 362, -437, 475, 110, 205, -319, -489, -444, 324, 478, 461, -83, -213, 55, -360, -92, -227, 111, -115, -441, -306, -249, 471, -466, 440, 411, 200, -345, -428, -65, 59, 360, -187, 190, -239, 215, 61, -244, -331, 40, 112, 35, 287, -195, -316, -496, 218, -31, -200, 96, 419, -59, -246, 393, -40, -307, -493, -157, 117, 66, -18, -300, 160, -486, -191, 217, -422, -133, 91, 80, 134, -492, -185, -336, 487, -54, -167, -240, 195, -42, -415, 175, 280, 69, 295, -350, 155, 244, 22, -124, 316, 129, -309, -203, -344, -308, 242, 166, -376, -120, 311, -245, -275, -335, 249, 319, -132, -468, -450, -201, 488, 251, 329, -477, 42, 83, -257, -127, 172, 154, 385, -14, 370, -281, -220, -490, 330, -154, 356, 32, 211, 180, 261, -273, -469, 495, 303, 231, -134, -176, 24, -142, -226, -256, -303, 236, -435, 466, 127, -258, -24, 30, 499, 382, 164, -84, 232}, {493, -255, 373, 29, 496, 24, 71, -314, 367, -10, 120, 277, 136, -103, 375, -30, -150, -34, 137, -302, 295, -1, -2, -361, -135, 154, 202, -294, -379, 378, -424, 314, -60, -469, 403, -174, 50, 434, 197, -433, -198, 253, -462, -28, 80, -180, -367, 19, 492, 463, -41, -133, 347, -298, -99, -176, 108, 451, 38, -360, 199, -38, -166, -333, 473, 179, -258, -73, -125, 155, 388, -423, -338, 268, -56, -445, -266, 138, 429, 479, -229, 304, 390, -204, 235, 421, 324, -466, 284, 15, -498, -442, -292, 18, 217, -339, -317, 21, 269, 380, 129, 101, -282, 409, -17, 78, -322, -8, 158, -467, -231, -24, 61, -391, -288, -117, 222, -309, -280, -295, 44, 346, -149, -381, -52, -13, 310, -315, -98, -328, -487, -26, 486, 203, 258, 157, 57, 428, 151, -447, 143, 453, -177, 27, -32, -113, -216, -62, -243, -209, 459, 164, -110, -116, -313, -408, 466, 404, -222, 134, -134, 114, -74, 302, -307, -321, -256, 394}, {70, -25, 357, -183, 86, -137, 360, -301, -331, -390, -304, -43, -147, -368, -243, 276, -182, 346, -407, -279, 174, -241, 94, 189, 166, 45, -340, 74, -442, 198, 442, -258, -228, 435, 148, -410, -175, 277, -157, 452, 200, -105, -387, 232, 444, -353, 302, 326, 46, -328, -465, 90, -93, 95, 8, -140, 335, -217, -244, -215, -350, -344, -114, -200, 428, 241, -363, 345, -57, 496, -31, -450, 279, -202, -212, -119, 290, 29, 85, -72, -347, -406, 125, 460, -107, -39, 180, 152, -334, -36, -10, -488, 365, 255, -198, -346, -153, 269, -286, -248, 472, 116, 27, 350, -440, -362, 287, -16, -472, -271, 497, 374, -426, -28, -58, 250, -150, 455, 52, -91, 47, 145, -415, 178, -496, 267, -151, 407, 394, -329, 457, -42, 363, 151, 278, 88, 136, -67, -90, 393, 324, -139, -298, 121, 228, -209, -216, 10, 421, 235, 221, 124, 38, -462, 303, -232, 397, -163, -305, 40, 187, 201, -164, -323, 416, 454, -433, 126, -281, -326, 482, -463}, {243, -149, -475, 400, -411, 19, 239, 26, -190, 215, 343, 44, -243, 183, 263, -268, 442, 101, 382, 456, -194, 162, -80, 448, -9, -480, 31, -164, 198, 62, 328, 188, -298, 292, 475, -280, -28, -374, 84, 389, 326, -283, -57, 59, 179, 260, 229, -370, 93, -20, 253, -482, -69, 329, 56, -430, -314, -81, 7, 428, -386, 234, 288, 465, -356, -450, 232, -227, 238, 398, 461, 332, 43, 500, 414, -112, -429, -84, 151, -481, -222, 9, -325, 368, -189, -288, -2, -371, -279, 403, 333, 10, 187, 160, -42, 470, -16, 427, -3, 479, 153, -87, -318, 335, -471, 192, -355, 496, 92, -26, 37, -361, 433, -85, 438, -172, -215, 286, -359, -396, 213, 344, -412}, {47, 241, 184, 406, 15, 448, -420, -253, -311, 19, -315, 421, 422, 69, 36, 430, 149, 358, 413, 444, 410, 169, -67, -205, -444, 475, 400, 340, 42, -190, 287, -365, -215, -436, -492, -120, -228, 352, 490, -257, 107, -394, -174, -48, 330, -18, 275, -491, 365, -409, 71, -36, -113, 8, 337, 283, 350, 251, 2, 86, -392, 316, -21, 464, 389, 38, 482, 368, -128, 139, 124, -395, 336, 309, -445, -319, -346, 373, -211, -460, -162, -277, -323, -193, -222, -127, -399, 341, 467, 209, 294, -179, -327, -321, -139, 495, -104, -92, -52, -254, 191, -329, -341, 197, -328, -65, 431, 40, 68, 22, -398, 424, 284, 231, -131, 460, 303, -443, 153, -7, 390, 208, 289, 227, -73, 236, 75, -402, -255, -250, 7, -144, -437, 474, 148, -140, 259, -306, -35, -337, 63}, {-293, -313, -320, -170, 326, 34, 224, 316, 208, -467, -146, 16, -152, 469, 446, 432, 375, 255, -107, 50, -270, 437, 95, 358, 271, -205, -207, -355, -41, 435, 429, 445, 305, -198, -329, -228, 101, 172, 32, 334, 293, -220, -72, 127, -477, 245, -36, -131, -448, -133, 28, -466, 376, -381, -260, -16, 181, 412, -288, -189, -460, 370, -353, -444, -11, -474, -470, 8, 67, -332, -457, 398, -422, 38, -39, -132, -469, 338, 365, -247, 385, 170, -5, -379, 390, -180, -63, 58, 54, 128, 145, -4, -159, 472, -279, -66, 343, 449, -386, -235, 143, -432, -135, 19, -253, -3, 45, -117, -405, 499, 364, -450}, {223, 219, -123, 382, -268, 106, 493, -418, 19, 440, -494, 258, -423, 385, -236, -42, -32, 332, -217, 104, 459, -261, -215, 265, -97, 496, 192, -452, -117, 113, -58, 202, 398, 206, 241, 21, -493, 215, -292, 174, 18, 32, 203, 77, 48, 221, 330, -376, 365, 322, 472, -169, -403, -407, -135, 381, 347, -314, 412, 39, 216, -85, 345, -366, -5, 2, -224, -100, 190, -337, -323, 257, -432, 390, 291, 411, -257, 462, -426, -490, 64, 54, -108, -165, -262, 13, -43, -177, -383, -68, 357, -331, -411, -389, -421, -128, 226, -163, -303, 145, 55, -86, -229, 157, 220, -254, -151, -199, -400, 434, -228, -398, -9, 199, -253, 56, 82, 171, 267, -468, 479, -283, -219, 301, 167, 118, -201, 490, -345, -155, -41, 346}, {-416, -470, 391, 56, 455, 461, -263, -194, -167, -255, -20, -161, 438, -380, -119, 230, 137, -318, 403, 200, -124, -417, 253, 384, 165, -74, 204, 423, -75, -221, 112, 352, 466, -91, 353, 103, 231, -381, -49, -139, 9, -187, -173, 105, 129, -433, 320, -283, -65, -169, 319, 265, 258, -12, -192, 170, 492, -406, 418, 417, -480, -133, -223, 209, 85, 463, 280, 318, 203, -69, 309, -351, 386, 294, -31, 255, -478, 227, -52, 469, 186, 114, -334, 99, -298, 429, 193, -218, -7, 38, -475, -402, -63, 347, -410, -367, -189, -494, -466, -474, 415, -93, 448, -415, -123, -408, -356, 87, -471, 314, 273, 444, 268, -401, 367, 262, 190, -452, -227, 335, -114, 152, 70, -340, 58, -61, 364, 19, -345, -32, -360, -488, 289, 369}, {40, -249, 434, 239, -137, -183, -66, 407, -290, 485, 494, -4, 457, -89, -166, 409, -250, -472, -332, 71, -425, 466, 323, -84, 379, 104, -423, 6, -337, 355, -222, -214, 268, 311, -184, 343, 397, -313, 110, -192, 17, -406, 161, 316, -46, 394, 490, -491, 186, -432, 143, 162, -185, -106, 191, -344, -31, -481, -300, -247, 233, 380, 20, -177, -211, -155, -121, 207, -413, -448, -49, -245, 59, -254, -475, -83, -218, 497, -72, -376, 410, 443, 419, -43, -188, 97, -353, 395, -314, -54, -369, 353, -391, -45, -57, 128, -257, -348, -384, 441, 96, 254, -366, -12, 1, 456, 372, 58, -271, 138, 492}, {-269, 121, -325, 445, 223, 411, 477, 429, 357, 243, 201, 17, 110, 56, -301, 139, 210, -474, 440, 184, 197, 286, 81, 487, 89, -61, -101, 163, 214, 105, 498, 13, 258, -433, 196, -60, -312, -385, -306, 156, 42, -262, 12, 359, 272, 412, 247, 436, -400, -124, -176, 478, 323, -326, -122, 167, -450, -68, 458, -388, -422, -164, -62, -58, -343, -368, -430, 38, 126, 267, 280, 439, -264, 448, 33, -223, -197, -15, 475, -446, -403, 66, -261, -199, -21, -342, -286, -167, 140, -97, 314, 269, 29, 58, 120, 208, 485, -80, -93, 136, -491, 171}, {417, -456, 346, 456, 141, 494, -325, 175, 54, 239, 281, 11, 204, 98, 401, 158, -17, 464, -324, 242, -169, 419, 217, -266, -10, 129, 385, -90, 187, -79, 327, -37, -476, 6, 153, -402, -54, 110, 384, -333, 125, 374, 216, 29, -149, -73, -115, 115, -430, -118, 321, 241, -285, 172, -114, -429, -304, -106, 191, -218, 350, -313, 62, -219, 171, -94, 131, 395, -213, -217, -102, 247, -240, -211, -183, -154, -19, -14, 156, -398, 454, 265, 73, 352, 477, -176, 64, -203, -145, -335, -179, 433, -291, 466, 476, 40, 97, 142, 359, -96, -125, -385, -164, -139, -230, 331, -495, -147, -270, -356, -135, 311, -453, 19, -428, 325, -177, 99, -403, -126, -399, -315, -484, -316, -287, 434, -220, 293, 214, 340, -427, -492, 69, -440, -373, -468}, {28, 438, 239, 409, -357, -100, 111, 298, -177, 204, 500, 71, -375, 162, 467, -422, -116, -175, 107, -480, 149, -183, -80, -353, 212, -365, -475, -226, 11, 200, 64, 473, -99, 487, 252, -181, 180, -212, -398, 244, 168, -449, -96, -291, -335, -379, 52, 243, 159, -52, -105, 245, -407, -152, 238, 13, 207, 406, 267, 90, 420, 378, -198, -22, -451, 249, 222, -498, 428, -442, 261, -364, 327, -88, 30, 362, -154, -299, 457, -370, 172, -492, 382, 189, -168, 464, -63, -49, -112, -425, 499, 260, 470, 36, 340, 110, -308, 425, -295, -24, -124, -268, 44, 321, -383, 193, -190, 55, 236, 353, 389, -60, 329, 130, -128}, {371, -300, 173, 154, 286, 487, 434, -106, -482, 109, -478, -211, -491, 308, -286, 466, -213, 397, 463, -272, -271, 18, -48, 126, -206, 411, -314, 145, -6, 430, -451, -253, 134, 17, 321, -440, 384, 390, -143, -167, -111, -110, 52, -437, -382, 91, 282, 13, 273, -57, -458, -294, 174, 92, 97, 391, 251, -3, -421, -82, 198, 37, -256, 3, 422, 336, -329, 320, 370, 421, -311, -22, -108, 169, -364, -114, 323, -221, 181, -80, -454, -473, -169, -176, 298, -323, -279, -234, 249, -90, 49, 353, 99, 445, -175, 348, 387, 303, 474, 405, -29, 241, -453, 301, -387, -464, 330, -456, -147, -290, -91, -384, -398, 192, -424, -389, -350, -317, 9, -484, -151, -212, 354, -205, 339, 55, -146, 136, -93, -339, -430, -409, -4, -236, -481}, {-478, -487, -270, -424, -443, 311, 98, -204, -260, -208, 410, -8, 240, 54, 39, -252, 164, 299, 345, -259, 103, -380, -34, -221, -120, -73, -418, 436, -322, 202, 69, 374, 473, 433, 477, -291, 244, 497, 444, 425, -28, 451, -386, -81, 227, 154, 3, -326, -212, -313, 2, 217, -392, 118, 206, -96, 151, 58, 65, 306, -88, -240, -310, 105, -344, 315, 4, -75, -89, -442, -193, -472, -311, -441, -138, 332, 201, 353, 147, -495, 340, -4, 38, 101, 347, -224, -188, 36, -400, 412, -223, 293, 73, -378, -420, 496, 403, -176, 186, 465, 398, 376, -500, 169, -100, 356, 342, -406, 485, -24, -401, -29, 90, -166, 50, -133, 32, 366, -130, 416, -286, -239, 11, -409, -179, 92, -228, 228, 283, -136, 122, -342, 141, -355}, {223, -343, 449, 198, -327, -252, 476, -2, -132, 63, 490, 455, 351, 328, 331, -163, -319, 71, -240, 321, 86, -37, -392, -144, -402, 20, -36, -464, -53, 188, 478, -390, 111, 114, 121, -279, -290, 12, -139, 320, 371, 447, -66, 273, -187, -129, -283, -490, 369, -193, -74, -255, 190, 453, 151, 265, -453, 93, 168, -125, 251, -99, 201, 129, -185, -28, -273, -367, 124, 355, -354, -246, -407, -469, -184, -308, -109, -81, -214, 123, -147, -251, -349, 90, 313, 314, -310, 59, -190, 296, 473, -85, 409, 15, 177, 259, -335, -306, 139, 305, -437, 404, -465, -89, -455, -237, -80, 253, 388, 166, -475, -452, -268, -225, -73, -385, -391, -90, 348, 28, 30, -92, 231, -337, -220, -348, -112, 441, 458, 173, 285, -78, 118, -120, 324, -211, -395, 341, -45, 158, 430, -102, -29, 300, -450, 340, 148, 488, 460, 477, 486, 403, -446, 356, -180, -17, 145, -447, 266, -353, 264, 463, 283, 474, -54, 290, -421, -488, 393, 406, 23, -377, 21, -95, 180, 459, 408, -4, -491, 95, 363}, {-257, 96, -101, -169, -407, 123, 172, -302, -471, 498, -55, 208, -286, -125, 100, 204, 385, 289, 215, 382, -161, -181, -349, 21, -317, 364, 324, -202, 369, -387, 166, 37, 5, -281, 0, 436, -223, -167, -23, 417, -287, 316, 432, 256, 50, -10, -217, 218, 310, 337, 113, 226, 380, 285, -329, -276, -215, 241, 483, -158, 413, 409, 28, -173, 473, 7, 33, 148, -333, -121, -386, 242, 183, 103, -247, -438, 239, 428, -357, 488, -35, 131, -390, -62, 358, 87, 331, 141, -106, -324, 314, -249, -44, -432, 338, 13, 79, 408, 187, -477, 10, -397, 17, -488, -359, 119, 26, 384, 147, 15, 104, 379, 110, -377, 4, 120, -244, 308, 348, -219, -328, 75, 190, 475, -423, -272}, {-411, 93, 354, -94, -213, -364, 477, 332, 272, 162, 341, 330, 475, 292, -173, -285, -453, 9, 141, 331, 481, 289, 488, -260, 279, 258, 172, -138, -50, -182, 348, -396, -18, -60, 25, -312, -198, 280, 426, -107, -101, 250, 387, 187, -148, -419, -339, -277, 107, -346, -359, 47, -455, 287, 340, -323, 433, -375, -397, -271, -111, -333, -296, 69, 78, -154, 171, 282, 77, -266, -282, 66, 189, 126, 173, -235, 442, -74, -147, 436, 474, 319, 333, 464, -357, 29, -377, -336, 489, -306, -229, 263, 304, 225, 133, -70, -219, 155, 59, 480, -29, 499, 196, 91, 389, -3, 140}, {-228, -278, -58, 144, 453, -340, -292, -55, -476, 149, -254, 350, -488, 396, 451, -143, -380, 336, 276, 92, 467, -408, 369, 440, 109, -329, 487, -369, 111, -442, 339, 258, 265, -384, -345, -121, 289, 102, -376, 159, -21, 496, -361, 181, 97, -17, 371, 138, 250, 57, -46, -158, 175, 385, 198, 209, 196, -94, 357, -165, -159, -185, -497, 55, -167, 310, -33, 414, 94, 164, -397, 327, 221, -289, 24, 309, -4, 449, -347, -465, -493, 151, -36, -52, -356, 224, 39, -127, 446, 418, 124, -29, -350, 137, -215, 464, -306, -449, -395, 3, -175, -171, -318, -391, 297, 254, 427, 105, 483, -280, -407, -482, -75, -485, -249, -342, 479, -80, -40, -321, -59, -69, -491, -181, -230, -85, 122, 458, -87, -70, -244, -309, -261, -362, -270, -232, -110, 145}, {-297, -244, -20, -57, 244, -243, 430, 431, 389, -440, -345, 164, 233, -305, 31, 150, -315, -476, -402, -307, 393, 394, 448, -214, 276, -245, 286, 277, -452, 134, -141, 295, 310, 333, 139, -466, -448, 16, 187, -66, -228, -427, 23, -362, 99, -96, 102, 496, 152, 65, 192, 177, -347, 142, -320, -282, 253, -111, 188, 50, 342, 29, -308, -260, 386, -65, -358, 495, -87, -38, 482, -224, -247, 145, 115, 384, 111, -350, 1, 197, -468, 413, -74, -365, -3, -70, -229, 347, -310, 161, 81, 379, 247, 410, -181, -138, -334, 360, -73, 382, -368, 199, 53, 128, -76, -364, -293, 215, -424, -209, 21, 228, 72, -474, 121, -286, -4, -172, 158, 363, 41, 227, 225, 40, 254, 25, -330, 468, 491, -125, -198, -33, -477, -246, -17, 175, -348, 488, 100, 78, -277, 308, 26, 91, -93, -425, -429, -471, -404, 7, -433, -337, -61, -253, -26, 275, 293, -483, 352, 245, -384, 300, -231, -451, 14, -405, 43, -119, 278, 30, 159, 279, -479}, {-489, -474, -468, -458, -450, -449, -437, -418, -416, -402, -385, -373, -343, -339, -334, -333, -313, -304, -297, -294, -247, -246, -244, -243, -230, -211, -208, -195, -190, -173, -170, -139, -138, -133, -95, -86, -83, -69, -61, -41, -20, -11, -5, -2, 2, 8, 11, 15, 22, 37, 48, 61, 65, 83, 96, 104, 109, 122, 123, 136, 139, 181, 196, 198, 215, 229, 246, 288, 306, 316, 330, 343, 349, 351, 361, 364, 379, 380, 391, 410, 428, 431, 439, 440, 445, 455, 465, 468, 478, 484, 490}, {-496, -495, -481, -405, -394, -381, -372, -371, -353, -347, -334, -323, -308, -296, -295, -293, -233, -220, -193, -180, -177, -175, -173, -169, -160, -146, -144, -137, -105, -75, -72, -63, -45, -29, -25, -9, 12, 13, 23, 26, 28, 29, 47, 102, 108, 111, 128, 138, 143, 144, 148, 151, 153, 170, 189, 194, 210, 213, 214, 235, 242, 264, 288, 289, 310, 313, 319, 327, 332, 334, 337, 349, 362, 372, 376, 377, 382, 399, 406, 407, 413, 454, 455, 462, 482, 500}, {-492, -468, -435, -424, -419, -418, -399, -391, -382, -379, -358, -333, -332, -325, -313, -303, -287, -275, -274, -267, -262, -237, -223, -219, -216, -204, -184, -174, -163, -150, -147, -142, -133, -132, -123, -117, -112, -88, -83, -76, -72, -62, -57, -56, -43, -41, -37, -28, -27, -25, -22, 8, 18, 20, 33, 94, 108, 129, 133, 149, 153, 167, 171, 196, 202, 230, 239, 246, 290, 301, 339, 370, 377, 378, 405, 413, 437, 446, 454, 455, 462, 485, 491, 493}, {-485, -477, -459, -438, -417, -401, -392, -379, -371, -336, -322, -312, -285, -280, -271, -268, -265, -260, -253, -231, -229, -225, -206, -203, -193, -182, -162, -149, -136, -81, -79, -78, -73, -68, -44, -32, -8, 11, 16, 49, 57, 64, 72, 81, 93, 119, 125, 136, 146, 151, 154, 155, 169, 171, 172, 182, 183, 195, 203, 222, 229, 243, 268, 270, 274, 284, 299, 300, 308, 316, 318, 325, 333, 343, 362, 372, 381, 392, 394, 423, 424, 432, 450, 451, 453, 460, 470, 493}, {-475, -468, -441, -422, -415, -405, -385, -360, -359, -354, -346, -338, -328, -291, -238, -225, -216, -202, -156, -117, -105, -83, -61, -56, -53, -51, -50, -38, -7, -1, 7, 14, 27, 30, 70, 100, 125, 132, 141, 150, 188, 190, 211, 229, 291, 333, 334, 364, 423, 446, 447, 456, 458, 469}, {-497, -490, -482, -479, -473, -465, -461, -449, -447, -443, -439, -424, -423, -415, -408, -402, -401, -396, -377, -356, -347, -344, -334, -333, -312, -304, -297, -290, -285, -276, -269, -261, -241, -223, -219, -216, -215, -212, -202, -176, -175, -142, -120, -119, -99, -93, -90, -76, -72, -71, -65, -45, -16, 0, 3, 28, 74, 85, 109, 114, 154, 167, 190, 191, 196, 207, 209, 215, 226, 229, 247, 250, 258, 269, 273, 280, 292, 309, 335, 336, 346, 358, 363, 369, 372, 378, 382, 390, 415, 419, 420, 421, 426, 439, 455, 460, 477}, {-500, -489, -463, -434, -425, -418, -345, -310, -306, -292, -275, -273, -270, -264, -259, -255, -252, -243, -199, -187, -160, -113, -17, -2, -1, 20, 30, 54, 62, 69, 116, 121, 131, 159, 174, 203, 209, 231, 236, 293, 294, 304, 312, 314, 351, 354, 397, 403, 428, 460, 466, 467}, {-473, -449, -446, -434, -427, -423, -419, -407, -388, -383, -381, -380, -375, -366, -361, -341, -338, -331, -330, -329, -323, -314, -303, -290, -273, -272, -265, -263, -248, -242, -236, -215, -208, -199, -183, -167, -161, -143, -140, -139, -105, -53, -49, -40, -38, -36, -30, -25, -21, -20, -4, 10, 29, 40, 41, 42, 59, 74, 91, 107, 108, 113, 124, 132, 167, 181, 189, 195, 210, 212, 213, 223, 233, 242, 265, 274, 279, 295, 296, 346, 347, 354, 371, 382, 415, 426, 428, 429, 435, 469, 492}, {-479, -464, -427, -414, -377, -370, -366, -312, -290, -287, -281, -280, -260, -252, -239, -210, -200, -190, -177, -175, -157, -146, -90, -85, -82, -47, -27, -24, -15, 7, 13, 32, 64, 75, 81, 97, 102, 138, 161, 169, 174, 177, 184, 197, 204, 214, 239, 288, 321, 337, 347, 373, 382, 393, 414, 415, 425, 451, 453, 462, 477, 480, 486, 498}, {-498, -489, -473, -466, -453, -451, -441, -422, -390, -388, -384, -366, -360, -335, -324, -323, -291, -265, -256, -242, -229, -179, -169, -155, -148, -146, -99, -94, -72, -69, -66, -15, 4, 5, 19, 38, 62, 70, 74, 79, 81, 86, 107, 108, 109, 111, 112, 124, 136, 161, 166, 175, 181, 196, 199, 208, 210, 217, 221, 222, 232, 233, 266, 279, 289, 316, 329, 354, 355, 357, 375, 397, 402, 403, 417, 428, 452, 457, 464, 467, 468, 485, 486}};
    public static int[][] in_org_0 = test_common.copy(in_0);
    public static int[] in_1 = {20, 8, 13, 3, 23, 47, 81, 68, 34, 247, 167, 647, 481, 520, 309, 131, 119, 133, 169, 230, 621, 590, 319, 336, 491, 195, 848, 14, 618, 671, 106, 779, 265, 23, 660, 318, 96, 649, 160, 675, -204, -319, -757, -451, -249, -759, -521, -158, -3, -589};
    public static int[] in_org_1 = test_common.copy(in_1);
    public static int[][] out = {{2, 6}, {4, 5}, {3, 4}, {4, 7}, {1, 4}, {29, 135}, {23, 63}, {50, 65}, {134, 146}, {150, 169}, {107, 110}, {37, 106}, {76, 124}, {16, 90}, {29, 105}, {7, 105}, {74, 92}, {76, 93}, {79, 106}, {55, 147}, {16, 66}, {5, 33}, {99, 112}, {74, 151}, {51, 81}, {10, 35}, {13, 83}, {31, 60}, {106, 115}, {12, 31}, {57, 67}, {55, 60}, {23, 73}, {34, 84}, {49, 84}, {85, 177}, {46, 69}, {8, 86}, {17, 41}, {6, 25}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}};
}
