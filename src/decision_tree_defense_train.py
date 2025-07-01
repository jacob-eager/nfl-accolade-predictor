from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.multioutput import MultiOutputClassifier
from sklearn import tree
import pandas as pd
import csv
import joblib
import matplotlib.pyplot as plt

with open("../data/defense_raw_stats.csv", mode='r') as file:
    data = csv.DictReader(file)
    df = pd.DataFrame(data)
    df = df.drop(columns=["position"])
    print(df.head())

    X = df [[
    "solo_tackle", "assist_tackle", "sack", "safety", "interception",
    "def_touchdown", "fumble_forced", "games_played_season"
    ]]
  
    y = df[["mvp", "dpoy", "allpro"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    dtc = DecisionTreeClassifier(max_depth=None, class_weight='balanced', min_samples_leaf=2)

    moc = MultiOutputClassifier(dtc)

    moc.fit(X_train, y_train)

    # Save the trained model to a file so we can use it to make predictions later
    joblib.dump(moc, '../models/decision_tree_defense_model.pkl')

    # Report how well the model is performing
    print("Model training results:")

    # Report an error rate on the training set
    mse_train = mean_absolute_error(y_train, moc.predict(X_train))
    print(f" - Training Set Error: {mse_train}")

    # Report an error rate on the test set
    mse_test = mean_absolute_error(y_test, moc.predict(X_test))
    print(f" - Test Set Error: {mse_test}")

    # Iterates through the decision trees for all 3 predicted accolades
    for i in range(3):
        tree.plot_tree(moc.estimators_[i],
                       feature_names= ["solo_tackle", "assist_tackle", "sack", "safety", "interception",
                                      "def_touchdown", "fumble_forced", "games_played_season"],
                       class_names=["mvp", "dpoy", "allpro"])

        plt.show()
