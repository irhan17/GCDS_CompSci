#Irhan Iftikar, December 2023
#Question Answered: What is the global average levelized cost of each sustainable source of energy in $/kWh?
#Cost Data Source: https://ourworldindata.org/grapher/levelized-cost-of-energy?time=earliest..2021
#Carbon Footprint Data Source: https://world-nuclear.org/information-library/energy-and-the-environment/carbon-dioxide-emissions-from-electricity.aspx

import matplotlib.pyplot as plt
file_in = open("C:\\Users\\iiftikar26\\Desktop\\GCDS Comp Sci\\levelized-cost-of-energy.csv")
energy = []
cost = []
index = 0
for line in file_in:   
    list_of_words = line.split(",") 
    index +=1
    if index == 1:
        for i in range (3,10):
            energy.append(list_of_words[i])
    elif index == 460:      #Index line in .csv that contains most recent global average cost figures 
        for i in range (3,10):
            cost.append(float(list_of_words[i]))

#Matplotlib code that creates graph
x_axis = energy
y_axis = cost
plt.bar(x_axis, y_axis)
plt.title('Global Average Cost per Unit of Various Sustainable Energy Sources ($/kWh)')
plt.xlabel('Sources of Sustainable Energy')
plt.ylabel('Global Average Cost per unit of energy ($/kWh)')
plt.xticks(fontsize = 7) 
plt.show()