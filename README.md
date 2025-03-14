# CSCE445_OCULUS
CSCE445 Group Project 

This project uses the EMIP dataset introduced here - https://acris.aalto.fi/ws/portalfiles/portal/51229125/SCI_Bednarik_EMIP.emip.pdf.

Stimuli:
  - Task 2: Rectangle
      - Java: https://github.com/karissaj18/CSCE445_OCULUS/blob/main/data/rectangle_java.jpg
      - Python: https://github.com/karissaj18/CSCE445_OCULUS/blob/main/data/rectangle_python.jpg
      - Scala: https://github.com/karissaj18/CSCE445_OCULUS/blob/main/data/rectangle_scala.jpg
  - Task 5: Vehicle
      - Java: https://github.com/karissaj18/CSCE445_OCULUS/blob/main/data/vehicle_java.jpg
      - Python: https://github.com/karissaj18/CSCE445_OCULUS/blob/main/data/vehicle_python.jpg
      - Scala: https://github.com/karissaj18/CSCE445_OCULUS/blob/main/data/vehicle_scala.jpg
   
Task - Read code and answer multiple choice question to evaluate comprehension

Study Metadata: https://github.com/karissaj18/CSCE445_OCULUS/blob/main/data/emip_metadata.csv


RQ1:
    Dependent Variables: Eye-tracking metrics such as fixation duration, saccade length, regression count, and pupil dilation.
    Independent Variable: Programming expertise level (high, medium, low, none) and experiment language expertise level (high, medium, low, none)
  

RQ2:
    Dependent Variables: Eye-tracking metrics including fixation counts, fixation durations, and linearity metrics (vertical next, vertical later, horizontal later, regression, and line regression)
    Independent Variables: Native language (native and non-native English speakers) and English proficiency (high, medium, low)

Metric Definitions:
  - Vertical Next: % of forward saccades that either stay on the same line or move one line down.
  - Vertical Later: % of forward saccades that either stay on the same line or move down any number of lines.
  - Horizontal Later: % of forward saccades within a line 
  - Regression: % of backward saccades of any length 
  - Line Regression: % of backward saccades within a line

Code:
  EMIP_TOOLKIT_EXAMPLES.ipynb - Toolkit from https://dl.acm.org/doi/pdf/10.1145/3448018.3457425 for processing EMIP      dataset
  stats.ipynb - Code to aggregate data by independent variables and calculate fixation durations and linearity metrics


Project Estimated Timeline:
Finish Testing ML models - 4/18
Finish Data Analysis - 5/9
Finish Final Report - 5/16










