import signal
import sys
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, validation_curve
from scikitplot.metrics import plot_roc, plot_confusion_matrix, plot_calibration_curve

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.naive_bayes import GaussianNB

from math import ceil, floor
from collections import Counter
pd.options.mode.chained_assignment = None  # default='warn'


def train(x_train, y_train, model):
  model.fit(x_train, y_train)
  return model


def predict(x_test, y_test, model):
  y_probs = model.predict_proba(x_test)
  y_pred = model.predict(x_test)
  return [accuracy_score(y_test, y_pred), y_pred, y_probs]


def plot_bar_chart(data, x_label, increment, cutoff, end):
  temp = {}
  for i in range(0, end, increment):
    key = str(i) if i < cutoff else f"{cutoff}+"
    temp[key] = 0
    for p in data:
      p = round(p)
      if key == f"{cutoff}+" and p >= cutoff:
        temp[key] += 1
      elif i <= p <= i + increment - 1:
        temp[key] += 1

  ranges = list(temp.keys())
  values = list(temp.values())

  fig = plt.figure(figsize=(10, 5))

  # creating the bar plot
  plt.bar(ranges, values, color='#9571eb', width=1, edgecolor='black')
  ax = plt.gca()

  y_min, y_max = 0, max(values) + 100
  ax.set_ylim(y_min, y_max)
  ax.set_yticks(range(y_min, y_max, 100))

  plt.xlabel(x_label)
  plt.ylabel("Frequency")
  plt.show()

def helper(x_train, x_test, y_train, y_test, model):
  model = train(x_train, y_train, model)
  acc, y_pred, y_probs = predict(x_test, y_test, model)
  print(f"Accuracy Score for model={model}:", acc)
  print()

  if isinstance(model, DecisionTreeClassifier):
    plot_tree(model)
    plt.show()

  """plot_roc(y_test, y_probs)
        plt.show()
      
        plot_confusion_matrix(y_test, y_pred)
        plt.show()"""

  return y_probs, y_pred

def signal_handler(signal, frame):
  print(2)
  # df_rainfall.to_csv(final_dataset, index=False)
  # [f.cancel() for f in futures]
  # Accessing protected member of a class here (could fail in future versions)
  try:
    """for pid, proc in executor._processes.items():
      if proc.is_alive():
        proc.terminate()
    executor.shutdown()"""
    pass
  except Exception as e:
    print(e)
  finally:
    sys.exit(0)


if __name__ == '__main__':
  # warnings.filterwarnings("ignore", category=RuntimeWarning)
  signal.signal(signal.SIGINT, signal_handler)
  signal.signal(signal.SIGTERM, signal_handler)

  final_dataset_with_elevations = 'nasa_glc_india_final_elevation.csv'
  df = pd.read_csv(final_dataset_with_elevations)

  #plot_bar_chart(df['short_term_rainfall'], "Short Term Rainfall (mm)", 50, 200, 400)
  #plot_bar_chart(df['long_term_rainfall'], "Long Term Rainfall (mm)", 50, 600, 800)
  #plot_bar_chart(df['elevation_relief'], "Elevation Relief (m)", 500, 3201, 3200) # pass 'cutoff' more than 'end'

  X = df[['short_term_rainfall', 'long_term_rainfall', 'elevation_relief']]
  Y = df['isRainfallInducedLandslide']

  print("X:", Counter(X))
  print("Y:", Counter(Y))

  over_sampler = SMOTE(sampling_strategy='minority', random_state=42)
  X_NEW, Y_NEW = over_sampler.fit_resample(X, Y)

  print("X_NEW:", Counter(X_NEW))
  print("Y_NEW:", Counter(Y_NEW))

  x_train, x_test, y_train, y_test = train_test_split(X_NEW, Y_NEW, test_size=1/3, random_state=42)
  
  # Logistic Regression
  #helper(x_train, x_test, y_train, y_test, model=LogisticRegression(random_state=42))

  # Decision Tree
  #y_probs, y_pred = helper(x_train, x_test, y_train, y_test, model=DecisionTreeClassifier(max_depth=3, random_state=42))

  # Support Vector Machine
  #helper(x_train, x_test, y_train, y_test, model=SVC(probability=True, random_state=42))

  # Naive Bayes Classifier
  helper(x_train, x_test, y_train, y_test, model=GaussianNB())

  df = pd.read_csv('dataset_with_probs.csv')

  print(len(df['latitude']))

  df1 = df.drop_duplicates()
  print(len(df1['latitude']))

  """x_train['LandslideProb'] = y_train
  x_test['LandslideProb'] = [temp[1] for temp in y_probs]
  final = pd.concat([x_test, x_train])
  final.to_csv('dataset_with_probs.csv', index=False)"""