# Detection Function
rf_model = RandomForestClassifier(
    **grid.best_params_,
    random_state=42,
    n_jobs=-1,
    class_weight=class_weight_dict
)

rf_model.fit(X_train, y_train)

# Hyperameter Tuning
param_grid = {
    "n_estimators": [300, 500],
    "max_depth": [10, 15],
    "min_samples_split": [2, 5, 10]
}

rf_base = RandomForestClassifier(
    random_state=42,
    n_jobs=-1,
    class_weight=class_weight_dict
)

print("\nRunning Grid Search...")

grid = GridSearchCV(
    estimator=rf_base,
    param_grid=param_grid,
    cv=3,
    scoring="accuracy",
    n_jobs=-1,
    verbose=1
)

grid.fit(X_train, y_train)

print("\nBest Parameters:")
print(grid.best_params_)

