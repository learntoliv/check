import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax=fig.add_axes([0.15,0.15,0.75,0.75])

TMDT=[25.5,22.5,24.65,27.05]
HTTT=[24,21.25,23.35,26.45]
Nam=['2017','2018','2019','2020']
TrucX=[0,1,2,3]
TrucXX = [0.25,1.25,2.25,3.25]
print(TrucXX)

AvgTMDT=np.mean(TMDT)
AvgHTTT=np.mean(HTTT)

print(AvgTMDT)
print(AvgHTTT)

ax.bar(TrucX,TMDT,width=0.25,align='center')
ax.bar(TrucXX,HTTT,color='green',width=0.25,align='center')

ax.set_xticks(TrucX)
ax.set_xticklabels(Nam)

#ax.legend(labels=['TMĐT'+': '+str(AvgTMDT),'HTTT'+': '+str(AvgHTTT)])

ax.set_title("Điểm chuẩn khoa hệ thống thông tin - UEL")
ax.set_xlabel("Năm")
ax.set_ylabel("Điểm")
plt.show()
'''
X=[1,2,3,4]
Y=[51,24,62,48]
ax.plot(X,Y,marker='s',Linestyle='--',color='pink')
ax.set_title("Title")
ax.set_xlabel("Đây là label của x")
ax.set_ylabel("Đây là label của y")
plt.show()
'''
