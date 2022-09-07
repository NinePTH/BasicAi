import seaborn as sns
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize = (9,9))
sns.heatmap(cm, annot=True, fmt='.0f', linewidths=1,cmap='Blues_r')
plt.xlabel('Predict')
plt.ylabel('Actual')
