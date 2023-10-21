"""CSV to read file MATPLOTLIB to plot graph"""
import csv
import matplotlib.pyplot as plt

def plot(season,total_match):
     # plt.pie(total_match, labels=total_match)
    plt.bar(season, total_match)
    plt.xlabel('Season')
    plt.ylabel('Total Matches')
    plt.title("Number of matches played per year for all the years in IPL")
    plt.tight_layout()
    plt.savefig('../images/match_played_per_year.png')
    # plt.savefig('../images/test.png')

def calculate(match_per_season):
    """calculatinhg total match per season"""
    total_match = []
    seasons = []
    for season , details in match_per_season.items():
        height = []
        seasons.append(season)
        for name , count in details.items():
            height.append(count)
        total_match.append(sum(height))
    plot(seasons,total_match)

def execute():
    """making the data structure for plotting"""
    team_count_by_season = {}
    with open('../dataset/matches.csv', 'r',encoding="utf-8") as file:
        data = csv.DictReader(file)
        for row in data:
            season = row.get('season')
            team1 = row.get('team1')

            #making the names same to calculate easily
            if team1 == "Rising Pune Supergiant":
                team1 = "Rising Pune Supergiants"


            if season not in team_count_by_season:
                team_count_by_season[season] = {}

            # counting the number of occurance for all the team in every season
            if team1 not in team_count_by_season[season]:
                team_count_by_season[season][team1] = 1
            else:
                team_count_by_season[season][team1] += 1

        calculate(team_count_by_season)

execute()
