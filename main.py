# import necessary libraries

import os
import re
import sys
import nltk
import json
import requests
import html5lib
import pandas as pd
import pyspark.sql.functions
import pyspark.sql.types as T
from datetime import datetime
from bs4 import BeautifulSoup
from pyspark.sql import Row
from textblob import TextBlob
from transformers import pipeline
from pyspark.sql.functions import explode, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import logging

from sklearn.metrics import accuracy_score,hamming_loss,classification_report

### Split Dataset into Train and Text
from sklearn.model_selection import train_test_split
# Feature engineering
from sklearn.feature_extraction.text import TfidfVectorizer

#from skmultilearn.adapt import MLkNN
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import string
import neattext as nt
import neattext.functions as nfx
from sklearn.utils import shuffle
import xgboost as xgb
from sklearn.multioutput import MultiOutputClassifier
from xgboost import XGBClassifier

from sklearn.ensemble import RandomForestClassifier

import ktrain
from ktrain import text

import matplotlib.pyplot as plt

from loguru import logger # https://github.com/Delgan/loguru

log_level = "info"

if __name__ == '__main__':        
    logger.info("main Function")

