import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib
# Load our data set
#df = pd.read_csv("../../Downloads/house_data.csv")
df = pd.read_csv("../data/offense_complete_standardized.csv")
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
# Create the Linear Regression model
model = LinearRegression()
# Train the model
model.fit(X_train, y_train)
# Save the trained model to a file so we can use it to make predictions later
joblib.dump(model, '../data/offense_linear_award_model.pkl')
# Report how well the model is performing
print("Model training results:")
# Report an error rate on the training set
mse_train = mean_absolute_error(y_train, model.predict(X_train))
print(f" - Training Set Error: {mse_train}")
# Report an error rate on the test set
mse_test = mean_absolute_error(y_test, model.predict(X_test))
print(f" - Test Set Error: {mse_test}")
