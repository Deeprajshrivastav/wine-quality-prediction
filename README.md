# website : https://wine-qualit.herokuapp.com/

# Project
  Use multiple machine learning classification algorithms to predict the wine quality.
# Dataset
I used Kaggle’s Red Wine Quality dataset to build various classification models to predict whether a particular red wine is “good quality” or not. Each wine in this dataset is given a “quality” score between 0 and 10. For the purpose of this project, I converted the output to a binary output where each wine is either “good quality” (a score of 7 or higher) or not (a score below 7). The quality of a wine is determined by 11 input variables:
# Result
After resampling, the random forest model has 90.3% accuracy on the test data, and it performs pretty well on the good and low quality group wine, however, it sacrifices too much accuracy on the medium group. The SVM, which has 78% accuracy on the test data, is like a balanced model, it doesn't performs as well as Random Forest on the low and good group, but it improves their accuracy compare to svm without resampling, and it does not lose too much accuracy on the medium wine. Based on the business idea, the company could use either model to classify their wine quality.


