#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#Vamos a considerar la red optica pasiva como
#una fuente de informacion discreta



#Para probar 
alf = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
num = (0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111)
Hex = dict(zip(alf, num))


'''
Hex = {	 0:'0', 1:'1', 10:'2', 11:'3', 100:'4', 101:'5',
	110:'6', 111:'7', 1000:'8', 1001:'9', 1010:'A',
	1011:'B', 1100:'C', 1101:'D', 1110:'E', 1111:'F'}
'''
		
bits = np.random.randint(2, size=100000)

bitCount = []
for n in [0, 1]:
	k = list(bits).count(n)
	bitCount.append(k)

plt.figure()
for i in [0, 1]:
	plt.bar([i], bitCount[i])

plt.xticks([0, 1], ['0', '1'])
plt.title('Bit occurrences: Passive optical network simulation')
plt.ylabel('Bit rate random distribution')
plt.xlabel('Bits')
plt.show()
plt.save('./saves/bits.png')







