import pandas as pd

def load_players(file_path):
    return pd.read_csv(file_path)
def load_matches(file_path):
    return pd.read_csv(file_path)

def merge_players_matches(players_df, matches_df):
    return pd.merge(players_df, matches_df, on='PlayerID', how='inner')


def total_runs_per_team(merged_df):
    return merged_df.groupby('Team')['Runs'].sum().reset_index()

def calculate_strike_rate(merged_df):
   temp_df = merged_df.copy()
   temp_df['StrikeRate'] = (temp_df['Runs'] / temp_df['Balls']) * 100
   print(temp_df)
   return temp_df[['PlayerID', 'Name', 'Runs', 'Balls', 'StrikeRate']]
    

def runs_agg_per_player(merged_df):
    agg = merged_df.groupby(['PlayerID', 'Name'])['Runs'].agg(['mean', 'max', 'min']).reset_index()
    print(agg)
    return agg
    

def avg_age_by_role(players_df):
    return players_df.groupby('Role')['Age'].mean().reset_index()

def total_matches_per_player(matches_df):
    tm = matches_df.groupby('PlayerID', as_index=False)['MatchID'].count()
    tm = tm.rename(columns={'MatchID': 'MatchCount'})
    print(tm) 

    return tm
    


    # Step 1: Get counts (index: PlayerID, column: count)
    
    # Step 2: Rename columns explicitly and cleanly
   

    # Ensure columns are in correct order
   
 



def top_wicket_takers(merged_df):
   wicket_summary = merged_df.groupby(['PlayerID', 'Name'], as_index=False)['Wickets'].sum()
   top_performers = wicket_summary.sort_values(by='Wickets', ascending=False).head(3).reset_index(drop=True)
   print(top_performers)
   return top_performers
   

def avg_strike_rate_per_team(merged_df):
    df = merged_df.copy()
    df['StrikeRate'] = df['Runs'] / df['Balls'] * 100
    result = df.groupby('Team', as_index=False)['StrikeRate'].mean()
    print(result)
    return result

def catch_to_match_ratio(merged_df):
    ca= merged_df.groupby('PlayerID', as_index=False).agg({'Catches': 'sum', 'MatchID': 'count'})
    ca['CatchToMatchRatio'] = ca['Catches'] / ca['MatchID']
    result = ca[['PlayerID' , 'CatchToMatchRatio']]
    print(result)
    return result
    
