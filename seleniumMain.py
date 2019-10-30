from selenium import webdriver
from bs4 import BeautifulSoup
import variables
import time
import re
import unittest
import sys
import os.path
import inspect



class seleniumMain(unittest.TestCase):
    def setUp(self):
        if getattr(sys, 'frozen', False):
            self.savePath = input('File Save Location: ')
            # executed as a bundled exe, the driver is in the extracted folder
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            self.driver = webdriver.Chrome(chromedriver_path)
        else:
            # executed as a simple script, the driver should be in `PATH`
            current_folder = os.path.realpath(
                os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
            chromedriver_path = os.path.join(current_folder, "drivers\\chromedriver.exe")
            self.driver = webdriver.Chrome(chromedriver_path)
            self.savePath = variables.savePath


    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(variables.websiteLink)
        time.sleep(10)

        mainHTML = BeautifulSoup(driver.page_source, "html.parser")

        seriesTypes = mainHTML.find_all('section', {'class': 'section loaded'})
        
        exactSeriesType = None
        for typeLists in seriesTypes:
            type = typeLists.find('h2').find(text=True, recursive=False).strip().lower()
            if variables.findType.lower() == type:
                exactSeriesType = typeLists

        allSeries = exactSeriesType.find_all('div', {'class': 'media-card'})

        outputFile = open(os.path.join(self.savePath, time.strftime("%Y%m%d_%H%M%S") + '_testFile.csv'), 'w', encoding='utf-8')

        for series in allSeries:
            seriesName = self.doubleQuote(series.find('a', {'class': 'title'}).string)
            seriesScore,seriesPopularity = [stat.string for stat in series.find_all('span', {'class': 'stat'})]

            if '.' in seriesScore:
                seriesScore = self.doubleQuote(str(re.search(r'\d+\.\d+', seriesScore).group()))
            else:
                seriesScore = self.doubleQuote(str(re.search(r'\d+', seriesScore).group()))

            seriesPopularity = self.doubleQuote(str(re.search(r'\d+', seriesPopularity).group()))

            printValues = seriesName + ',' + seriesScore + ',' + seriesPopularity + '\n'

            outputFile.write(printValues)

    def tearDown(self):
        self.driver.close()

    def doubleQuote(self, value):
        if '"' in value:
            value = value.replace('"', "'")
        return '"' + value + '"'


if __name__ == "__main__":
    unittest.main()
