#This file will include a class with instance methods
#That will be responsible to interact with our website
#After we have some results, to apply filtrations.

#this allows you to identify driver as a WebDriver type to allow autocompletions
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
		def __init__(self, driver:WebDriver):
				self.driver = driver #receives original driver from booking class
		
		# *star_values turns it into an arbitrary argument as opposed to a single value star_value
		def apply_star_rating(self, *star_values):
				#find the parent element
				star_filtration_box = self.driver.find_element_by_id('filter_class')
				#identify the child elements. * is all child elements
				star_child_elements = star_filtration_box.find_elements_by_css_selector('*')
				
				for star_value in star_values:
						for star_element in star_child_elements:
								# innerHTML gets the text ie. #<h1>Jim</h1>, we get Jim
								# strip cleans up white spaces
								if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars' 
										star_element.click()
		
		def sort_price_lowest_first(self):
				element = self.driver.find_element_by_css_selector(
						'li[data-id="price"]'
				)
				element.click()
