
def main():
    prompt_user()

def prompt_user():

    """
    OFFENSE: 28 attributes

    In order:
    pass_attempts
    complete_pass
    incomplete_pass: Can either prompt the user or do (pass_attempts - complete_pass(
    passing_yards
    receiving_yards
    rush_attempts
    rushing_yards
    rush_touchdown
    pass_touchdown
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




    :return:
    """







    # This could probably be replaced with asking for a position, if we decide to use position as an attribute
    category = input("Is your player on offense or defense? \n")

    if category.lower() == "offense":
        has_passing_stats = input("Does your player have passing stats? \n")
        if has_passing_stats.lower() == "yes":
            pass_yards = int(input("Passing yards: "))
            pass_attempts = int(input("Pass attempts: "))
            pass_completions = int(input("Pass completions: "))
            pass_tds = int(input("Passing TDs: "))
            pass_ints = int(input("Passing INTs: "))
        else:
            pass_yards = 0
            pass_attempts = 0
            pass_completions = 0
            pass_tds = 0
            pass_ints = 0

        has_receiving_stats = input("Does your player have receiving stats? \n")
        if has_receiving_stats.lower() == "yes":
            targets = int(input("Targets: "))
            receptions = int(input("Receptions: "))
            receiving_tds = int(input("Receiving TDs: "))
        else:
            targets = 0
            receptions = 0
            receiving_tds = 0

        has_rushing_stats = input("Does your player have rushing stats? \n")
        if has_rushing_stats.lower() == 'yes':
            rushing_yards = int(input("Rushing yards: "))
            rushing_attempts = int(input("Rushing attempts: "))
            rushing_tds = int(input("Rushing TDs: "))
        else:
            rushing_yards = 0
            rushing_attempts = 0
            rushing_tds = 0

    elif category.lower() == 'defense':
        fumbles_forced = int(input("Fumbles forced: "))
        fumbles_recovered = int(input("Fumbles recovered: "))
        fumble_return_tds = int(input("Fumble return TDs: "))
        assisted_tackles = int(input("Tackle assists: "))
        solo_tackles = int(input("Solo tackles: "))
        sacks = float(input("Sacks: "))
        defensive_ints = int(input("Defensive INTs: "))
        pick_sixes = int(input("INT return TDs: "))



if __name__ == "__main__":
    main()