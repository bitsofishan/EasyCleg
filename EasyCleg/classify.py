class classify():
   def classify(X_train,y_train): 
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    #Some dataset,cross validation libraries
    from sklearn.datasets import load_boston,load_iris
    from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV
    from sklearn.pipeline import Pipeline
    #Preprocessing Library
    from sklearn.preprocessing import PolynomialFeatures,StandardScaler
    #ML Models 
    from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet,LogisticRegression
    from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier
    from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
    from sklearn.svm import SVC
    pipe=Pipeline([
    ("scaler",StandardScaler()),
    
    ("classifier",LogisticRegression())
    ])
    param_grid=[
    {
    "classifier":[LogisticRegression(max_iter=10000000)],
    "classifier__C":[0.05,0.1,1.0,5,10]
    },
    {
    "classifier":[DecisionTreeClassifier()],
    "scaler":["passthrough"]
    },
    {
    "classifier":[RandomForestClassifier()],
    "classifier__n_estimators":[100,300,500],
    "scaler":["passthrough"],
    },
    {
    "classifier":[SVC()],
    "classifier__gamma":[1,0.1,0.01],
    "classifier__C":[1,100,1000]
       
    },
    
    ]
    grid=GridSearchCV(pipe,param_grid=param_grid,cv=5)
    grid.fit(X_train,y_train)
    print("Best Score: ",grid.best_score_)
    print("Best Params: ",grid.best_params_)
    print("Best Estimator: ",grid.best_estimator_)
    