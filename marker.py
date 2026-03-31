import matplotlib.pyplot as plt
import numpy as np

# x=([2,4,6,8,10])
# y=([10, 20, 15, 25, 30])
# plt.plot(x,y)
# plt.subplot(1,2,1)

# x=([2,4,6,8,10])
# y=([10, 20, 15, 25, 30])
# plt.plot(x,y)
# plt.subplot(1,2,1)


# x=([2,4,6,8,10])
# y=([10,20,30,40,50])
# plt.subplot(1,2,2)
# plt.plot(x,y,marker='o',color='g',ms=10,mec='k',mfc='white',linestyle='--')
# plt.show()


plt.subplot(1,2,1)  
plt.plot([1,2,3],[4,5,6])
plt.subplot(1,2,2)   
plt.plot([1,2,3],[6,5,4])
plt.subplot(1,2,1)
plt.plot([1,2,3],[7,8,9])

plt.show()





import matplotlib.pyplot as plt
import numpy as np
x = [2,4,6,8,10]
y = [10, 20, 15, 25, 30]
plt.subplot(1,2,1)  
plt.plot(x, y, marker='o', color='b', linestyle='-')



x = [2,4,6,8,10]
y = [10,20,30,40,50]
plt.subplot(1,2,2)   
plt.plot(x, y, marker='o', color='g', ms=10, mec='k', mfc='white', linestyle='--')


plt.show()






