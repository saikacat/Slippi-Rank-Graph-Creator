import json
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
def chart_creator_slp(filename,targetfilename):
    # load data from JSON file
    with open(filename) as f:
        data = json.load(f)

    # extract time and rank data
    print(data)
    time_data = [datetime.fromisoformat(entry['Time']) for entry in data]
    rank_data = [entry['Number'] for entry in data]
    name = [entry['Name'] for entry in data]
    rank_data = pd.to_numeric(rank_data)
    
    # format time data as strings
    time_strings = [time.strftime('%H:%M') for time in time_data]
    
    # create figure and axis objects
    fig, ax = plt.subplots()

    # draw scatter plot
    ax.scatter(time_strings, rank_data)

    # draw line plot
    ax.plot(time_strings, rank_data)

    # title
    plt.xlabel("Time")
    plt.ylabel("ELO")
    plt.title(name[0])

    # show graph
    plt.savefig(targetfilename)
    plt.close()
#chart_creator('sidd.json', 'sidd.jpg')