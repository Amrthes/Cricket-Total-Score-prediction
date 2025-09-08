import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

st.title("Cricket Runs Predictor with Optional Batting Average")

# -------------------------------
# Load Dataset & Train Model
# -------------------------------
df = pd.read_csv("odb.csv")  # Replace with your dataset path

# Decide which features to use
use_avg = st.sidebar.checkbox("Include Batting Average as Feature?", value=False)

if use_avg:
    features = ['Mat', 'Inns', 'BF', 'SR', 'Ave']
else:
    features = ['Mat', 'Inns', 'BF', 'SR']

X = df[features]
y = df['Runs']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_scaled, y)

# -------------------------------
# Input Section
# -------------------------------
st.sidebar.header("Player Stats Input")

matches = st.sidebar.number_input("Matches Played", min_value=0, value=50)
innings = st.sidebar.number_input("Innings Batted", min_value=0, value=45)
balls_faced = st.sidebar.number_input("Balls Faced", min_value=0, value=3000)
strike_rate = st.sidebar.number_input("Strike Rate", min_value=0.0, value=85.0)

if use_avg:
    ave = st.sidebar.number_input("Batting Average", min_value=0.0, value=50.0)

# -------------------------------
# Predict Button
# -------------------------------
if st.button("Predict Runs"):
    if use_avg:
        player_input = [[matches, innings, balls_faced, strike_rate, ave]]
    else:
        player_input = [[matches, innings, balls_faced, strike_rate]]
    
    player_input_scaled = scaler.transform(player_input)
    predicted_runs = model.predict(player_input_scaled)
    
    st.success(f"Predicted Runs: {int(predicted_runs[0])}")

# -------------------------------
# Model Performance
# -------------------------------
y_train_pred = model.predict(X_scaled)
train_r2 = model.score(X_scaled, y)
st.subheader("Model Performance")
st.write(f"R² Score on Training Data: {train_r2:.4f}")
