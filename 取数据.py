import re
import time
import matplotlib.pyplot as plt
with open('0.txt') as f:
    file = f.read()
pattern=re.compile('408.+1948') 
result=pattern.findall(file)    
v = []
v = result[0]
pattern=re.compile('508.+1545') 
result0=pattern.findall(file)
w = []
w = result0[0]
a = r','
v = re.split(a,v)
w = re.split(a,w)
v = list(map(eval,v))
w = list(map(eval,w))
plt.xlim(xmax=1600,xmin=0)
plt.ylim(ymax=1600,ymin=0)
plt.plot(v,w,'ro')
plt.show()

def bag(n, c, w, v):
    
    
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    for x in value:
        print(x)
    return value

def show(n, c, w, value):
    print('最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个,', end='')

def bag1(n, c, w, v):
    values = [0 for i in range(c+1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            
            if j >= w[i-1]:
                values[j] = max(values[j-w[i-1]]+v[i-1], values[j])
    return values
def sort(v,w):
    xx=[a/b for a,b in zip(v,w)]     
    xx.sort(reverse=True)                    
    x = xx
    '''
    print("非递增排序的结果为：")
    for i in x:
       print(i)
     '''

if __name__ == '__main__':
    
    n = 30
    c = 10149
    
    sort(v,w)
   
    start =time.perf_counter()
    value = bag(n, c, w, v)
   
    show(n, c, w, value)
    end = time.perf_counter()
    print('\nRunning time: %s Seconds'%(end-start))
    
    print('\n空间复杂度优化为N(c)结果:', bag1(n, c, w, v))
    






