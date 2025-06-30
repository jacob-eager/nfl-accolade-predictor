from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
import csv
from sklearn.metrics import mean_absolute_error
import joblib
import matplotlib.pyplot as plt

with open("../data/offense_raw_stats.csv", mode='r') as file:
    data = csv.DictReader(file)
    df = pd.DataFrame(data)
    df = df.drop(columns=["position"])
    print(df.head())

    X = df.iloc[:, 0:32]

    y = df.iloc[:, 32:35]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    dtc = DecisionTreeClassifier(class_weight='balanced')

    dtc.fit(X_train, y_train)

    # Save the trained model to a file so we can use it to make predictions later
    joblib.dump(dtc, 'offense_model.pkl')

    # Report how well the model is performing
    print("Model training results:")

    # Report an error rate on the training set
    mse_train = mean_absolute_error(y_train, dtc.predict(X_train))
    print(f" - Training Set Error: {mse_train}")

    # Report an error rate on the test set
    mse_test = mean_absolute_error(y_test, dtc.predict(X_test))
    print(f" - Test Set Error: {mse_test}")

    tree.plot_tree(dtc)
    plt.show()
