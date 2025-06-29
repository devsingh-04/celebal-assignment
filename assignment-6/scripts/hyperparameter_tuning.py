from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

def run_grid_search(model, param_grid, X_train, y_train, cv=5):
    grid = GridSearchCV(model, param_grid, cv=cv, scoring='f1', n_jobs=-1)
    grid.fit(X_train, y_train)
    return grid.best_estimator_, grid.best_params_

def run_random_search(model, param_dist, X_train, y_train, cv=5, n_iter=10):
    random = RandomizedSearchCV(model, param_distributions=param_dist, cv=cv, 
                                scoring='f1', n_iter=n_iter, n_jobs=-1)
    random.fit(X_train, y_train)
    return random.best_estimator_, random.best_params_
