def diff(self, dic1, dic2):
        """Compare two dictionaries and return changes in the second dictionary. """
        change = [x for x in dic1 if dic1[x] != dic2[x]]
	return change
