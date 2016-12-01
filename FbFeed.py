from lxml import html
from selenium import webdriver
import os
import time
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

class NewsFeed:

	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.browser = webdriver.Firefox()
		self.POI = []

	def login(self):
		
		self.browser.get('http://www.facebook.com')
		inputElement = self.browser.find_element_by_id("email")
		inputElement.send_keys(self.username)
		inputElement = self.browser.find_element_by_id("pass")
		inputElement.send_keys(self.password)
		inputElement.submit()

	def read(self):

		while(1):

			self.browser.get('http://www.facebook.com')
			page = self.browser.page_source
			with open('temp.html','w') as f:
				f.write(page)

				with open('temp.html','r') as f:
					page = f.read()

					tree = html.fromstring(page)

					names = tree.xpath(
						'//div[contains(@class, "fbFeedTickerStory")]/a/div/div/div/div/span/text()'
						)
					feeds = tree.xpath(
						'//div[contains(@class, "fbFeedTickerStory")]/a/div/div/div/div/text()'
						)
			for name,feed in zip(names,feeds):			
				if name in self.POI:
					print name + ' : ' + feed
					for i in range(3):
						os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga')
						time.sleep(0.5)

			time.sleep(5)


	def add(self,name):
		self.POI.append(name)


	def show(self):
		if not self.POI:
			print('No people to show')
		else:
			print(self.POI)