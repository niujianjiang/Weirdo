import re
import time
import numpy as np
import matplotlib.pyplot as plt
import copy
with open('0.txt') as f:
    file = f.read()
a = int(input("请输入选择的数据集:"))
if(a == 1):
    
    n = 30
    c = 10149
    pattern=re.compile('408.+1948')
    result=pattern.findall(file)    
    V = []
    V = result[0]
    pattern=re.compile('508.+1545') 
    result0=pattern.findall(file)
    W = []
    W = result0[0]    

if(a==2):
    
    n = 300
    c = 61500
    pattern=re.compile('408.+759')
    result=pattern.findall(file)    
    V = []
    V = result[0]
    pattern=re.compile('508.+728') 
    result0=pattern.findall(file)
    W = []
    W = result0[0]
    
a = r','
V = re.split(a,V)
W = re.split(a,W)
V = list(map(eval,V))
W = list(map(eval,W))

#动态规划算法

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
#回溯算法

def BacktrackBag(t):
    global rest            # 剩余背包容量
    global restp           # 当前未装入背包的总价值
    global cw              # 背包当前载重量
    global cp              # 背包当前装入价值
    global bestp           # 背包当前最优装入价值
    global x               # 解空间树表征数组
    global W               # 物品重量数组
    global V               # 物品价值数组
    global bestx           #最优表征数组
    if t >= n:
        if cp == bestp:
            bestx = copy.deepcopy(x)
        #if bestp >= cp:
        # print(x,'当前最优解:%.0f'% bestp)
    else:
        for i in range(1,-1,-1):
            x[t] = i
            #如果该物品可以放入，并且之后的物品比当前价值优进行递归
            if rest >= x[t]*W[t] and cp + restp - V[t] * (1-x[t]) >= bestp:
                rest = rest - x[t]*W[t]
                cp = cp + V[t]*x[t]
                restp = restp - V[t]
                if cp >= bestp:
                    bestp = cp
                BacktrackBag(t+1)
                rest = rest + x[t] * W[t]
                cp = cp - V[t] * x[t]
                restp = restp + V[t]

#遗传算法
def init(N,n):
    C = []
    for i in range(N):
        c = []
        for j in range(n):
            a = np.random.randint(0,2)
            c.append(a)
        C.append(c)
    return C

##评估函数
# x(i)取值为1表示被选中，取值为0表示未被选中
# w(i)表示各个分量的重量，v（i）表示各个分量的价值，w表示最大承受重量
def fitness(C,N,n,W,V,w):
    S = []##用于存储被选中的下标
    F = []## 用于存放当前该个体的最大价值
    for i in range(N):
        s = []
        h = 0  # 重量
        f = 0  # 价值
        for j in range(n):
            if C[i][j]==1:
                if h+W[j]<=w:
                    h=h+W[j]
                    f = f+V[j]
                    s.append(j)
        S.append(s)
        F.append(f)
    return S,F

##适应值函数,B位返回的种族的基因下标，y为返回的最大值
def best_x(F,S,N):
    y = 0
    x = 0
    B = [0]*N
    for i in range(N):
        if y<F[i]:
            x = i
        y = F[x]
        B = S[x]
    return B,y

## 计算比率
def rate(x):
    p = [0] * len(x)
    s = 0
    for i in x:
        s += i
    for i in range(len(x)):
        p[i] = x[i] / s
    return p

## 选择
def chose(p, X, m, n):
    X1 = X
    r = np.random.rand(m)
    for i in range(m):
        k = 0
        for j in range(n):
            k = k + p[j]
            if r[i] <= k:
                X1[i] = X[j]
                break
    return X1

##交配
def match(X, m, n, p):
    r = np.random.rand(m)
    k = [0] * m
    for i in range(m):
        if r[i] < p:
            k[i] = 1
    u = v = 0
    k[0] = k[0] = 0
    for i in range(m):
        if k[i]:
            if k[u] == 0:
                u = i
            elif k[v] == 0:
                v = i
        if k[u] and k[v]:
            # print(u,v)
            q = np.random.randint(n - 1)
            # print(q)
            for i in range(q + 1, n):
                X[u][i], X[v][i] = X[v][i], X[u][i]
            k[u] = 0
            k[v] = 0
    return X

##变异
def vari(X, m, n, p):
    for i in range(m):
        for j in range(n):
            q = np.random.rand()
            if q < p:
                X[i][j] = np.random.randint(0,2)

    return X

#画图
def huatu(v,w):
    plt.xlim(xmax=1600,xmin=0)
    plt.ylim(ymax=1600,ymin=0)
    plt.plot(v,w,'ro')
    plt.show()
                
#非递增排序
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
    b = int(input("请输入选择的算法:"))
    if(b == 1):
    
       sort(V,W)       
       start =time.perf_counter()
       value = bag(n, c, W, V)
       show(n, c, W, value)
       end = time.perf_counter()
       print('\nRunning time: %s Seconds'%(end-start))
    
       print('\n空间复杂度优化为N(c)结果:', bag1(n, c, W, V))
       huatu(V,W)
    
    if(b == 2):
        rest=c
        cw = 0
        cp = 0
        restp=0
        for i in V:
            restp=restp+i
        bestp=0
        x=[0 for i in range(n)]
        print('物品个数:',str(n))
        print('物品重量数组:',str(W))
        print('物品价值数组:',str(V))
        print('背包容量:',str(c))
        huatu(V,W)
        start =time.perf_counter()
        BacktrackBag(0)
        end = time.perf_counter()
        print('\nRunning time: %s Seconds'%(end-start))
        print(bestx,'当前最优解:%.0f'% bestp)
    if(b==3):
       m = 30        ##规模
       N = 800       ##迭代次数
       Pc = 0.8      ##交配概率
       Pm = 0.05     ##变异概率 
       n = len(W)##染色体长度
       w = 1000
       C = init(m, n)
       start =time.perf_counter()
       S,F  = fitness(C,m,n,W,V,w)
       B ,y = best_x(F,S,m)
       Y =[y]
       for i in range(N):
           p = rate(F)
           C = chose(p, C, m, n)
           C = match(C, m, n, Pc)
           C = vari(C, m, n, Pm)
           S, F = fitness(C, m, n, W, V, w)
           B1, y1 = best_x(F, S, m)
           if y1 > y:
               y = y1
           Y.append(y)
       end = time.perf_counter()   
       print('\nRunning time: %s Seconds'%(end-start))
       print("最大值为：",y)
       plt.plot(Y)
       plt.show()

    
    
