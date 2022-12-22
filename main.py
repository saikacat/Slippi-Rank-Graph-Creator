import requests
import datetime as dt
import time as t
import pytz
import json
from keep_alive import keep_alive
from listofplayers import *
from chart import *

playerOfInterest = listOfplayers
keep_alive()
while True:
  playerOfInterest = listOfplayers
  for player in playerOfInterest:
    # Making a get request
    response = requests.get('http://slprank.com/rank/' + player)

    # print url
    rankStats = response.text
    rankStats = rankStats.replace('(', '').replace(')', '').split()
    print(rankStats)
    Name = player
    if (len(rankStats) == 4):
      #GM players
      Rank = rankStats[0]
      Number = rankStats[1]
      WL = rankStats[3]
    if (len(rankStats) == 5):
      #below top 50
      Rank = rankStats[0] + rankStats[1]
      Number = rankStats[2]
      WL = rankStats[4]
    if (len(rankStats) == 6):
      #below top 50
      Rank = rankStats[0] + rankStats[1]
      Number = rankStats[3]
      WL = rankStats[5]
    pst = pytz.timezone('America/Los_Angeles')
    current_time = dt.datetime.now(pst)
    dictionary = {
      "Name": Name,
      "Rank": Rank,
      "Number": Number,
      "Time": current_time
    }
    #print(dictionary)
    try:
      playerJson = player + '.json'
      with open('json_files/' + playerJson, 'r') as f:
        data = json.load(f)
        temp = data
        #print(temp)
        latestRank = temp[len(temp) - 1].get('Number')
        if (latestRank != Number):
          with open('json_files/' + playerJson, "w") as outfile:
            temp.append(dictionary)
            json.dump(temp, outfile, indent=4, sort_keys=True, default=str)
          chart_creator_slp('json_files/' + playerJson,
                            'graphs/ ' + player + '.png')
          print('Updated!')
        else:
          print('No Rank Change' + Number)
    except FileNotFoundError:
      print('filenotfound, creating file')
      with open('json_files/' + playerJson, 'w') as f:
        # Write the data to the file in JSON format
        initList = [dictionary]
        json.dump(initList, f, indent=4, sort_keys=True, default=str)
  t.sleep(30)
