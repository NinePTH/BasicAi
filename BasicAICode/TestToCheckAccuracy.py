y_pred = LogReg.predict(x_test)

score = LogReg.score(x_test,y_test)
percent_score = round(score*100,2)
print("Accuracy =",percent_score)
