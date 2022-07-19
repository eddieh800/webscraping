from selenium import webdriver
import os
import booking.constants as const
from booking.booking_filtration import filtration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
	def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown = False): #stores information of location of our drivers
		self.driver_path = driver_path
		self.teardown = teardown
		os.environ['PATH'] += self.driver_path
		super(Booking, self).__init__()
		self.implicitly_wait(15)
		self.maximize_window() #just for aesthetics
	
	def __exit__(self, exc_type, exc_al, exc_tb): #this was autofilled by pycharm
		if self.teardown:
			self.quit() 
			#Purpose is to shut down browser once python get out of indentation in run.py, with Booking() as bot. Default is set at False above

	def land_first_page(self):
		#you have access to all methods in booking and methods in selenium now
		self.get(const.BASE_URL)

	def change_currency(self, currency=None):
		currency_element = self.find_element_by_css_selector(
			'button[data-tooltip-text="Choose your currency"]'
		)
		currency_element.click()
		selected_currency_element = self.find_element_by_css_selector(
			f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
			# a is for <a> anchor in HTML, and *= is for substring
		)
		select_currency_element.click()

	def select_place_to_go(self, place_to_go):
		search_field = self.find_element_by_id(’ss’) #this is the no button in the popup
		search_field.clear() #cleans the text box first
		search_field.send_keys(place_to_go)
		
		first_result = self.find_element_by_css_selector(
			'li[data-i="0"]'
			# <li> : list HTML
		)
		first_result.click()

	def select_dates(self, check_in_date, check_out_date):
		check_in_element = self.find_element_by_css_selector(
			f'td[data-date={check_in_date}]'
			# <td> is table data. child element of <table>
		)
		checkin_date_element.click()

		check_out_element = self.find_element_by_css_selector(
			f'td[data-date={check_out_date}]'
		)
		check_out_element.click()

	def select_adults(self, count=1):
		selection_element = self.find_element_by_id('xp__guests__toggle')
		selection_element.click()

		while True:
			decrease_Adults_element = self.find_element_by_css_selector(
				'button[aria-label="Decrease number of Adults"]'
			)
			decrease_adults_element.click()
	
			# If the value of adults reaches 1, then we should get out
			# of the while loop
			adults_value_element = self.find_element_id('group_adults')
			adults_value = adults_value_elements.get_attribute(
				'value'
			)
	
			if int(adults_value) == 1:
				break

		increase_button_element = self.find_element_by_css_selector(
			'button[aria-label="Increase number of Adults"]'
		)
		
		for _ in range(count-1):
			increase_button_element.click()

	def click_search():
		search = self.find_element_by_css_selector(
			'button[type="submit]'
		)
		search.click()

	def apply_filtrations(self):
		filtration = BookingFiltration(driver=self)
		filtration.apply_star_rating(4,5)
		filtration.sort_price_lowest_first()
		
	def report_results(self):
		# parent 
		hotel_boxes = self.find_element_by_id(
			'hotellist_inner'
		)
		# children
		#).find_elements_by_class_name('sr_property_block')

		report = BookingReport(hotel_boxes)
		table = PrettyTable(
			field_names = ['Hotel Name', 'Hotel Price', 'Hotel Score']
		)
		table.add_rows(report.pull_deal_box_attributes())
		print(table)
