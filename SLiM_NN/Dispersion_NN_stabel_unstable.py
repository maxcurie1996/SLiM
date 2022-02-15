# TensorFlow and tf.keras
import tensorflow as tf  #https://adventuresinmachinelearning.com/python-tensorflow-tutorial/
import keras
from sklearn.model_selection import train_test_split

# Helper libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

#**********start of user block***********
filename='./NN_data/0MTM_scan_CORI_2.csv'
testing_output=True
load_model = tf.keras.models.load_model('SLiM_NN_omega.h5')
#**********end of user block*************
#****************************************

df=pd.read_csv(filename)
try:
    df=df.drop(columns=['change'])
except:
    pass

#df=df.astype('float')

df_unstable=df.query('omega_omega_n!=0 and gamma_omega_n>0')
df_stable=df.query('omega_omega_n==0 or gamma_omega_n<=0')

df_unstable['unstable']=[1]*len(df_unstable)
#df_unstable['stable']=[0]*len(df_unstable)
df_stable['unstable']=[0]*len(df_stable)
#df_stable['stable']=[1]*len(df_stable)

df=pd.concat([df_unstable, df_stable], axis=0)
print(df)

df_x=pd.DataFrame(np.transpose([df['nu'],df['zeff'],\
                    df['eta'],df['shat'],\
                    df['ky'],df['mu']/df['xstar']]),
                  columns=['nu', 'zeff','eta','shat',\
                    'ky','mu_norm'])

#df_y=pd.DataFrame(np.transpose([df['unstable'],df['stable']]),
#                  columns=['unstable','stable'])

df_y=pd.DataFrame(np.transpose([df['unstable']]),\
                  columns=['unstable'])

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2)


if testing_output==True:
    print('x_train')
    print(x_train)
    print('y_train')
    print(y_train)

#*********end of trainning***********************
predictions = load_model.predict(x_train)
print('x_train')
print(x_train)
print('y_train')
print(y_train)
print('predictions')
print(predictions)
print('abs(y_train-predictions)')
print(abs(y_train-predictions))

predictions = load_model.predict(x_test)
print('y_test')
print(y_test)
print('predictions')
print(predictions)
print('abs(y_train-predictions)')
print(abs(y_test-predictions))