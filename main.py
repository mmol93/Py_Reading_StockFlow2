from selenium import webdriver
from datetime import datetime
import os
import shutil
import time
import numpy
import successiveForegin
import dollarIndex

# 외국인 수급 7일치 가져오기 - C
successiveForeginKOSPI = successiveForegin.FivedayForeignKOSPI()
successiveForeginKOSDAQ = successiveForegin.FivedayForeignKOSDAQ()

# 달러 인덱스 7일치 확인 - C
dollarList = dollarIndex.dollarIndex()

