import csv
import plotly.figure_factory as ff
import statistics
import pandas as pd
import plotly.graph_objects as go
import random

#reading the csv file
df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

#plotting the graph
#fig = ff.create_distplot([data], ["reading_time"], show ist = False)
#fig.show()

#finding mean
mean = statistics.mean(data)

#finding standard deviation
std_dev = statistics.stdev(data)

print("Mean: ", mean)
print("Standard deviation: ", std_dev)

##  code to find the mean of 100 data points 1000 times and plot it
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

# Pass the number of time you want the mean of the data points as a parameter in range function in for loop

mean_list = []

def setup():
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
fig.show()

def standard_deviation():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()

z_score = (mean_list-mean)/std_dev
print("Z_score: ", z_score)