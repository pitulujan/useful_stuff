import numpy as np
import plotly
import plotly.graph_objs as go

#human=[1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
human=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#pred=[0.99495077,0.99003577,0.967879,0.961321,0.95545518,0.9380002,0.92304438,0.89999533,0.89013481,0.75337273,0.7274664,0.71306813,0.70426112,0.69134212,0.64295697,0.58826309,0.54354703,0.53859508,0.50757229,0.4280808,0.40622327,0.39703402,0.3619625,0.35666329,0.34817493,0.32479161,0.31744358,0.29971516,0.29379517,0.28226212,0.27624473,0.25776327,0.2547791,0.23838229,0.20526864,0.18951584,0.14818035,0.14754875,0.10877646,0.10578647,0.10430827,0.10362618,0.0963476,0.09600912,0.09037148,0.08928362,0.08600342,0.08381057,0.08336438,0.07887153,0.07785273,0.07513297,0.07413775,0.073962,0.07006582,0.06719338,0.06092214,0.05691037,0.05631018,0.05575538,0.05434696,0.04983854,0.04774934,0.04747128,0.04703354,0.04573681,0.04569092,0.04536905,0.04529282,0.04487643,0.04174899,0.04035146,0.0385563,0.03789528,0.03671287,0.03498545,0.0325367,0.03238676,0.03182875,0.03052442,0.03004322,0.02980619,0.02980084,0.02580278,0.02568285,0.02567445,0.02543844,0.02540255,0.02514908,0.02411849,0.02353584,0.02195843,0.02152951,0.02076722,0.01763428,0.01744882,0.0166555,0.01558327,0.01553866,0.01547055,0.01531105,0.01525652,0.01522939,0.01514714,0.01473448,0.01450471,0.01438344,0.01432076,0.01335833,0.01276994,0.01256607,0.01162332,0.01096248,0.01024698,0.01019179,0.01015629,0.00936104,0.0084996,0.00824201,0.00819532,0.00811525,0.00760231,0.00740392,0.00720088,0.00708597,0.0070554,0.00704544,0.00680009,0.00670008,0.00663708,0.00591505,0.00583393,0.00568064,0.00542003,0.00541583,0.00539256,0.00519696,0.00510551,0.00510501,0.00505992,0.00499339,0.00494416,0.00458924,0.00446414,0.00445538,0.00441362,0.00438804,0.00436893,0.00432189,0.00421588,0.00400643,0.0039911,0.00387174,0.00383164,0.00377026,0.00350658,0.00350521,0.00342172,0.00322224,0.00318342,0.00317294,0.00313618,0.00302549,0.0029621,0.00278213,0.00276694,0.0027053,0.00264427,0.00260641,0.00260514,0.00258435,0.00256932,0.00253922,0.00253922,0.00253091,0.00252764,0.00252307,0.00245261,0.00240859,0.00228752,0.00227075,0.00222676,0.00207178,0.002047,0.00203526,0.00201345,0.00197152,0.00196738,0.00194628,0.00193926,0.00193046,0.00192252,0.00192119,0.00191583,0.00190542,0.00190033,0.00189764,0.00189736,0.0018891,0.00186329,0.00182611,0.00181963,0.00181914,0.00179614,0.00179232,0.00178788,0.00172214,0.00166881,0.00166477,0.00165834,0.00165534,0.00163072,0.00162207,0.00158498,0.00157386,0.00153821,0.00152846,0.00148438,0.00147822,0.0014721,0.00144038,0.00143628,0.00139304,0.00138265,0.00138265,0.00137797,0.00134221,0.00130755,0.00130058,0.00124715,0.00119467,0.00116044,0.00115496,0.00114317,0.00114031,0.00113932,0.00111238,0.00102489,0.001015,0.00100357,0.0009949,0.00098171,0.00096982,0.00095594,0.0009336,0.00092728,0.0009113,0.00090815,0.00090687,0.00090361,0.00090084,0.00090073,0.00089503,0.00089337,0.00088101,0.00083987,0.00079172,0.00079117,0.00078281,0.00075975,0.00074066,0.00073208,0.00072499,0.00071112,0.00070951,0.00069611,0.00068112,0.00067533,0.00067359,0.00067121,0.00065786,0.00064388,0.00063043,0.00062466,0.00061825,0.00061446,0.00059225,0.00058546,0.00057994,0.00056088,0.00054264,0.00053903,0.00053649,0.00052987,0.00052474,0.0005133,0.00050147,0.00049216,0.00049143,0.00048844,0.00047609,0.0004751,0.00047196,0.00047101,0.00046343,0.00045797,0.00045574,0.00044864,0.00044319,0.00043167,0.00043143,0.00041341,0.00039104,0.00038946,0.0003817,0.00036616,0.0003598,0.0003553,0.00035264,0.00035219,0.00033246,0.0003283,0.00032606,0.00032323,0.00031775,0.00031725,0.0003139,0.00031088,0.00029925,0.00028603,0.000276,0.00027272,0.00026633,0.00026197,0.00025678,0.00024797,0.00024764,0.00024343,0.00023943,0.0002357,0.00023432,0.00023428,0.0002313,0.0002304,0.00022582,0.0002232,0.00022027,0.00021565,0.0002109,0.0002084,0.00020424,0.00020174,0.00020032,0.00019984,0.0001997,0.00019772,0.00019706,0.00019492,0.00019334,0.00019218,0.0001912,0.0001907,0.00019047,0.00018924,0.00018896,0.00018412,0.00018382,0.00018256,0.00018155,0.00017396,0.00016789,0.00016666,0.00016254,0.00016225,0.00016208,0.00015946,0.00015648,0.00015371,0.00015044,0.0001491,0.00014887,0.00014774,0.00014433,0.00013431,0.00013404,0.00012836,0.00012641,0.00012555,0.00012454,0.00012124,0.00011654,0.00011459,0.00011381,0.00011276,0.00010746,0.00010667,0.00010615,0.00010484,0.00010258,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pred=[0.90686524,0.97466236,0.9865154,0.96491855,0.93714786,0.66641563,0.96820706,0.32192194,0.88495624,0.9264947,0.98050714,0.95933735,0.93808424,0.9354981,0.7624677,0.9719248,0.66269135,0.66269135,0.2789184,0.84478927,0.9578849,0.39887178,0.36206365,0.9838705,0.98672014,0.9707334,0.8241213,0.9093908,0.6933262,0.08338363,0.98862594,0.648973,0.99466324,0.99696904,0.99521625,0.50122446,0.8748932,0.42956835,0.9842576,0.9782216,0.96120125,0.7241925,0.6881472,0.9893937,0.961068,0.97974795,0.07449366,0.13387121,0.5304638,0.08551219,0.28783175,0.11144241,0.71447235,0.31828445,0.8437226,0.5666732,0.85688275,0.94649786,0.5666732,0.8096969,0.70182896,0.9156585,0.17753208,0.88380224,0.66897005,0.09042821,0.9576277,0.44872862,0.8915332,0.9851614,0.94767654,0.9920328,0.48551816,0.96680796,0.048913263,0.9888121,0.10778522,0.39764103,0.98257345,0.8241357,0.1702407,0.16474836,0.04900371,0.24454895,0.007518576,0.024598306,0.025285473,0.014443582,0.9240224,0.008454585,0.09065061,0.13686612,0.017740155,0.01711442,0.03249405,0.005046549,0.4393372,0.007329381,0.004109941,0.009603306,0.14251395,0.05585028,0.027361779,0.018098682,0.031849835,0.5586279,0.015153328,0.228848,0.3099526,0.046496857,0.011144398,0.010547642,0.02211087,0.3203222,0.34302607,0.24151911,0.5166508,0.00509467,0.27882132,0.108277716,0.05068857,0.012297728,0.15816621,0.11955715,0.024414355,0.08717896,0.087496884,0.021490594,0.04929051,0.10381517,0.04399455,0.98601264,0.327161,0.048442345,0.27312317,0.96920985,0.07043674,0.028535403,0.102069154,0.9822045,0.98360264,0.05736726,0.120761186,0.10749648,0.6886029,0.19282249,0.10541811,0.05933464,0.14664677,0.03302493,0.39439848,0.5151296,0.07374425,0.13977249,0.48971212,0.30331498,0.2868064,0.1679929,0.41464958,0.09965518,0.3270251,0.42022994,0.18443973,0.11421501,0.16608292,0.07834512,0.707894,0.097470134,0.119094625,0.10194838,0.83265334,0.4718403,0.19018802,0.39140326,0.14446688,0.9005852,0.5633696,0.25466436,0.17188716,0.3556889,0.73883325,0.26692265,0.018462664,0.9645019,0.13473287,0.9813479,0.011288435,0.6724073,0.929865,0.2956993,0.19317603,0.23335473,0.07082878,0.92368746,0.027791534,0.4068626,0.4310636,0.10988392,0.14436063,0.10787405,0.11576188,0.03314058,0.85854876,0.09088466,0.052359786,0.10019859,0.056577694,0.048362676,0.122229844,0.032388717,0.159601,0.07489617,0.30399308,0.6090619,0.029330866,0.0863364,0.13414314,0.0661006,0.058572564,0.07890575,0.07912781,0.06071292,0.035518244,0.033690613,0.067968175,0.058564387,0.16312574,0.37792706,0.12942947,0.0399538,0.05773491,0.48240966,0.11993156,0.061715256,0.0640511,0.48298153,0.059673876,0.13215211,0.08068889,0.04644735,0.29904523,0.12464397,0.055661615,0.13771826,0.1639421,0.122668214,0.11468398,0.50987226,0.16613631,0.0606032,0.03292414,0.030291233,0.1253112,0.06341402,0.051757872,0.030918028,0.41446355,0.11966338,0.064275526,0.051569767,0.05636701,0.07449938,0.052528866,0.16874781,0.08037209,0.070373476,0.1075907,0.07287975,0.17066482,0.101808876,0.1704214,0.015388957,0.003215755,0.006586776,0.9328303,0.8536819,0.00396937,0.006360852,0.005735051,0.008287898,0.009867526,0.014631846,0.008440705,0.009734178,0.002930097,0.004778072,0.00760881,0.008409454,0.00998786,0.011539544,0.002884935,0.007111307,0.002910872,0.008072508,0.00609502,0.014415264,0.019860417,0.008932647,0.015472876,0.006781669,0.015106132,0.010140061,0.005204571,0.015604099,0.007171485,0.004074226,0.003648787,0.007993698,0.009313172,0.007582712,0.008127053,0.012648664,0.007755768,0.005451361,0.005574118,0.028797919,0.009145743,0.006247141,0.003430303,0.007126167,0.2952864,0.005299941,0.011580654,0.004640703,0.010066434,0.003080238,0.011995991,0.007883327,0.008177199,0.007062067,0.007179454,0.00520571,0.003436776,0.004645639,0.003602398,0.01748263,0.013152459,0.009425719,0.004902476,0.070876986,0.006051413,0.25911763,0.5586279,0.01967144,0.2535536,0.3099526,0.013478701,0.013478701,0.08067678,0.7920024,0.1607009,0.008290516,0.34302607,0.00509467,0.029041626,0.07689239,0.108277716,0.09299724,0.00716826,0.002201872,0.8095291,0.021490594,0.021404635,0.33997157,0.9156585,0.015292031,0.17259862,0.005046549,0.09378354,0.046674892,0.009236953,0.17890573,0.08067678,0.21972874,0.3340827,0.061585456,0.008294437,0.09489137,0.09286795,0.024660943,0.005222603,0.115954116,0.011199196,0.037493326,0.6161589,0.16945766,0.014541672,0.015864,0.02824915,0.039092887,0.5539596,0.06911586,0.01709779,0.047820807,0.958935,0.03104226,0.021805998,0.022098992,0.023002433,0.0347204,0.08102829,0.12866992,0.6177947,0.044404663,0.043969654,0.010775175,0.020119622,0.022141982,0.38791206,0.6207751,0.100903,0.96585757,0.0839595,0.1066167,0.22848345,0.15928139,0.19323087,0.10582195,0.27772376,0.3395285,0.68198293,0.2486423,0.16071227,0.048469927,0.038284987,0.08368178,0.02570079,0.102540724,0.028654745,0.027561482,0.027472576,0.1702407,0.24146333,0.5030702,0.050922472,0.6689637,0.9670187,0.96322745,0.20548403,0.4406905,0.4553534,0.75293636,0.67242694,0.14348634,0.9821976,0.9280921,0.97640455,0.34632185,0.98130864,0.85703313,0.94008225,0.9401851,0.96899945,0.96502054,0.9689034,0.42809355,0.9850503,0.9829798,0.9429899,0.36703786,0.39848614,0.9782581,0.9782581,0.97694325,0.97604954,0.01794767,0.31058794,0.02022886,0.2510459,0.17652127,0.18176565,0.2853982,0.09325867,0.26707557,0.70347786,0.9526321,0.98049736,0.9921813,0.16810618,0.66815305,0.50445145,0.26211798,0.58058023,0.97914326,0.96697515,0.8007623,0.9304183,0.98230517,0.9514415,0.9117497,0.13571043,0.620507,0.070342354,0.19404344,0.76996773,0.8300578,0.85469955,0.4453592,0.88495046,0.33009362,0.6586908,0.9057834,0.11615468,0.7206364,0.9213281,0.97153497,0.9708436,0.9450645,0.6696053,0.8115337,0.9799646,0.8162393,0.51060843,0.7104761,0.21680741,0.928235,0.9367221,0.9832575,0.7104761,0.07316507,0.017360162,0.71097,0.033631686,0.4378205,0.4047515,0.43727243,0.20099401,0.014065703,0.3707858,0.029546253,0.10215204,0.06989362,0.006506014,0.05665979,0.010734534,0.001196268,0.006435846,0.004208405,0.021285528,0.005615599,0.24560453,0.003438542,0.02876094,0.004491441,0.11360939,0.014613342,0.008411382,0.007614282,0.032479797,0.04675975,0.13035339,0.002346824,0.049711633,0.010432241,0.04717122,0.020903345,0.010712606,0.015933681,0.012368636,0.007116839,0.11224563,0.0065267,0.004678515,0.002815266,0.015303184,0.04266197,0.5841037,0.039658904,0.7891704,0.627658,0.015044961,0.04969237,0.051666964,0.07180563,0.19975585,0.0302157,0.052068707,0.021772431,0.023226094,0.51724434,0.51724434,0.51724434,0.04415507,0.010567228,0.859893,0.9575336,0.76527524,0.19357897,0.17913699,0.05671475,0.49292028,0.9753289,0.4923112,0.18621626,0.11437261,0.018615428,0.3905585,0.04237756,0.082203984,0.08843948,0.072707936,0.30281302,0.18052353,0.22561924,0.22049609,0.041965052,0.09116539,0.046489608,0.2243708,0.07351276,0.18873449,0.033301227,0.012727877,0.08724117,0.15712503,0.09805589,0.8592182,0.80128133,0.81253433,0.34864354,0.036882937,0.13930342,0.05151957,0.06845213,0.47913054,0.31647277,0.047686465,0.03786729,0.61518097,0.21520725,0.08914189,0.26687545,0.91750854,0.083145894,0.54495215,0.8922378,0.7875156,0.07361232,0.05473509,0.2676584,0.076297715,0.097466104,0.02264577,0.065030396,0.36881995,0.11956809,0.117654,0.010092983,0.016280968,0.067394495,0.094692826,0.35325274,0.014201649,0.33534682,0.04859325,0.07771086,0.24422753,0.20311382,0.02430019,0.6965899,0.084077634,0.0484422,0.014842906,0.02807114,0.067434855,0.010307177,0.2394544,0.03567596,0.012562648,0.008230277,0.038509257,0.14214902,0.062115766,0.4672965,0.02312911,0.089616135,0.011311274,0.43556422,0.09347169,0.068370014,0.10817662,0.22725405,0.054592703,0.006325636,0.79275703,0.04977415,0.034720037,0.1298531,0.11269127,0.06639363,0.09585667,0.083079346,0.014162462,0.020772895,0.13146381,0.04516394,0.04805809,0.1708803,0.018069962,0.02679002,0.30685467,0.011049503,0.04828382,0.07653809,0.027329657,0.54214114,0.106016606,0.013897928,0.0372413,0.13820972,0.028164988,0.01152877,0.07776456,0.09006767,0.12281876,0.048776947,0.1847022,0.025844889,0.01589984,0.41777223,0.001696982,0.00535072,0.003745618,0.005182067,0.006070821,0.001722693,0.00585732,0.00211918,0.000690377,0.057746854,0.002970781,0.108438395,0.003759378,0.005360753,0.001261361,0.005008046,0.001002734,0.004583742,0.61635244,0.001443084,0.002137254,0.003079832,0.006934782,0.002355708,0.001896143,0.005823004,0.000789414,0.001260419,0.002333969,0.001811832,0.004237298,0.002933295,0.002269872,0.037798926,0.001836729,0.002222352,0.002377566,0.003039887,0.002871776,0.002249266,0.013286779,0.003375355,0.003930222,0.004076713,0.005889324,0.004591943,0.002176812,0.004660321,0.015654389,0.007748825,0.001278104,0.008209813,0.006623856,0.001782086,0.00171735,0.002649962,0.002755081,0.002875895,0.003445399,0.001297131,0.006511462,0.006339925,0.00234241,0.003349855,0.004833184,0.000513353,0.007431231,0.006326859,0.004114595,0.001650215,0.003708969,0.005442464,0.002699562,0.002858342,0.001080774,0.001815174,0.016785577,0.2778006,0.009310373,0.03658538,0.004491441,0.019549245,0.008049684,0.001783838,0.1683122,0.008411382,0.002376652,0.008423785,0.115232095,0.008288851,0.042702537,0.032479797,0.034390572,0.014257927,0.03829645,0.051522337,0.049711633,0.12803014,0.03774707,0.013979971,0.016462862,0.009869841,0.012368636,0.07754122,0.4553111,0.008716966,0.07454543,0.010895054,0.00139819,0.6712849,0.018337637,0.001783838,0.07663425,0.007948046,0.03774707,0.014310297,0.010900374,0.015508394,0.07754122,0.001078949,0.010895054,0.06939733,0.31080046,0.21684511,0.11607083,0.03430179,0.011194719,0.01075701,0.17071712,0.08670988,0.21749741,0.8323371,0.052897755,0.030960672,0.07389588,0.14942756,0.8763077,0.096409366,0.008235537,0.09202654,0.13874747,0.006946512,0.010195832,0.012205885,0.018605338,0.06147201,0.07447015,0.005658113,0.879574,0.055362433,0.03823266,0.083762705,0.022698905,0.42725357,0.07447042,0.03287883,0.97037065,0.93199754,0.08838131,0.081456564,0.3713871,0.4047515,0.97919947,0.05671475,0.49292028,0.98649526,0.89801896,0.22618827,0.9898527,0.98042196,0.8410097,0.80307144,0.94966507,0.46426287,0.96058136,0.99224794,0.17653112,0.962423,0.9800457,0.9585539,0.9485276,0.7131311,0.98770684,0.9732905,0.8735849,0.86540556,0.756374,0.78801006,0.8345256,0.55943066,0.29758677,0.16574118,0.98792994,0.7402624,0.7402624,0.60186905,0.9797437,0.9904669,0.95260614,0.86729014,0.88143945,0.15275064,0.30266163,0.82969517,0.23275879,0.9837871,0.6573269,0.9960716,0.79373354,0.96840894,0.9839138,0.67309105,0.95242155,0.98819005,0.9519191,0.97254395,0.17019376,0.7283414,0.14339826,0.04140633,0.60813004,0.716218,0.9509044,0.76685244,0.87122244,0.94211394,0.97883385,0.9119393,0.70167434,0.7179685,0.83408666,0.68370366,0.94479203,0.17129365,0.9184882,0.94508135,0.98645985,0.3714541,0.9569901,0.85440934,0.95206994,0.97434324,0.93903553,0.07718883,0.010176283,0.71587276,0.17577074,0.18789548,0.04403317,0.036577433,0.93903553,0.06832883,0.07277226,0.32956222,0.3447103,0.004446847,0.027190052,0.011515675,0.009786495,0.021737952,0.9166176,0.007823881,0.005145244,0.011288516,0.9351616,0.004375562,0.069609396,0.06759897,0.38792703,0.16451311,0.013496981,0.021204898,0.012884709,0.007146669,0.2636976,0.04980157,0.005916072,0.39172736,0.014880661,0.008110066,0.008698287,0.004199314,0.018849976,0.033666234,0.2981117,0.08613776,0.974935,0.24643414,0.28802207,0.3113809,0.9420734,0.052624542,0.76168877,0.40898046,0.40898046,0.9688191,0.28637117,0.023688093,0.062201176,0.98661196,0.05323147,0.01487915,0.31008166,0.53995305,0.3944484,0.2362136,0.038620383,0.06469673,0.096471354,0.6765957,0.47456434,0.26104808,0.1706122,0.21490827,0.10610512,0.47092512,0.13799721,0.17374107,0.073251896,0.21181436,0.3369309,0.22413726,0.20257688,0.3745246,0.066398315,0.27891067,0.22199684,0.26063502,0.11272953,0.09490301,0.51115483,0.50740933,0.15023977,0.078231215,0.03699199,0.57403874,0.032753617,0.19816913,0.03348663,0.23465589,0.06836368,0.6067918,0.1975228,0.7105812,0.05018492,0.10702859,0.27961263,0.1653511,0.045832604,0.67418784,0.7148121,0.02796473,0.016005993,0.07886358,0.021791197,0.040587857,0.010582335,0.056768242,0.35741013,0.039902616,0.07370327,0.029321404,0.42229164,0.22941595,0.0317303,0.23654717,0.050986107,0.05471938,0.026897188,0.4965589,0.05052532,0.5154548,0.11932727,0.07540692,0.1095379,0.067694925,0.020431975,0.3993138,0.027680509,0.07304037,0.098456636,0.03207106,0.023121573,0.020113597,0.021688676,0.18532366,0.010794965,0.23435009,0.31740132,0.029686343,0.030583272,0.1819507,0.10669364,0.09029141,0.6842764,0.16397722,0.055305183,0.14113465,0.58897525,0.036683835,0.12127728,0.030197978,0.0691335,0.16447642,0.10564424,0.040634498,0.0769422,0.049329888,0.074140854,0.09083042,0.06977183,0.15104757,0.02241674,0.032645687,0.055753842,0.030710468,0.24868442,0.1572943,0.111002795,0.020543456,0.16380331,0.068289846,0.053317763,0.18703856,0.38745835,0.15991141,0.09207646,0.41109753,0.007353028,0.006471972,0.002172216,0.018528987,0.00754205,0.002658242,0.002117422,0.001798634,0.011190387,0.001931287,0.003024756,0.002226872,0.001704045,0.001756174,0.003128244,0.006887407,0.002848976,0.004437971,0.003202333,0.003995507,0.003963407,0.007229094,0.004186292,0.004074749,0.007525581,0.01517291,0.005157698,0.003861248,0.007065869,0.01541766,0.005418338,0.006015859,0.002347843,0.005618427,0.015876288,0.010702973,0.007794313,0.001762341,0.00763794,0.003814528,0.003298339,0.003015638,0.001707673,0.006704568,0.023795264,0.004007112,0.015574515,0.014607878,0.017366672,0.003746707,0.004243914,0.00338992,0.002873584,0.005942965,0.007483694,0.01390884,0.004008247,0.006014119,0.002559355,0.005134759,0.004538158,0.003551019,0.0421324,0.004225669,0.006520133,0.005579915,0.004970724,0.004742045,0.3619886,0.004725258,0.007427212,0.10101676,0.004954296,0.057021704,0.010811786,0.021838166,0.00656243,0.06759897,0.045902412,0.032200504,0.035606485,0.02737675,0.007146669,0.013435818,0.24732141,0.33282846,0.071595855,0.0926131,0.04092633,0.086913675,0.14962424,0.005916072,0.006140444,0.17842636,0.01737438,0.08000398,0.026822615,0.008161489,0.008698287,0.004199314,0.018849976,0.008992769,0.08242534,0.1258373,0.16165932,0.00656243,0.05389106,0.38792703,0.002842279,0.021665027,0.04980157,0.19605939,0.024820806,0.057892594,0.009370867,0.055133484,0.002504811,0.2981117,0.015003172,0.19203256,0.021545202,0.040210966,0.009666276,0.030650863,0.075218014,0.9323273,0.06281883,0.98490715,0.007225543,0.027550995,0.06809837,0.026667856,0.040106483,0.04426059,0.08368423,0.60169595,0.014428311,0.01022782,0.23231164,0.006132585,0.076940596,0.026325567,0.08277299,0.021201147,0.039519425,0.457552,0.2723706,0.011346705,0.06527248,0.08149808,0.11927423,0.23112263,0.37406132,0.66421616,0.07923377,0.15220034,0.4710296,0.054126024,0.029994704,0.058517173,0.7055691,0.218107,0.041899387,0.03899068,0.07718883,0.010176283,0.35952973,0.34716025,0.048145868,0.9903576,0.97880507,0.11227171,0.16701241,0.15142578,0.07441752,0.16397117,0.138841,0.53959656,0.17093387,0.71587276,0.8910666,0.05323147,0.37196195,0.9853431,0.18358676,0.9764939,0.6795728,0.4565862,0.09661303,0.21326192,0.9823528,0.9519528,0.075876504,0.84767586,0.9416297,0.96922773,0.32109213,0.6160442,0.8468907,0.10035243,0.83582634,0.89468825,0.83575654,0.6272408,0.9907101,0.9351442,0.8701757,0.18155494,0.93976927,0.97139984,0.91278565,0.9827839,0.3145681,0.9927619,0.99027985,0.7437361,0.9907554,0.039252862,0.9722768,0.98690575,0.986844,0.97893757,0.96851313,0.9826347,0.95747566,0.22233823,0.8339629,0.835168,0.873687,0.087316826,0.5947638,0.9461603,0.8468907,0.8942199,0.69217306,0.9266871,0.9679778,0.122393675,0.14101027,0.9873432,0.6008411,0.50873095,0.98507476,0.96965563,0.21679097,0.111646585,0.9871012,0.98946303,0.9690504,0.9828668,0.9649021,0.1097198,0.9907101,0.9813618,0.97218275,0.98727256,0.9846311,0.9896778,0.9792644,0.013877803,0.2588595,0.026774682,0.032,0.840314,0.113292255,0.046044476,0.06981102,0.007321825,0.41938543,0.004848883,0.007193666,0.21459696,0.015081373,0.006700006,0.002199708,0.005287404,0.13273413,0.059228465,0.05073218,0.07384835,0.9331655,0.2814477,0.020924382,0.010298362,0.023330297,0.005583816,0.003533347,0.007259513,0.041190688,0.007808453,0.007961298,0.013844385,0.6856621,0.007441988,0.039090496,0.033137385,0.018531803,0.054095868,0.008881893,0.42174035,0.06541134,0.06979812,0.01721911,0.015080736,0.6784482,0.42063543,0.15251152,0.026882786,0.21262504,0.050884508,0.57518333,0.17461236,0.035287417,0.1615936,0.011530845,0.08023457,0.5374693,0.08922841,0.06950123,0.5354978,0.023647098,0.5264262,0.9800969,0.6707817,0.25287727,0.59893936,0.020476725,0.054928813,0.982667,0.9846311,0.2643206,0.19530606,0.09253054,0.33134264,0.22485848,0.08958631,0.057672203,0.13771664,0.017834952,0.20281541,0.2520977,0.1500889,0.105311915,0.28614655,0.46968305,0.17401052,0.4826138,0.18116705,0.15377586,0.03192156,0.04015532,0.098401085,0.13273554,0.082441084,0.1679785,0.018946718,0.21683168,0.043908954,0.40920466,0.3466831,0.38565406,0.045806535,0.056442373,0.09637829,0.38376975,0.2503846,0.5485846,0.82693654,0.18659043,0.6078993,0.23822398,0.032851245,0.74604785,0.042311914,0.08984366,0.16194502,0.011645973,0.6132754,0.14535403,0.21220289,0.073028244,0.038437746,0.2467388,0.11894533,0.070026614,0.07775907,0.02678538,0.25817624,0.08331641,0.040310644,0.034374095,0.803411,0.09409034,0.035920925,0.081133515,0.32591742,0.501253,0.5902785,0.104131244,0.006587266,0.04469348,0.047304176,0.07982037,0.020911194,0.28146005,0.009085931,0.08350192,0.066643566,0.026731102,0.09276159,0.035380155,0.13202678,0.030053487,0.06310583,0.049358986,0.034968063,0.023654062,0.03085182,0.0462501,0.026343975,0.04778137,0.1493956,0.15863667,0.04574561,0.1842103,0.18061328,0.017641796,0.05347729,0.20694385,0.16149099,0.034869123,0.23087408,0.03665063,0.09117762,0.024901832,0.19619279,0.04350223,0.06722011,0.0333045,0.1156156,0.21385866,0.029392548,0.04616843,0.051898006,0.039195098,0.014597476,0.020602763,0.011908401,0.06757234,0.040163945,0.011038008,0.00343317,0.027907165,0.019329397,0.003623723,0.006336111,0.009417802,0.004578434,0.003597692,0.007108853,0.006597492,0.0053225,0.011744772,0.03184943,0.005319805,0.018671896,0.003324636,0.005282854,0.004042423,0.004052923,0.016876603,0.009982547,0.004595127,0.028130334,0.004981573,0.005605054,0.00419301,0.015123901,0.009869971,0.006380955,0.006086778,0.013383118,0.0076928,0.006432923,0.00595158,0.002965625,0.623754,0.008923639,0.004498907,0.012408945,0.005604403,0.010804894,0.01354753,0.006807548,0.004875214,0.002303633,0.09516067,0.005638697,0.01543529,0.008886541,0.00297217,0.003712278,0.003859381,0.007981181,0.005832909,0.004011507,0.012123933,0.004901618,0.00515518,0.01004689,0.008137989,0.012308784,0.002043856,0.02227863,0.014847627,0.03915873,0.003640156,0.010996081,0.005643474,0.005707629,0.13273413,0.002875754,0.4788588,0.05073218,0.003031836,0.025549129,0.010622852,0.055960473,0.36599243,0.003533347,0.007259513,0.007320412,0.011432778,0.13430063,0.007967979,0.007808453,0.003269577,0.040078744,0.020971479,0.4366719,0.018531803,0.00640835,0.003280768,0.028191404,0.17450182,0.0044,0.01157942,0.015080736,0.2814477,0.012954451,0.004831544,0.004747905,0.010298362,0.01528801,0.055960473,0.20140342,0.007459192,0.020971479,0.01057382,0.15132993,0.09073376,0.003380124,0.21033044,0.010146112,0.007205632,0.001999357,0.16323274,0.010944738,0.009996804,0.007035274,0.022594083,0.014870899,0.1723517,0.046314728,0.015125521,0.007855239,0.008393703,0.02220946,0.009152707,0.004401669,0.016220545,0.025472008,0.94818515,0.020950885,0.20953283,0.0586099,0.013913012,0.02320858,0.23468561,0.039416578,0.9656331,0.025751077,0.6669158,0.49872747,0.46527126,0.11087681,0.27337575,0.05179629,0.17727771,0.33082458,0.20662537,0.15333857,0.29137176,0.054265484,0.392722,0.056317896,0.0348311,0.044573866,0.18744196,0.33420122,0.17114069,0.08707932,0.033137694,0.09417465,0.013877803,0.10816833,0.032,0.937426,0.04581404,0.46947667,0.073901676,0.19429827,0.16168913,0.0152204,0.027778381,0.64015144,0.80833817,0.97416997,0.9714944,0.7916619,0.92438114,0.8631168,0.57996756,0.9624299,0.8551949,0.9337537,0.56160295,0.19932176,0.95685947,0.32270157,0.9528118,0.2828355,0.9411209,0.8997418,0.88047755,0.7042815,0.21648584,0.8164049,0.9755528,0.9662251,0.6475108,0.9631609,0.4216858,0.9643511,0.5828264,0.6820032,0.43493685,0.8563786,0.073029906,0.034372494,0.4768557,0.05643777,0.48211432,0.9855299,0.48717168,0.96480954,0.96418166,0.87539244,0.9729934,0.9589378,0.96259433,0.8671304,0.9348833,0.819811,0.24137361,0.40104765,0.06747524,0.07245479,0.8453629,0.22379881,0.1905944,0.44106773,0.12744626,0.4812226,0.79076487,0.7332112,0.95468086,0.070571594,0.3291556,0.4052307,0.9604735,0.871728,0.94276446,0.95585376,0.46932593,0.9643511,0.9430697,0.92499965,0.8883045,0.43321666,0.9662387,0.32922712,0.9411209,0.48724326,0.31541562,0.082774855,0.03476715,0.105001844,0.7668778,0.010356255,0.1886185,0.021587236,0.017848738,0.08941931,0.08069955,0.010315235,0.057194047,0.02872466,0.18428181,0.04586885,0.017758394,0.09070429,0.12779501,0.12494423,0.031353872,0.034509342,0.085280925,0.106034726,0.0869645,0.036720976,0.016303495,0.06476926,0.04151854,0.065582186,0.113801114,0.05185108,0.04332329,0.092796005,0.12459789,0.8152464,0.3303574,0.4999027,0.931692,0.098536015,0.13202743,0.13058902,0.26738566,0.265135,0.3964973,0.37036026,0.44892582,0.27187455,0.12698516,0.6600774,0.8982479,0.34846333,0.50832576,0.08340165,0.44474077,0.3332138,0.51754105,0.07953018,0.30674466,0.42115262,0.63901734,0.050743382,0.10903356,0.0856096,0.03843965,0.2286018,0.04696652,0.18548198,0.04349759,0.06849972,0.027248941,0.65199745,0.14702587,0.18679777,0.12837541,0.028508527,0.25903007,0.09973045,0.071011595,0.22201228,0.7751396,0.62781864,0.45671895,0.6156472,0.28828168,0.31570345,0.45471472,0.3809754,0.4248503,0.6009936,0.54673404,0.3435344,0.5300888,0.58689374,0.36224633,0.96858627,0.0828757,0.07920539,0.044307988,0.25293842,0.042814966,0.27248445,0.34133977,0.37303075,0.3320524,0.34344926,0.419884,0.071461126,0.56724095,0.15182704,0.2320857,0.0946425,0.19233276,0.17218828,0.11699415,0.32411283,0.05989502,0.22507603,0.05477563,0.0735805,0.06345904,0.09070923,0.07510303,0.051095344,0.1324515,0.04269966,0.053522162,0.07238008,0.10267618,0.08116666,0.1583892,0.18026017,0.065232694,0.06111229,0.09822444,0.09324209,0.10500543,0.7037795,0.05668452,0.056427263,0.03384689,0.114063926,0.06126261,0.043102164,0.09707789,0.1612822,0.030754022,0.20099425,0.0457803,0.05530928,0.14282684,0.051028144,0.018541621,0.22407869,0.1542705,0.061281193,0.46801457,0.15936203,0.045573734,0.009013091,0.011434567,0.009573979,0.01231308,0.2834669,0.30998063,0.008236016,0.008145313,0.010725504,0.03775069,0.007114511,0.014078306,0.00433181,0.009224228,0.008256158,0.012992522,0.01442204,0.005103524,0.015352923,0.012747643,0.006484994,0.018212922,0.006100536,0.014228765,0.005777217,0.005800385,0.010170493,0.014965014,0.008386705,0.006435373,0.005490259,0.14491299,0.005830589,0.007195361,0.008447232,0.02514511,0.014502762,0.012413329,0.008328774,0.007351319,0.019811662,0.016587678,0.011399968,0.008860934,0.011090648,0.004148934,0.008465828,0.014836639,0.00740161,0.009172877,0.029183408,0.007618387,0.013727833,0.014544735,0.004810228,0.007021663,0.014200847,0.006584645,0.008127964,0.027756033,0.006875024,0.006005779,0.010951811,0.007519857,0.003389316,0.005784147,0.011842692,0.0154114,0.76177657,0.006316633,0.009373904,0.006510861,0.005716912,0.012100454,0.014487069,0.007149362,0.006525002,0.01592451,0.021005252,0.008635377,0.008263994,0.009737175,0.006329572,0.38862833,0.008524629,0.010223805,0.0722278,0.0780273,0.12570517,0.079137996,0.16016547,0.16016547,0.03259458,0.021967344,0.029436478,0.115484886,0.09070429,0.12779501,0.33639306,0.021698097,0.026942348,0.059456363,0.068371624,0.013921663,0.017266273,0.12279644,0.13640825,0.16108891,0.18231423,0.016568607,0.32009602,0.31809112,0.024079077,0.053289298,0.058201227,0.05214149,0.04332329,0.00526231,0.011677282,0.07440546,0.019270292,0.04933231,0.3870673,0.42562252,0.009431683,0.079137996,0.16016547,0.04468197,0.40638188,0.017758394,0.25062105,0.034581155,0.034097176,0.008292771,0.104193635,0.016303495,0.013921663,0.21365426,0.31809112,0.058201227,0.051756054,0.348533,0.012222303,0.014358332,0.017919753,0.01836957,0.015048912,0.090551816,0.014965314,0.012344522,0.023450103,0.02138149,0.03657722,0.7443122,0.6730627,0.01645289,0.1450847,0.068009,0.07237623,0.028118199,0.02799381,0.03771247,0.14910072,0.019423049,0.42610773,0.13381647,0.39655194,0.0846432,0.61719805,0.02833508,0.540594,0.1398491,0.07061475,0.24491091,0.071527205,0.1950287,0.19369036,0.1668233,0.14456476,0.25193265,0.42990664,0.08138948,0.019528989,0.06448413,0.056459684,0.68478084,0.7710968,0.18519476,0.14931765,0.07856338,0.080515176,0.31541562,0.12718691,0.5544194,0.7945316,0.35096803,0.34588212,0.63141406,0.6124072,0.31367397,0.31541562,0.060423464,0.40428483,0.97331816,0.34846333]


def graphic_stuff(human,pred):
	calcs={}

	x=np.arange(0.0, 1.0, 0.01)
	recall_vector=[]
	precision_vector=[]
	f1_vector=[]
	for threshold in x:
		aux=[]
		pred_pos_real_pos=0
		pred_pos_real_neg=0
		pred_neg_real_pos=0
		pred_neg_real_neg=0

		for idx,prediction in enumerate(pred):
			if prediction > threshold:
				aux.append(1)
				if human[idx]==1:
					pred_pos_real_pos+=1
					
				else:
					pred_pos_real_neg+=1
					
			else:
				aux.append(0)
				if human[idx]==0:
					pred_neg_real_neg+=1
					
				else:
					pred_neg_real_pos+=1
					

		calcs[str(round(threshold,2))]={'binary_pred':aux}
		calcs[str(round(threshold,2))]['pred_pos_real_pos']=pred_pos_real_pos
		calcs[str(round(threshold,2))]['pred_pos_real_neg']=pred_pos_real_neg
		calcs[str(round(threshold,2))]['pred_neg_real_pos']=pred_neg_real_pos
		calcs[str(round(threshold,2))]['pred_neg_real_neg']=pred_neg_real_neg
		
		recall   = pred_pos_real_pos/(pred_pos_real_pos+pred_neg_real_pos)
		precision= pred_pos_real_pos/(pred_pos_real_pos+pred_pos_real_neg)
		f1       = 2*recall*precision/(recall+precision)
		accuracy = (pred_pos_real_pos+pred_neg_real_neg)/(pred_neg_real_neg+pred_pos_real_pos+pred_pos_real_neg+pred_neg_real_pos)

		calcs[str(round(threshold,2))]['recall']=recall
		calcs[str(round(threshold,2))]['precision']=precision
		calcs[str(round(threshold,2))]['f1']=f1
		calcs[str(round(threshold,2))]['accuracy']=accuracy
		recall_vector.append(recall)
		precision_vector.append(precision)
		f1_vector.append(f1)

	print(f1_vector,len(f1_vector))

	# Create traces
	trace0 = go.Scatter(
	    x = x,
	    y = f1_vector,
	    mode = 'lines+markers',
	    name = 'f1'
	)
	trace1 = go.Scatter(
	    x = x,
	    y = recall_vector,
	    mode = 'lines+markers',
	    name = 'recall'
	)
	trace2 = go.Scatter(
	    x = x,
	    y = precision_vector,
	    mode = 'lines+markers',
	    name = 'precision'
	)
	data = [trace0, trace1, trace2]


	plotly.offline.plot({
	    "data": data,
	    "layout": go.Layout(title="hello world")
	}, auto_open=True)


if __name__ == '__main__':
	graphic_stuff(human,pred)


