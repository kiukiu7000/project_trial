# Import necessary resources
import math
import numpy as np
import pandas as pd
import os
import tensorflow as tf
from tensorflow import keras
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from torch.utils.data import DataLoader
from torchvision import transforms
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 
for dirname, _, filenames in  os.walk(""):
    for filename in filenames:
        print(os.path.join(dirname, filename))

pd.options.display.max_columns = None

# Load dataset
data = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

"""
# Check data
print(data.head)
print(data.dtypes)
print(data.isnull().sum())
"""
age_att=data.groupby(['Age','Attrition']).apply(lambda x:x['DailyRate'].count()).reset_index(name='Counts')
print(px.line(age_att,x='Age',y='Counts',color='Attrition',title='Agewise Counts of People in an Organization'))

print("End Program")