import pandas as pd
import matplotlib.pyplot as plt


#Load data from the textfile. It is not saved as a csv, but read_csv was working better than read_table. 
#I wanted to use skiprows so that it was not necceassry manually delete rows from the textfile. 
# However, it would still load up files as having a single column instead of reading them in correctly. Also the number of events changes the number of rows. 
data = pd.read_csv("LOG00241.TXT")#skiprows=[0]

#the last line of the textfile is "END LOGGING" and causes some type problems so I remove it here. (could also be removed from arduino code.)
data = data.truncate(after=(len(data.index)-2))

#Ensure the time column is formatted as a date time. 
data['time'] = pd.to_datetime(data['time'])



#Plot the water and enegy use.
fig, ax = plt.subplots(2,2)
ax[0,0].plot(data['time'],data['valve_state'])
ax[0,0].set_title('Valve State')
ax[0,1].plot(data['time'],data['energy_use'])
ax[0,1].set_title('Energy Use')
ax[1,0].plot(data['time'],data['water_use'])
ax[1,0].set_title('Water Use')
ax[1,1].plot(data['time'],data['tempering_water_use'])
ax[1,1].set_title('Tempering Water Use')
plt.show()

#Plot the external temperatures
fig, ax = plt.subplots(2,4)
k= 0
j = 0
for i in range(60,68): #All the external temp sensors are in column 60-68
    column = data.columns[i]
    if k<4: 
        ax[j,k].plot(data[column])
        ax[j,k].set_title(column)
        ax[j,k].set_ylim(0,120)
        k=k+1
        
    if k>=4:
        j=j+1
        k=0
fig.set_tight_layout(True)
plt.show()


#Plot the boiler Temps
for i in range(1,5): #there are 4 arrays of 12 sensors each. So I am plotting each array in its own plot
    fig, ax = plt.subplots(2,6) #Set up figure with 2 rows of 6 subplots
    k= 0
    j = 0
    for i in range(i*12,(i+1)*12): #plot each subplot. luckliy everything is in order. the first array starts at column 12 and the last one is column 60, so we can just iterate through them. 
        column = data.columns[i]
        if k<6: 
            ax[j,k].plot(data[column])
            ax[j,k].set_title(column)
            ax[j,k].set_ylim(0,120)
            k=k+1
            
        if k>=6:
            j=j+1
            k=0
    plt.show()
