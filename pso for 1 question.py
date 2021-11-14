import random
import math
import matplotlib.pyplot as plt
#參數區域
t=2000
w=0.9
c1=2
c2=2
particles=20

#製造粒子(由定義最大最小值製造，最大最小值個數為向量個數)
p=[]
max1=2
min1=-1
max2=1
min2=-2
for particle in range(particles):
    tempp=[]
    x1=random.uniform(min1, max1)
    x2=random.uniform(min2, max2)
    while x1+x2<-1:
        x1=random.uniform(min1, max1)
        x2=random.uniform(min2, max2)
    tempp.append(x1)
    tempp.append(x2)#這邊向量有幾個就要加幾行
    p.append(tempp)
#產生對應粒子內向量速度
speed=[]
smax1=1
smin1=-1
smax2=1
smin2=-1
for particle in range(particles):
    temps=[]
    x1=random.uniform(smin1, smax1)
    x2=random.uniform(smin2, smax2)
    temps.append(x1)
    temps.append(x2)#這邊向量有幾個就要加幾行
    speed.append(temps)
#計算初始各粒子局部適應值，並選出最佳適應值與對應最佳解
fitness=[]
regionp=[]
regionf=[]
for particle in p:
    x=particle[0]
    y=particle[1]
    f=math.exp(-0.1*(x**4+y**4))+math.exp(math.cos(2*math.pi*x)+math.cos(2*math.pi*y))
    fitness.append(f)
bestfitness=100
bestparticle=0
for i in range(particles):
    if fitness[i]<bestfitness:
        bestfitness=fitness[i]
        bestparticle=p[i]
for particle in p:
   regionp.append(particle)
for f in fitness:
    regionf.append(f)
#迭代以找尋最佳解
historyf=[]
historyp=[]
for time in range(t):
    #粒子群更新
    for a in range(len(p)):
        for b in range(2):
            r1=random.random()
            r2=random.random()
            speed[a][b]=w*speed[a][b]+c1*r1*(regionp[a][b]-p[a][b])+c2*r2*(bestparticle[b]-p[a][b])
            if speed[a][b]>smax1 :
                speed[a][b]=smax1
            elif speed[a][b]<smin1:
                speed[a][b]=smin1
            p[a][b]=p[a][b]+speed[a][b]
    for particle in p:
        while particle[0]+particle[1]<-1:
            particle[1]=-1-particle[0]+random.uniform(1,2)
    #粒子群評估與更新最佳與局部解
    tt=0
    for particle in p:
        x=particle[0]
        y=particle[1]
        f=math.exp(-0.1*(x**4+y**4))+math.exp(math.cos(2*math.pi*x)+math.cos(2*math.pi*y))
        fitness[tt]=f
        tt+=1
    for i in range(particles):
        if fitness[i]>regionf[i]:
            regionf[i]=fitness[i]
            regionp[i]=p[i]
    for i in range(particles):
        if regionf[i]>bestfitness:
            bestfitness=regionf[i]
            bestparticle=regionp[i].copy()
    #紀錄
    historyf.append(bestfitness)
    historyp.append(bestparticle)
print(bestfitness)
print(bestparticle)
plt.plot(historyf)   


