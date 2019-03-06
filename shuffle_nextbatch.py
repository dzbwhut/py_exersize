'''
1) shuffle 同步乱序dataset,lables;
2) 用next_batch获取样本的batch
'''

import numpy as np


'''
  shuffle 同步乱序dataset,lables;
  shuffle在原数据存储空间上乱序，无需返回值
'''
def data_labels_shuffle(dataset,lables):
	state = np.random.get_state()
	np.random.shuffle(lables)	
	
	np.random.set_state(state)
	np.random.shuffle(dataset)
		
	#return dataset,lables


'''
 用next_batch获取样本的batch
'''
def next_batch(dataset,lables,batch_size,echo_num):		
	for i in range(int(len(lables)/batch_size)):
		j=i*batch_size
		k=j+batch_size
		yield dataset[j:k]
		yield lables[j:k]

# 试验
a=np.array(range(10))
b=np.array(range(10,20,1))
data_labels_shuffle(a,b)
c=next_batch(a,b,5,10)

for i in c:	
	print(i)
