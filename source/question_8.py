"""CSV to read file MATPLOTLIB to plot graph"""
import csv
import matplotlib.pyplot as plt

def plot(name, economy):
    """Ploting the graph from data structure"""
    # names = list(data.keys())
    plt.figure(figsize=(12,6))
    # economy = [data[bowler]['economy'] for bowler in names]
    plt.bar(name, economy)
    plt.xlabel("Bowlers")
    plt.ylabel("Economy Rate")
    plt.xticks(rotation=90)
    plt.title("Top 10 Economic Bowlers of the Season 2015-16")
    plt.tight_layout()
    plt.savefig("../images/top_10_economical_bowler.png")


def calculate(data):
    """Calculate dunction to calculate the economy of bowler"""
    for bowler in data:
        try:
            runs = data[bowler]['total']
            overs = data[bowler]['over']
            economy = runs / overs
            data[bowler]['economy'] = round(economy, 2)
        except ZeroDivisionError:
            data[bowler]['economy'] = 0.0
    sorted_list = sorted(data.items(), key= lambda x : x[1]['economy'])

    top_10_economical_bowler = sorted_list[:10]
    # print(top_10_economical_bowler)

    name = []
    economy = []
    for i in range(len(top_10_economical_bowler)):
        name.append(top_10_economical_bowler[i][0])
        economy.append(top_10_economical_bowler[i][1]['economy'])
    plot(name,economy)


def execute():
    """Execute funtion to make the data structure"""
    match_id_for_2015 = []
    with open('../dataset/matches.csv', 'r', encoding="utf-8") as file:
        matches = csv.DictReader(file)
        for _match in matches:
            match_id = _match.get('id')
            season = _match.get('season')
            if season == '2015' and match_id not in match_id_for_2015:
                match_id_for_2015.append(match_id)
    total_run_deliveries = {}
    with open('../dataset/deliveries.csv', 'r', encoding='utf-8') as file:
        deliveries = csv.DictReader(file)
        for delivery in deliveries:
            match_id = delivery.get('match_id')
            bowler = delivery.get('bowler')
            total_run = delivery.get('total_runs')
            if match_id in match_id_for_2015:
                if bowler not in total_run_deliveries:
                    total_run_deliveries[bowler] = {'total': 0, 'over': 0}
                total_run_deliveries[bowler]['total'] += int(total_run)
                total_run_deliveries[bowler]['over'] += 1
    calculate(total_run_deliveries)
execute()
