from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load sample dataset
X, y = load_iris(return_X_y=True)
print(X.shape)
print(y.shape)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
print(type(X_test))
# Random Forest model
model = RandomForestClassifier(
    n_estimators=100,      # number of trees
    max_depth=5,           # limits tree depth
    min_samples_split=2,   # minimum samples needed to split a node
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
