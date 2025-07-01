from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
import csv
from sklearn.metrics import mean_absolute_error
from sklearn.multioutput import MultiOutputClassifier
import joblib
import matplotlib.pyplot as plt

with open("../data/offense_complete.csv", mode='r') as file:
    data = csv.DictReader(file)
    df = pd.DataFrame(data)
    df = df.drop(columns=["position"])
    print(df.head())

    X = df[["position", "pass_attempts", "complete_pass", "incomplete_pass", "passing_yards",
            "receiving_yards", "rush_attempts", "rushing_yards", "rush_touchdown",
            "pass_touchdown", "safety", "interception", "fumble", "fumble_lost",
            "receptions", "targets", "receiving_touchdown", "total_tds", "total_yards",
            "games_played_season", "passer_rating", "comp_pct", "int_pct", "pass_td_pct",
            "ypa", "rec_td_pct", "yptarget", "ayptarget", "ypr", "rush_td_pct", "ypc", "td_pct"]]

    y = df[["mvp", "opoy", "allpro"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    dtc = DecisionTreeClassifier(max_depth=None, class_weight='balanced', min_samples_leaf=2)

    moc = MultiOutputClassifier(dtc)

    moc.fit(X_train, y_train)

    # Save the trained model to a file so we can use it to make predictions later
    joblib.dump(moc, 'offense_model.pkl')

    # Report how well the model is performing
    print("Model training results:")

    # Report an error rate on the training set
    mse_train = mean_absolute_error(y_train, moc.predict(X_train))
    print(f" - Training Set Error: {mse_train}")

    # Report an error rate on the test set
    mse_test = mean_absolute_error(y_test, moc.predict(X_test))
    print(f" - Test Set Error: {mse_test}")

    tree.plot_tree(moc.estimators_[2],
                   feature_names=["pass_attempts", "complete_pass", "incomplete_pass", "passing_yards",
                                  "receiving_yards", "rush_attempts", "rushing_yards", "rush_touchdown",
                                  "pass_touchdown", "safety", "interception", "fumble", "fumble_lost",
                                  "receptions", "targets", "receiving_touchdown", "total_tds", "total_yards",
                                  "games_played_season", "passer_rating", "comp_pct", "int_pct", "pass_td_pct",
                                  "ypa", "rec_td_pct", "yptarget", "ayptarget", "ypr", "rush_td_pct", "ypc",
                                  "td_pct"],
                   class_names=["mvp", "opoy", "allpro"])

    plt.show()

