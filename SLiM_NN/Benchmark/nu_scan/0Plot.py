import matplotlib.pyplot as plt 
import pandas as pd

SLiM_csv='SLiM_calc_2.csv'
SLiM_NN_csv='SLiM_calc_NN.csv'

data=pd.read_csv(SLiM_csv)      #data is a dataframe. 
data_NN=pd.read_csv(SLiM_NN_csv)      #data is a dataframe. 

data=data.query('gamma>0.00001 and nu<14')

plt.clf()
plt.plot(data['nu'],data['gamma'],label='SLiM')
plt.plot(data_NN['nu'],data_NN['gamma_10']*max(data['gamma']),label='SLiM_NN')
plt.xlabel(r'$\nu_{ei}/\omega_{*n}$',fontsize=15)
plt.ylabel(r'$\gamma/\omega_{*n}$',fontsize=15)
plt.axhline(0,color='black',alpha=0.5)
plt.grid(alpha=0.2)
plt.xlim(0,20)
plt.legend()
plt.show()

data_NN=data_NN.query('gamma_10==1 and nu<14 ')


plt.clf()
plt.plot(data['nu'],data['f'],label='SLiM')
plt.plot(data_NN['nu'],data_NN['f'],label='SLiM_NN')
plt.xlabel(r'$\nu_{ei}/\omega_{*n}$',fontsize=15)
plt.ylabel(r'$\omega/\omega_{*n}$',fontsize=15)
plt.ylim(0, 1.2*max(max(data_NN['f']),max(data['f'])) )
plt.grid(alpha=0.2)
plt.xlim(0,17)
plt.legend()
plt.show()
