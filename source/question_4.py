"""CSV to read file MATPLOTLIB to plot graph"""
import csv
import matplotlib.pyplot as plt

def plot(seasons, teams,data_struct ):
    """Ploting the graph"""
    bottom = [0] * len(seasons)
    plt.figure(figsize=(10, 6))
    for team in teams:
        heights = [data_struct[season].get(team, 0) for season in seasons]
        plt.bar(seasons, heights, label=team, bottom=bottom)
        bottom = [h1 + h2 for h1, h2 in zip(bottom, heights)]
    plt.xlabel('Season')
    plt.ylabel('Number of Wins')
    plt.title('Stacked Bar Chart of IPL Team Wins by Season')
    plt.legend(
        loc="center left",
        title = "teams",
        bbox_to_anchor=(1, 0, 0.5, 1)
    )
    plt.tight_layout()
    plt.savefig('../images/matches_player_per_team_per_season.png')
def execute():
    """Execute func to make dataset"""
    with open('../dataset/matches.csv', 'r',encoding="utf-8") as file:
        data = csv.DictReader(file)
        team_count_by_season = {}
        for row in data:
            season = row.get('season')
            team1 = row.get('team1')
            team2 = row.get('team2')
            #making the names same to calculate easily
            if team1 == "Rising Pune Supergiant":
                team1 = "Rising Pune Supergiants"
            if team2 == "Rising Pune Supergiant":
                team2 = "Rising Pune Supergiants"
            if season not in team_count_by_season:
                team_count_by_season[season] = {}
            # counting the number of occurance for all the team in every season
            if team1 not in team_count_by_season[season]:
                team_count_by_season[season][team1] = 1
            else:
                team_count_by_season[season][team1] += 1

            if team2 not in team_count_by_season[season]:
                team_count_by_season[season][team2] = 1
            else:
                team_count_by_season[season][team2] += 1
        # seasons = list(team_count_by_season.keys())
        seasons = list(team_count_by_season.keys())
        teams = list(set(team for season in team_count_by_season.values() for team in season))

        plot(seasons, teams, team_count_by_season)
execute()




# for season, details in team_count_by_season.items():
#     print(f"Season: {season}")
#     height = []
#     team = []

#     bottom = [0] * len(details)  # Initialize the bottom values for each bar

#     for name, count in details.items():
#         height.append(count)
#         team.append(name)
#     for i in range(len(team)):
#         plt.bar(season, height[i], label=team[i], bottom=bottom[i])
#         bottom[i] += height[i]
#         print(bottom[i])
# for season , details in team_count_by_season.items():
#     print(f"season : {season}")
#     height = []
#     team = []
#     for name , count in details.items():
#         # print(f"\t{name} : {count}")
#         height.append(count)
#         team.append(name)
#     print(height, end="\n")
#     print(team)
#     plt.bar(season, height, label = name)
