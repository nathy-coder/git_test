import pandas as pd 
import matplotlib.pyplot as plt
x=[1,2,34,6,0,8]
y=[12,3,24,26,72,28,]

df = pd.DataFrame(x,y)
plt.plot(x,y)
plt.show()