"""
 -------生成器函数-----------
 定义生成器函数generator与定义普通函数是一样的，
 唯一的不同生成器函数中有一个或多个yield，yield与return类似都是用来返回数据
 两者的区别:
     return -- 函数退出:   返回数据后直接退出当前函数，
     yield  -- 函数不退出: 将数据返回后仍然继续运行函数，
               因此,最后生成器函数返回的是一个迭代器对象。	
"""

def yield_test():	
	for i in range(5):
		yield i
		yield i*10
		
n2=yield_test()

print('Type(n2):     ', type(n2),'\nOutput:')	
for i in n2:	
	print('    ',i)
	
'''
output:  
	0
	0
	1
	10
	2
	20
	3
	30
	4
	40
'''
