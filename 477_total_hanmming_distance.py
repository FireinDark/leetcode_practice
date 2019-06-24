# -*- coding: utf-8 -*-
__author__ = 'yi.liu'


class Solution:
     # 时间复杂度太高
     # def totalHammingDistance(self, nums) -> int:
     #    result = 0
     #    for i in range(len(nums) - 1):
     #        for j in range(i + 1, len(nums)):
     #            tmp = nums[i] ^ nums[j]
     #            result += len(str(bin(tmp)).split('1')) - 1
     #    return result

     # 另外一种就是根据二进制每位数上的数进行表示
     # 比如 4个数
     # 1 0 0 0
     # 0 1 0 0
     # 0 0 1 0
     # 1 0 0 1
     # 高位上 0 有2 个， 1有两个，选出两个不同的数字组合数量为 C(2 1) * C(2 1) = 4
     # 所以只需要把所有的每一位上不同的数加起来就行
     def totalHammingDistance(self, nums) -> int:
          if len(nums) < 2:
               return 0
          result = 0
          for i in range(31):
               num_zero = num_one = 0
               for num in nums:
                    if (num >> i) & 1:
                         num_one += 1
                    else:
                         num_zero += 1
               result += num_zero * num_one
          return result

if __name__ == '__main__':
    a = [9527589, 7604310, 3278196, 6342685, 2854091, 1244203, 714240, 6722801, 7792918, 2476447, 6983281, 3489538,
         5781896, 35913, 2843903, 1176154, 1292032, 9599466, 448269, 4461609, 1116775, 6729246, 2447744, 22693, 3510830,
         4447362, 8642422, 4468115, 8827494, 863193, 5287491, 5819309, 5539248, 6894936, 7852570, 6527656, 7168350,
         6902063, 9148571, 1321593, 9544613, 3817322, 8932378, 149601, 4692604, 3856514, 1433453, 198410, 2244, 3639597,
         6615396, 6577552, 5984177, 5098054, 1512409, 9073011, 3812630, 2487912, 7247579, 4089441, 6430561, 7890199,
         8788702, 2001717, 9122869, 5454056, 8539505, 5859565, 1478327, 3875326, 3071449, 8116306, 9101645, 7796624,
         1907722, 6235484, 3282909, 8102896, 3903311, 7353565, 6142031, 5824650, 159101, 6085371, 8381965, 7034498,
         8459612, 3832071, 5689621, 1539768, 3217257, 4080934, 7651834, 761753, 6570301, 3338265, 6744921, 1134447,
         8765773, 5200415, 8304112, 5094862, 947666, 792065, 359597, 8595949, 6635183, 4205082, 4555867, 9871979,
         1194789, 9221032, 7888842, 3632559, 9229196, 5833099, 2070800, 4747869, 4647122, 3548318, 2047754, 8545195,
         3949571, 2554518, 5058998, 2458753, 1280044, 803060, 8616827, 4585618, 9973701, 2483797, 163886, 4339110,
         5087351, 6085711, 1714834, 844426, 2725989, 1946624, 6899284, 5174274, 8173970, 3634561, 4784365, 3102815,
         1999443, 5848061, 7138489, 8267015, 4110205, 3289799, 269304, 6462012, 1724134, 8492481, 6170710, 2458535,
         4333141, 9529390, 5492206, 6566689, 2935780, 9609492, 3323230, 5733745, 6549655, 6217832, 376657, 8439037,
         5723200, 846331, 7124835, 7394836, 7265127, 7415521, 1070345, 2351371, 3397350, 1175917, 6226019, 1472298,
         457080, 1021595, 4399522, 8062055, 818047, 8335580, 727028, 3634937, 7469975, 5375009, 8305024, 6347535,
         169619, 6021263, 6415988, 6504966, 4474565, 8575599, 6215889, 5383343, 4954495, 9620010, 1883700, 5092996,
         533716, 4935069, 9707161, 2522779, 7760069, 5452973, 811480, 8833010, 6776917, 661684, 986152, 267979, 4225204,
         9235610, 1342330, 4010040, 4217090, 4420322, 4183390, 8758579, 9448922, 2030222, 5959735, 6729317, 4191662,
         3069507, 4775422, 9410214, 5786399, 4328433, 662235, 4524144, 279163, 4529757, 690364, 5743268, 8647361,
         3188822, 1197112, 2417917, 4905194, 5081683, 7707967, 2676572, 4601417, 3737029, 5100684, 3423952, 1526241,
         3668745, 7070432, 6723883, 5290381, 8680605, 3737641, 6989724, 8356972, 1786615, 4593514, 1780307, 1339781,
         8436641, 7790941, 7387899, 5956144, 8282935, 5357913, 4515730, 1550975, 1924151, 6328375, 7536453, 853844,
         6295491, 703089, 7704788, 8545429, 5377787, 796448, 5444298, 6827666, 9492349, 8824610, 2424272, 8033411,
         2941517, 7023361, 4258631, 7973977, 5546791, 6098094, 7668159, 8328361, 5930782, 6605535, 9758723, 4666690,
         4198159, 7636406, 9950845, 6876939, 140013, 2768733, 5809744, 3955492, 9032010, 5961134, 7340397, 6293521,
         4998033, 371066, 9842920, 6571088, 9862330, 1879513, 1775976, 7770309, 4090140, 9217210, 4475041, 8348444,
         8962942, 8374037, 5865714, 7375638, 8147519, 2615782, 6402867, 5325075, 6715242, 3908671, 1546863, 218501,
         9916102, 8402071, 1673063, 358187, 4424123, 7502197, 1465451, 4522283, 6678002, 8413282, 5500627, 9058079,
         650283, 4743613, 3116530, 9730894, 745818, 6415691, 9254887, 8139890, 8561134, 9378168, 7663233, 7061322,
         1672091, 8615248, 3635188, 4193154, 6159083, 6706680, 799471, 4007438, 4683698, 6327149, 1129493, 6679541,
         4232809, 8916202, 3379457, 6080287, 7744645, 3229248, 209384, 9588596, 8230135, 1110427, 4236832, 4026141,
         5999995, 1910823, 7055234, 694030, 9829885, 7187444, 714586, 721112, 2861770, 44955, 7024751, 5589695, 3595998,
         2413404, 398158, 5698566, 7068915, 2266220, 4464716, 3303657, 8938090, 9039119, 158673, 1884532, 4740908,
         3929129, 6253468, 5507530, 9093934, 4471133, 849777, 7681221, 4973461, 3664996, 8031677, 4485890, 550497,
         9094646, 6302875, 8258511, 9275922, 469270, 6723726, 7932858, 6323115, 6796568, 5529506, 4123033, 9226861,
         4160797, 7053808, 6376403, 1506518, 3515508, 2900951, 5672088, 1976504, 7015332, 7635407, 7008229, 4530820,
         7900961, 2430459, 2887319, 8241133, 3175011, 7337637, 6778802, 1687635, 4094145, 5523156, 4145825, 916583,
         2871174, 8662583, 886085, 2900533, 1502229, 923862, 8766484, 4722235, 9436774, 8974007, 1534471, 600954,
         3154757, 2943992, 2254508, 2553711, 7250881, 8289646, 9966601, 4971008, 2741824, 4711848, 2434508, 5917887,
         5283557, 8234505, 5379570, 6304706, 9382973, 925490, 7424789, 4760509, 630780, 6728958, 6308571, 4005162,
         2276742, 3261971, 2306155, 5912462, 3417871, 3995252, 5201218, 2624934, 3471041, 2126263, 425221, 2453962,
         453308, 5334724, 1539428, 8035010, 8089643, 9161941, 3954071, 126040, 5926323, 3693788, 990909, 9303433,
         7303022, 2546321, 1827307, 2137780, 6372951, 3182107, 2109019, 8100691, 5714676, 1904996, 847112, 1594057,
         3361613, 4040890, 8435705, 2240877, 4328741, 3624589, 5628251, 3988201, 9550528, 6469506, 7843101, 3183751,
         8045927, 1785417, 5801683, 4977533, 1673342, 3625472, 2636588, 4193485, 8652978, 3869275, 7115693, 6431152,
         3624714, 9806238, 3418604, 9428203, 81523, 7073860, 2995324, 1706207, 8064639, 9651622, 4485341, 3184563,
         4729966, 3707203, 4549259, 6111434, 9062270, 3469931, 6033292, 9807235, 312273, 1574127, 8793146, 8599580,
         8699956, 7015897, 367893, 6133245, 8372103, 4580820, 9257050, 4753632, 9812063, 6647001, 6159631, 452204,
         336953, 2049354, 2443838, 6100818, 8517848, 5030232, 9169879, 9672883, 3069031, 5230311, 4244428, 653557,
         6946731, 4690867, 9943931, 4781119, 1616515, 690108, 8527032, 2104097, 6415193, 6823669, 8453214, 2348685,
         8072460, 1099169, 2735007, 8535373, 5237395, 5291684, 7420260, 8550962, 97185, 2472850, 6695811, 3835122,
         6142977, 8564206, 3039938, 3701461, 7446398, 4432261, 6001582, 8583532, 8676821, 3467128, 4803762, 4377639,
         9177741, 159915, 4833690, 3237290, 5020433, 4814952, 7438725, 8371815, 2505227, 9863940, 1534049, 7235114,
         514875, 5465361, 7796752, 3190019, 706293, 378770, 9066095, 8002928, 2995247, 4443181, 3869534, 4596105,
         8747311, 6161892, 3780453, 7627741, 1021234, 2272664, 2373981, 3526731, 8152291, 7932653, 3609589, 9371275,
         9170870, 1700440, 5167535, 850265, 2509416, 4861928, 4108890, 2213171, 5634996, 3808238, 8288256, 3412538,
         8087987, 5358414, 2248326, 8392636, 6823484, 8213365, 2753769, 278683, 584154, 5987689, 6336192, 5893996,
         634100, 6726620, 6878963, 2846893, 955128, 223033, 4054760, 510239, 8891064, 3696360, 5087512, 1310239,
         8764381, 4704736, 354304, 4095121, 2017432, 4982872, 3055517, 6011670, 6348104, 8647800, 3987162, 7155476,
         698302, 2349567, 40767, 4164880, 1341277, 1289046, 8375208, 5546711, 3410579, 8355407, 2920861, 8164169,
         9427308, 885034, 7787444, 995331, 982275, 3717839, 6435910, 1424664, 2130842, 590786, 9008423, 923826, 5824119,
         3142139, 5603821, 6859704, 1846790, 5954739, 6822877, 5537113, 1883238, 4414518, 6147627, 9695334, 402988,
         7836019, 8445643, 1606156, 4632394, 8349887, 6603043, 6579170, 1665391, 162572, 9568802, 7538845, 2826653,
         2565892, 4709304, 7049767, 4002941, 276017, 1838471, 763238, 7160717, 4415810, 3540738, 4436939, 9006686,
         9945623, 8014052, 2934893, 7984660, 2059217, 1889299, 6035523, 756186, 837976, 1509570, 9327272, 2514362,
         2447973, 3093141, 6111569, 9042596, 7987814, 8319005, 6744468, 7979499, 4753690, 4634446, 412142, 8130140,
         5991641, 4743924, 3443395, 8518497, 2596821, 2962318, 6839523, 5002036, 4443175, 6837914, 7576261, 211299,
         7879978, 5570756, 1473115, 7912865, 9689718, 5464255, 2595810, 9007196, 4974015, 164805, 9617434, 268689,
         5730664, 3988933, 8614473, 2347761, 6968948, 169098, 5097060, 3035786, 6209664, 4393590, 9875443, 757192,
         4553485, 7974348, 6117700, 527355, 4268809, 8775422, 5384690, 8371879, 1413119, 8263584, 3759478, 6093026,
         640905, 5693968, 8538018, 5449290, 3797432, 9527281, 9618733, 26118, 7303893, 8130882, 3439212, 5833305,
         6141840, 2570315, 5872820, 7110579, 1304955, 8229926, 2404984, 4561685, 4922749, 3165323, 3733066, 8494543,
         475899, 5326060, 7222337, 1359659, 5258543, 5091851, 4145168, 2806516, 3377445, 7624692, 9167893, 6201289,
         1864500, 3820464, 4932305, 2430060, 6655282, 756664, 2078034, 8237262, 3670470, 5802306, 5097449, 4550486,
         5267557, 9750015, 1166801, 7990184, 7847196, 4422394, 4060936, 3441272, 6684813, 8166935, 5657517, 3907862,
         6346844, 4752603, 2654750, 4588553, 3286913, 5918526, 3688165, 4577593, 1373060, 6718238, 3314531, 6855473,
         6935242, 5793666, 5212591, 701723, 8594003, 6997983, 3532163, 5904737, 1339375, 2268243, 3748701, 4873343,
         6309392, 6595596, 1598729, 5745473, 5265307, 4926822, 3697346, 3950081, 7141421, 8764983, 8502818, 7781111,
         7288956, 3146502, 3040540, 5987031, 6485299, 5397362, 9623916, 8310197, 9059257, 5077109, 8620795, 7291127,
         8031343, 7710685, 2770175, 7143525, 5074823, 5436971, 4461132, 9816859, 8810083, 9749028, 2150335, 5003325,
         5937841, 2955281, 9607220, 1413260, 7471257, 1640407, 7737883, 3520783, 4199588, 96899, 5679580, 6291392,
         1416153, 3712397, 255640, 4201919, 9443573, 7747621, 9750148, 3402132, 2492655, 4458558, 5426441]

    print(Solution().totalHammingDistance(a))