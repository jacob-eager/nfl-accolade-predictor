import joblib
import pandas as pd


def main():
    prompt_user()

def prompt_user():

    csv_file_offense = '../data/' + 'offense_linear_award_model.pkl'
    csv_file_defense = '../data/' + 'defense_linear_award_model.pkl'
    
    """
    OFFENSE: 28 attributes

    In order:
    pass_attempts
    complete_pass
    incomplete_pass = (pass_attempts - complete_pass)
    passing_yards
    receiving_yards
    rush_attempts
    rushing_yards
    rush_touchdown
    pass_touchdown
    safety
    interception
    fumble
    fumble_lost
    receptions
    targets
    receiving_touchdown
    total_tds: (rush_touchdown + pass_touchdown + receiving_touchdown)
    total_yards: (passing_yards + receiving_yards + rushing_yards)
    games_played_season
    passer_rating:
            a = ((complete_pass / pass_attempts) - 0.3) * 5
            b = ((passing_yards / pass_attempts) - 3) * 0.25
            c = (pass_touchdown / pass_attempts) * 20
            d = 2.375 - ((interception / pass_attempts) * 25)
            passer_rating = ((a + b + c + d) / 6) * 100
    comp_pct = (complete_pass / pass_attempts)
    int_pct = (interception / pass_attempts)
    pass_td_pct = (pass_touchdown / pass_attempts)
    ypa = (passing_yards / pass_attempts)
    rec_td_pct = (receiving_touchdown / targets)
    yptarget = (receiving_yards / targets)
    ayptarget = (receiving_yards / targets)
    ypr = (receiving_yards / receptions)
    rush_td_pct = (rush_touchdown / rush_attempts)
    ypc = (rushing_yards / rush_attempts)
    td_pct = ((pass_attempts + rush_attempts + receptions) / total_tds)

    """
    #If these aren't initialized, it can bug
    total_yards = 0
    pass_td_pct = 0
    passer_rating = 0
    comp_pct = 0
    int_pct = 0
    ypa = 0
    yptarget = 0
    ayptarget = 0
    ypr = 0
    rush_td_pct = 0
    ypc = 0
    td_pct = 0
    total_tds = 0
    rec_td_pct = 0
    # This could probably be replaced with asking for a position, if we decide to use position as an attribute
    category = input("Is your player on offense or defense? \n")

    if category.lower() == "offense":
        positions = ["QB", "WR", "TE", "G", "FB", "C", "RB", "T"]
        position = positions.index(input("What position does your player play? QB, RB, WR, etc."))
        has_passing_stats = input("Does your player have passing stats? \n")
        if has_passing_stats.lower() == "yes":
            passing_yards = int(input("Passing yards: "))
            pass_attempts = int(input("Pass attempts: "))
            complete_pass = int(input("Pass completions: "))
            pass_touchdown = int(input("Passing TDs: "))
            interception = int(input("Passing INTs: "))
        else:
            passing_yards = 0
            pass_attempts = 0
            complete_pass = 0
            pass_touchdown = 0
            interception = 0

        has_receiving_stats = input("Does your player have receiving stats? \n")
        if has_receiving_stats.lower() == "yes":
            targets = int(input("Targets: "))
            receptions = int(input("Receptions: "))
            receiving_yards = int(input("Receiving yards: "))
            receiving_touchdown = int(input("Receiving TDs: "))
        else:
            targets = 0
            receptions = 0
            receiving_yards = 0
            receiving_touchdown = 0

        has_rushing_stats = input("Does your player have rushing stats? \n")
        if has_rushing_stats.lower() == 'yes':
            rushing_yards = int(input("Rushing yards: "))
            rush_attempts = int(input("Rushing attempts: "))
            rush_touchdown = int(input("Rushing TDs: "))
        else:
            rushing_yards = 0
            rush_attempts = 0
            rush_touchdown = 0

        safety = int(input("Safeties: "))
        fumble = int(input("Fumbles: "))
        fumble_lost = int(input("Fumbles lost: "))
        games_played_season = int(input("Games played: "))

        incomplete_pass = (pass_attempts - complete_pass)

        try:
            total_tds = (rush_touchdown + pass_touchdown + receiving_touchdown)
            total_yards = (passing_yards + receiving_yards + rushing_yards)
            a = ((complete_pass / pass_attempts) - 0.3) * 5
            b = ((passing_yards / pass_attempts) - 3) * 0.25
            c = (pass_touchdown / pass_attempts) * 20
            d = 2.375 - ((interception / pass_attempts) * 25)
            passer_rating = ((a + b + c + d) / 6) * 100
            comp_pct = (complete_pass / pass_attempts)
            int_pct = (interception / pass_attempts)
            pass_td_pct = (pass_touchdown / pass_attempts)
            ypa = (passing_yards / pass_attempts)
            rec_td_pct = (receiving_touchdown / targets)
            yptarget = (receiving_yards / targets)
            ayptarget = (receiving_yards / targets)
            ypr = (receiving_yards / receptions)
            rush_td_pct = (rush_touchdown / rush_attempts)
            ypc = (rushing_yards / rush_attempts)
            td_pct = ((pass_attempts + rush_attempts + receptions) / total_tds)

        except:
            print()

        model, scaler = joblib.load(csv_file_offense)

        input_features = [
            "position", "pass_attempts", "complete_pass", "incomplete_pass", "passing_yards",
            "receiving_yards", "rush_attempts", "rushing_yards", "rush_touchdown",
            "pass_touchdown", "safety", "interception", "fumble", "fumble_lost",
            "receptions", "targets", "receiving_touchdown", "total_tds", "total_yards",
            "games_played_season", "passer_rating", "comp_pct", "int_pct", "pass_td_pct",
            "ypa", "rec_td_pct", "yptarget", "ayptarget", "ypr", "rush_td_pct", "ypc", "td_pct"
        ]
        input_values = [
            position, pass_attempts, complete_pass, incomplete_pass, passing_yards,
            receiving_yards, rush_attempts, rushing_yards, rush_touchdown,
            pass_touchdown, safety, interception, fumble, fumble_lost,
            receptions, targets, receiving_touchdown, total_tds, total_yards,
            games_played_season, passer_rating, comp_pct, int_pct, pass_td_pct,
            ypa, rec_td_pct, yptarget, ayptarget, ypr, rush_td_pct, ypc, td_pct
        ]

        # Wrap input_values in another list to form 1 row of 31 columns
        attributes = pd.DataFrame([input_values], columns=input_features)
        attributes_scaled = scaler.transform(attributes)

        predicted_values = model.predict(attributes_scaled)

        predicted = predicted_values[0]

        print('MVP: ' + str(predicted[0]))
        print('OPOY: ' + str(predicted[1]))
        print('All-Pro: ' + str(predicted[2]))



    elif category.lower() == 'defense':
        fumbles_forced = int(input("Fumbles forced: "))
        fumbles_recovered = int(input("Fumbles recovered: "))
        fumble_return_tds = int(input("Fumble return TDs: "))
        assisted_tackles = int(input("Tackle assists: "))
        solo_tackles = int(input("Solo tackles: "))
        sacks = float(input("Sacks: "))
        defensive_ints = int(input("Defensive INTs: "))
        pick_sixes = int(input("INT return TDs: "))

        model, scaler = joblib.load(csv_file_offense)

        input_features = ["fumbles_forced", "fumbles_recovered", "fumble_return_tds", "assisted_tackles", "solo_tackles", "sacks", "defensive_ints", "pick_sixes"]
        input_values = [fumbles_forced, fumbles_recovered, fumble_return_tds, assisted_tackles, solo_tackles, sacks, defensive_ints, pick_sixes]

        attributes = pd.DataFrame([input_values], columns=input_features)
        attributes_scaled = scaler.transform(attributes)

        predicted_values = model.predict(attributes_scaled)

        predicted = predicted_values[0]

        print('MVP: ' + str(predicted[0]))
        print('DPOY: ' + str(predicted[1]))
        print('All-Pro: ' + str(predicted[2]))





if __name__ == "__main__":
    main()
