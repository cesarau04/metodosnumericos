def find_index(lst, str):
	for word in lst:
		if word==str:
			return lst.index(word)
