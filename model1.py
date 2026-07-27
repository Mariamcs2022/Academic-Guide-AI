import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, top_k_accuracy_score
import joblib

df = pd.read_csv(r"genaraldatatDONE4.csv")

X = df.drop(columns=["major", "Major_Group"])
y = df["Major_Group"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

RandomForestmodel = RandomForestClassifier( max_depth=10 ,  random_state=42)
RandomForestmodel.fit(X_train, y_train)   

y_pred = RandomForestmodel.predict(X_test) 
proba = RandomForestmodel.predict_proba(X_test)

top1_acc = accuracy_score(y_test, y_pred)
top2_acc = top_k_accuracy_score(y_test, proba, k=2)
top3_acc = top_k_accuracy_score(y_test, proba, k=3)

print(f" Top-1 Accuracy: {top1_acc:.4f}")
print(f" Top-2 Accuracy: {top2_acc:.4f}")
print(f" Top-3 Accuracy: {top3_acc:.4f}")

