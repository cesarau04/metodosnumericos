""
Write a function to return the name of the month as a string when provided an integer representing the month on the Gregorian calendar. Use the below table for reference. You can expect all test cases to provide a valid integer input.
#	Month Name
01	January
02	February
03	March
04	April
05	May
06	June
07	July
08	August
09	September
10	October
11	November
12	December
""
def month_name(num):
	month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
	return month_dict[num]
