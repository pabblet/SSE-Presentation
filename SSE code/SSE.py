import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy.io import ascii

plt.style.use('ggplot')

i=input('Ingrese numero del archivo: ')
data= ascii.read('evolve'+i+'.dat')

#Diagrama HR
plt.plot(data['log10(Teff)'], data['log10(L)'], color='#444444', label='data')
plt.gca().invert_xaxis()
plt.xlabel('log(Teff)')
plt.ylabel('log(L)')
plt.legend(loc='best')
plt.show()

#Masa en funcion del tiempo
plt.plot(data['Tev(Myr)'], (data['Mt']), color='#444444', label='data')
plt.xlabel('Tev [Myr]')
plt.ylabel('M(t) [Msun]')
plt.legend(loc='best')
plt.show()

#Radio en funcion del tiempo
plt.plot(data['Tev(Myr)'], 10**data['log10(R)'], color='#444444', label='data')
plt.xlabel('Tev [Myr]')
plt.ylabel('R [Rsun]')
plt.legend(loc='best')
plt.show()

#Grafico de diagrama HR con todos los remanentes
n=0
masses=['0.8', '1.0', '8.0', '15.0', '25.0']
colors=['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB', '#444444']
while n<5:
    data= ascii.read('evolve'+str(n+1)+'.dat')
    plt.plot(data['log10(Teff)'], data['log10(L)'], color=colors[n], label='Masa '+masses[n]+' [Msun]')
    n+=1

plt.gca().invert_xaxis()
plt.xlabel('log(Teff)')
plt.ylabel('log(L)')
plt.legend(loc='best')
plt.show()