import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_absolute_error
import joblib
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import StandardScaler

# Load our data set
df = pd.read_csv("../data/offense_complete.csv")
# Create the X and y arrays
X = df [[
    "position", "pass_attempts", "complete_pass", "incomplete_pass", "passing_yards",
    "receiving_yards", "rush_attempts", "rushing_yards", "rush_touchdown",
    "pass_touchdown", "safety", "interception", "fumble", "fumble_lost",
    "receptions", "targets", "receiving_touchdown", "total_tds", "total_yards",
    "games_played_season", "passer_rating", "comp_pct", "int_pct", "pass_td_pct",
    "ypa", "rec_td_pct", "yptarget", "ayptarget", "ypr", "rush_td_pct", "ypc", "td_pct"
]]
y = df[["mvp", "opoy", "allpro"]]
# Split the data set in a training set (75%) and a test set (25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
#Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled =  scaler.transform(X_test)
# Create the Linear Regression model
model = LogisticRegression()
moc = MultiOutputClassifier(model)
# Train the model
moc.fit(X_train_scaled, y_train)
# Save the trained model to a file so we can use it to make predictions later
joblib.dump((moc, scaler), '../models/offense_linear_award_model.pkl')
# Report how well the model is performing
print("Model training results:")
# Report an error rate on the training set
mse_train = mean_absolute_error(y_train, moc.predict(X_train_scaled))
print(f" - Training Set Error: {mse_train}")
# Report an error rate on the test set
mse_test = mean_absolute_error(y_test, moc.predict(X_test_scaled))
print(f" - Test Set Error: {mse_test}")
