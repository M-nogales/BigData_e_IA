IN metrics
ValueError: Target is multiclass but average='binary'.
error apears if the metric is not a binary solution (0,1) an example can be a result of (1=low,2=medium,3=high)
add average (macro or weighted)
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')
auc_roc = roc_auc_score(y_test, y_pred_prob, multi_class='ovr')