"""Importing the modules"""
import csv
import matplotlib.pyplot as plt

def plot(years, teams,team_championships):
    """Plotting the graph fro data"""
    plt.figure(figsize=(10, 6))
    bottom = [0] * len(years)
    for team in teams:
        values = team_championships[team]
        plt.bar(years, values, label=team, bottom=bottom)
        bottom = [b + v for b, v in zip(bottom, values)]
    plt.xlabel('Year')
    plt.ylabel('number of wins')
    plt.title('IPL win count by Team')
    plt.legend(title='Teams', loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig('../images/won_per_team_per_year.png')
    # plt.savefig('../images/test.png')

def calculate(won_per_team):
    """calculate the team wons per year"""
    teams = set()
    years = list(won_per_team.keys())
    for year_data in won_per_team.values():
        teams.update(year_data.keys())
    teams = sorted(teams)
    team_championships = {team: [won_per_team[year].get(team, 0) for year in years] for team in teams}
    plot(years,teams, team_championships)


def execute():
    """Execute fun to mnake the datastructure"""
    won_per_team_year = {}
    with open('../dataset/matches.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = int(row.get('season'))
            winner = row.get('winner')
            if year not in won_per_team_year:
                won_per_team_year[year] = {}
            if winner not in won_per_team_year[year]:
                won_per_team_year[year][winner] = 1
            else:
                won_per_team_year[year][winner] += 1
    calculate(won_per_team_year)
    return won_per_team_year
execute()





# """CSV to read file MATPLOTLIB to plot graph"""

# import csv
# import matplotlib.pyplot as plt

# MATCHES = '../dataset/matches.csv'

# def plot(won_per_year_data):
#     """ploting the graph"""
#     seasons = list(won_per_year_data.keys())
#     teams = list(set(team for season in won_per_year_data.values() for team in season))

#     # Initialize a list to keep track of the bottom values for each team
#     bottom = [0] * len(seasons)

#     plt.figure(figsize=(10, 6))

#     for team in teams:
#         heights = [won_per_year_data[season].get(team, 0) for season in seasons]
#         plt.bar(seasons, heights, label=team, bottom=bottom)
#         bottom = [h1 + h2 for h1, h2 in zip(bottom, heights)]

#     plt.xlabel('Season')
#     plt.ylabel('Number of Wins')
#     plt.title('Stacked Bar Chart of Matches won per team per season')

#     plt.legend(
#         loc="center left",
#         title = "teams",
#         bbox_to_anchor=(1, 0, 0.5, 1))
#     plt.tight_layout()
#     plt.savefig('../images/test.png')
# def execute():
#     won_per_team_per_year = {}
#     with open(MATCHES, 'r', encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             team_name = row.get('winner')
#             season = row.get('season')

#             #changing name to make both the team name same
#             if team_name == "Rising Pune Supergiant":
#                 team_name = "Rising Pune Supergiants"

#             # creating dict inside a dict for every season
#             if season not in won_per_team_per_year:
#                 won_per_team_per_year[season] = {}
#             # checking if tetam exist in that season then add 1,
              # else add that team and initialize it with 1
#             if team_name not in won_per_team_per_year[season]:
#                 won_per_team_per_year[season][team_name] = 1
#             else:
#                 won_per_team_per_year[season][team_name] += 1
#     plot(won_per_team_per_year)
# execute()
