import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_absolute_error
import joblib
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import StandardScaler
# Load our data set
df = pd.read_csv("../data/defense_complete.csv")
# Create the X and y arrays
X = df [[
    "position", "solo_tackle", "assist_tackle", "sack", "safety", "interception",
    "def_touchdown", "fumble_forced", "games_played_season"
]]
y = df[["mvp", "dpoy", "allpro"]]
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
joblib.dump((moc, scaler), '../data/defense_linear_award_model.pkl')
# Report how well the model is performing
print("Model training results:")
# Report an error rate on the training set
mse_train = mean_absolute_error(y_train, moc.predict(X_train_scaled))
print(f" - Training Set Error: {mse_train}")
# Report an error rate on the test set
mse_test = mean_absolute_error(y_test, moc.predict(X_test_scaled))
print(f" - Test Set Error: {mse_test}")
