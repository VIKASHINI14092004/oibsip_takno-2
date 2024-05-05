import pandas as pd

df = pd.read_csv('Unemployment in India.csv', encoding='UTF-8-SIG')
print(df.head())
print(df.info())
# Fill missing values with the mean for numerical columns and mode for categorical columns
df.fillna({
    'Region': df['Region'].mode()[0],
    ' Date': df[' Date'].mode()[0],
    ' Frequency': df[' Frequency'].mode()[0],
    ' Estimated Unemployment Rate (%)': df[' Estimated Unemployment Rate (%)'].mean(),
    ' Estimated Employed': df[' Estimated Employed'].mean(),
    ' Estimated Labour Participation Rate (%)': df[' Estimated Labour Participation Rate (%)'].mean(),
    'Area': df['Area'].mode()[0]
}, inplace=True)
print('Missing values filled.')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Load and preprocess data
df[' Date'] = pd.to_datetime(df[' Date'])
label_encoders = {}
for column in ['Region', ' Frequency', 'Area']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Split data into features and target
X = df.drop(' Estimated Unemployment Rate (%)', axis=1)
y = df[' Estimated Unemployment Rate (%)']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')
