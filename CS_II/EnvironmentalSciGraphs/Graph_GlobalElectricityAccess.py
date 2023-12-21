#Irhan Iftikar, December 2023
#Question Answered: What percentage of people have access to household electricity in each region?
#Data Source for Region: https://unstats.un.org/sdgs/report/2019/goal-07/
#Data Source for Country: https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS

import matplotlib.pyplot as plt
file_in = open("C:\\Users\\iiftikar26\\Desktop\\GCDS Comp Sci\\region-electricity-access.csv")
next(file_in)
regions = []
percentages = []
for line in file_in:   
    list_of_words = line.split(",") 
    regions.append(list_of_words[0])
    percentages.append(int(list_of_words[1]))

#Matplotlib code that creates graph
x_axis = regions
y_axis = percentages
plt.bar(x_axis, y_axis)
plt.title('Percentage of Population Having Access to Household Electricity by Global Region')
plt.xlabel('Global Region')
plt.xticks(fontsize = 4) 
plt.ylabel("% of Population")
plt.show()