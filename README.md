# website : https://wine-qualit.herokuapp.com/

# Project
  Use multiple machine learning classification algorithms to predict the wine quality.
  
# Result
After resampling, the random forest model has 90.3% accuracy on the test data, and it performs pretty well on the good and low quality group wine, however, it sacrifices too much accuracy on the medium group. The SVM, which has 78% accuracy on the test data, is like a balanced model, it doesn't performs as well as Random Forest on the low and good group, but it improves their accuracy compare to svm without resampling, and it does not lose too much accuracy on the medium wine. Based on the business idea, the company could use either model to classify their wine quality.


