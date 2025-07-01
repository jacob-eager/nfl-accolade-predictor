import joblib
import pandas as pd


def main():
    prompt_user()

def prompt_user():

    csv_file_offense = '../models/offense_linear_award_model.pkl'
    csv_file_defense = '../models/defense_linear_award_model.pkl'

    category = input("Is your player on offense or defense? \n")
    if category.lower() == "offense":
        positions = ["QB", "WR", "TE", "G", "FB", "C", "RB", "T"]
        position = positions.index(input("What position does your player play? QB, RB, WR, etc. \n"))

        # Passing stats
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

        # Receiving stats
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

        # Rushing stats
        has_rushing_stats = input("Does your player have rushing stats? \n")
        if has_rushing_stats.lower() == 'yes':
            rushing_yards = int(input("Rushing yards: "))
            rush_attempts = int(input("Rushing attempts: "))
            rush_touchdown = int(input("Rushing TDs: "))
        else:
            rushing_yards = 0
            rush_attempts = 0
            rush_touchdown = 0

        # Universal stats
        safety = int(input("Safeties: "))
        fumble = int(input("Fumbles: "))
        fumble_lost = int(input("Fumbles lost: "))
        games_played_season = int(input("Games played: "))

        # Calculated stats
        incomplete_pass = (pass_attempts - complete_pass)
        total_tds = (rush_touchdown + pass_touchdown + receiving_touchdown)
        total_yards = (passing_yards + receiving_yards + rushing_yards)
        a = ((complete_pass / pass_attempts) - 0.3) * 5 if pass_attempts != 0 else 0
        b = ((passing_yards / pass_attempts) - 3) * 0.25 if pass_attempts != 0 else 0
        c = (pass_touchdown / pass_attempts) * 20 if pass_attempts != 0 else 0
        d = 2.375 - ((interception / pass_attempts) * 25) if pass_attempts != 0 else 0
        passer_rating = ((a + b + c + d) / 6) * 100
        comp_pct = (complete_pass / pass_attempts) if pass_attempts != 0 else 0
        int_pct = (interception / pass_attempts) if pass_attempts != 0 else 0
        pass_td_pct = (pass_touchdown / pass_attempts) if pass_attempts != 0 else 0
        ypa = (passing_yards / pass_attempts) if pass_attempts != 0 else 0
        rec_td_pct = (receiving_touchdown / targets) if targets != 0 else 0
        yptarget = (receiving_yards / targets) if targets != 0 else 0
        ayptarget = (receiving_yards / targets) if targets != 0 else 0
        ypr = (receiving_yards / receptions) if receptions != 0 else 0
        rush_td_pct = (rush_touchdown / rush_attempts) if rush_attempts != 0 else 0
        ypc = (rushing_yards / rush_attempts) if rush_attempts != 0 else 0
        td_pct = ((pass_attempts + rush_attempts + receptions) / total_tds) if total_tds != 0 else 0

        # Load model
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

        attributes = pd.DataFrame([input_values], columns=input_features)
        attributes_scaled = scaler.transform(attributes)

        predicted_values = model.predict(attributes_scaled)

        predicted = predicted_values[0]

        print("\nPredicted Results:")
        print(f" - MVP: {'Yes' if predicted[0] == 1 else 'No'}")
        print(f" - OPOY: {'Yes' if predicted[1] == 1 else 'No'}")
        print(f" - All-Pro: {'Yes' if predicted[2] == 1 else 'No'}")

    elif category.lower() == 'defense':
        positions = ["SS", "CB", "DB", "DE", "DT", "FS", "FS", "ILB", "LB", "MLB", "NT", "OLB", "S"]
        position = positions.index(input("What position does your player play? CB, DT, MLB, etc. \n"))

        solo_tackle = int(input("Solo tackles: "))
        assist_tackle = int(input("Assisted tackles: "))
        sack = float(input("Sacks: "))
        safety = int(input("Safeties: "))
        interception = int(input("Interceptions: "))
        def_touchdown = int(input("Defensive touchdowns: "))
        fumble_forced = int(input("Fumbles forced: "))
        games_played_season = int(input("Games played: "))

        model, scaler = joblib.load(csv_file_defense)

        input_features = ["position", "solo_tackle", "assist_tackle", "sack",
                          "safety", "interception", "def_touchdown", "fumble_forced",
                          "games_played_season"]
        input_values = [position, solo_tackle, assist_tackle, sack,
                          safety, interception, def_touchdown, fumble_forced,
                          games_played_season]

        attributes = pd.DataFrame([input_values], columns=input_features)
        attributes_scaled = scaler.transform(attributes)

        predicted_values = model.predict(attributes_scaled)

        predicted = predicted_values[0]

        print("\nPredicted Results:")
        print(f" - MVP: No") # Automatic no since there are no defensive MVPs in the dataset
        print(f" - DPOY: {'Yes' if predicted[0] == 1 else 'No'}")
        print(f" - All-Pro: {'Yes' if predicted[1] == 1 else 'No'}")

if __name__ == "__main__":
    main()
