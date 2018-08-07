""
Write a function to return the name of the month as a string when provided an integer representing the month on the Gregorian calendar. Use the below table for reference. You can expect all test cases to provide a valid integer input.
#	Month Name
1	January
2	February
3	March
4	April
5	May
6	June
7	July
8	August
9	September
10	October
11	November
12	December
""
def month_name(num):
	month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
	return month_dict[num]
