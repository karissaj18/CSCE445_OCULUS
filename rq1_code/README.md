# Replication Package: Predicting Programmer Expertise and Language Background Using Eye-Tracking Metrics

## Overview

This replication package supports the study titled **“Exploring Machine Learning and Eye Movement Patterns to
Predict Programmer Expertise and English Proficiency in Code
Comprehension”**. 
It includes all code and processed fixation data required to replicate two binary classification tasks using machine learning:

1. **Programming Expertise Classification** (Expert vs. Novice)
2. **Language Background Classification** (Native vs. Non-Native English Speaker)

Both tasks use participant-level features derived from eye-tracking data in the EMIP dataset and are modeled using Random Forest classifiers.

## File Structure

replication_package/  
├── README.md  
├── requirements.txt  
├── code/  
│ ├── expertise_classification/  
│ │ ├── feature_extraction.py  
│ │ └── model.py  
│ └── language_classification/  
│ ├── feature_extraction.py  
│ └── model.py  
├── reactangle_data/  
│ ├── expert_fixations/  
│ ├── novice_fixations/  
│ ├── native_fixations/  
│ └── nonnative_fixations/  



## Requirements

### 1. Download the Fixation Data

The `reactangle_data/` folder contains preprocessed fixation files organized by participant category. To reproduce the results:

- Download the fixation data from this repository or source [🔗 OneDrive Link](https://uofnelincoln-my.sharepoint.com/:f:/r/personal/gagrawal2_unl_edu/Documents/Eye%20Tracking%20Project%20-%20Oculus/rectangle_data?csf=1&web=1&e=uEDYWl).
- Place the entire `reactangle_data/` folder at the root of the replication package.

Then filter and structure the data into the following subfolders:
- `expert_fixations/`
- `novice_fixations/`
- `native_fixations/`
- `nonnative_fixations/`

### 2. Install Python Packages

Ensure you have Python 3.8 or higher. Install required packages using:

```bash
pip install -r requirements.txt
```
## Running the Code
1. Feature Extraction
Run the appropriate feature extraction script to generate the input CSV file for each task.

For expertise classification:
```bash
python code/expertise_classification/feature_extraction.py
```

For language classification:
```bash
python code/language_classification/feature_extraction.py
```
Each script outputs a fixation_features.csv file in the same directory.

2. Model Training and Evaluation
   Run the corresponding model script to train and evaluate the classifier.

For expertise classification:
```bash
python code/expertise_classification/model.py
```
For language classification:
```bash
python code/language_classification/model.py
```
Each script outputs:
Classification scores
A confusion matrix plot
Cross-validation accuracy scores

Data
The reactangle_data/ directory contains participant fixation data organized as follows:
- expert_fixations/: Fixation files for expert programmers
- novice_fixations/: Fixation files for novice programmers
- native_fixations/: Fixation files for native English speakers
- nonnative_fixations/: Fixation files for non-native English speakers