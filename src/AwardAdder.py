import pandas as pd

player_file_path = ['offense.csv', 'defense.csv']
award_file_path =  ['mvp2012-2024.csv', 'offensive_player_of_the_year.csv',
                    'defensive_player_of_the_year.csv', 'combined_all_pro.csv']
award_type = ['mvp', 'opoy', 'dpoy', 'allpro']
output_file_path = ['offense_complete.csv', 'defense_complete.csv']

team_name_map = {
    'ARI': 'Arizona Cardinals', 'ATL': 'Atlanta Falcons', 'BAL': 'Baltimore Ravens',
    'BUF': 'Buffalo Bills', 'CAR': 'Carolina Panthers', 'CHI': 'Chicago Bears',
    'CIN': 'Cincinnati Bengals', 'CLE': 'Cleveland Browns', 'DAL': 'Dallas Cowboys',
    'DEN': 'Denver Broncos', 'DET': 'Detroit Lions', 'GB': 'Green Bay Packers',
    'HOU': 'Houston Texans', 'IND': 'Indianapolis Colts', 'JAX': 'Jacksonville Jaguars',
    'KC': 'Kansas City Chiefs', 'LV': 'Las Vegas Raiders', 'LAC': 'Los Angeles Chargers',
    'LAR': 'Los Angeles Rams', 'MIA': 'Miami Dolphins', 'MIN': 'Minnesota Vikings',
    'NE': 'New England Patriots', 'NO': 'New Orleans Saints', 'NYG': 'New York Giants',
    'NYJ': 'New York Jets', 'PHI': 'Philadelphia Eagles', 'PIT': 'Pittsburgh Steelers',
    'SF': 'San Francisco 49ers', 'SEA': 'Seattle Seahawks', 'TB': 'Tampa Bay Buccaneers',
    'TEN': 'Tennessee Titans', 'WAS': 'Washington Commanders'
}
for i in range(len(player_file_path)):
    player_df = pd.read_csv(player_file_path[i])

    player_df['player_name'] = player_df['player_name'].str.strip()
    player_df['team'] = player_df['team'].str.strip().map(team_name_map)
    player_df['season'] = player_df['season'].astype(int)

    for j in range(len(award_file_path)):
        award_df = pd.read_csv(award_file_path[j])

        award_df['Player'] = award_df['Player'].str.strip()
        award_df['Tm'] = award_df['Tm'].str.strip()
        if award_type[j] == 'allpro':
            award_df['Tm'] = award_df['Tm'].map(team_name_map)
        award_df['Year'] = award_df['Year'].astype(int)

        award_set = set(zip(award_df['Player'], award_df['Year'], award_df['Tm']))

        player_df[award_type[j]] = player_df.apply(
            lambda row: 1 if (row['player_name'], row['season'], row['team']) in award_set else 0,
            axis=1
        )

    player_df.to_csv(output_file_path[i], index=False)
