from booking.booking import Booking

with Booking() as bot:
	bot.land_first_page()
	bot.change_currency(currency = 'USD')
	bot.select_place_to_go('New York')
	bot.select_dates(check_in_date = '2022-05-16',
									 check_out_date = '2022-05-23')
	bot.select_adults(10)
	bot.click_search()
	bot.apply_filtrations()
	bot.refresh() #a workaround to let our bot grab data properly because we pulled before sorting finished the job
	bot.report_results()
