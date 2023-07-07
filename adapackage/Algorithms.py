from adapackage import Scene


class Algorithms:
	"""
	This class encapsulates the algorithms used for sorting.

	Methods
	-------
	merge(list_to_be_sorted, left, middle, right)

	merge_sort(list_to_be_sorted, left, right)

	couting_sort(list_to_be_sorted, sorted_list, k)
	"""

	@staticmethod
	def merge(list_to_be_sorted: list, left: int, middle: int, right: int) -> None:
		""" Merges two sublists of the list_to_be_sorted.
		These sublists are:
			- list_to_be_sorted[left..middle]
			- list_to_be_sorted[middle + 1..right]
		In order for merge to work, each of the sublists must be already sorted in ascending order.
		Its complexity is O(n).

		Parameters
		----------
		list_to_be_sorted: list
			The list to be sorted.

		left: int
			The index that keeps track of the leftmost element of the first sublist.

		middle: int
			The index that keeps track of the rightmost element of the first sublist.

		right: int
			The index that keeps track of the rightmost element of the second sublist.

		Returns
		-------
		None
			Modifies the list to be sorted in place, so it does not return anything.
		"""

		n_left: int = middle - left + 1
		n_right: int = right - middle


		left_list: list = [None for _ in range(n_left)]
		right_list: list = [None for _ in range(n_right)]

		for i in range(n_left):
			left_list[i] = list_to_be_sorted[left + i]


		for j in range(n_right):
			right_list[j] = list_to_be_sorted[middle + 1 + j]

		i: int = 0
		j: int = 0
		k: int = left

		# As long as each sublist has at least one element,
		# compare the elements of the sublists and add the smallest one to the list to be sorted.
		while i < n_left and j < n_right:
			if left_list[i] <= right_list[j]:
				list_to_be_sorted[k] = left_list[i]
				i += 1

			else:
				list_to_be_sorted[k] = right_list[j]
				j += 1

			k += 1

		# If the right sublist has no elements left,
		# add the remaining elements of the left sublist to the list to be sorted.
		while i < n_left:
			list_to_be_sorted[k] = left_list[i]
			i += 1
			k += 1

		# If the left sublist has no elements left,
		# add the remaining elements of the right sublist to the list to be sorted.
		while j < n_right:
			list_to_be_sorted[k] = right_list[j]
			j += 1
			k += 1

	@staticmethod
	def merge_sort(list_to_be_sorted: list, left: int, right: int) -> None:
		""" Sort a list in ascending order using the merge sort algorithm.

		- This function follows a divide and conquer approach.
		- Its complexity is O(nlogn).

		Parameters
		----------
		list_to_be_sorted: list
			The list to be sorted.

		left: int
			The index that keeps track of the leftmost element of a sublist of the list that is being sorted at the moment.

		right: int
			The index that keeps track of the rightmost element of a sublist of the list that is being sorted at the moment.

		Returns
		-------
		None
			Modifies the list to be sorted in place, so it does not return anything.
		"""

		if left < right:
			middle: int = (left + right) // 2

			# Divide phase
			Algorithms.merge_sort(list_to_be_sorted, left, middle)       # T(n/2)
			Algorithms.merge_sort(list_to_be_sorted, middle + 1, right)  # T(n/2)

			# Conquer phase
			Algorithms.merge(list_to_be_sorted, left, middle, right)     # O(n)

	@staticmethod
	def counting_sort(list_to_be_sorted: list[Scene], k: int) -> None:
		""" Sort a list in ascending order using the counting sort algorithm.

		- Its complexity is O(n).

		Parameters
		----------
		list_to_be_sorted : list
			The list to be sorted.

		k : int
			The max greatness in the list list_to_be_sorted of scenes.

		Returns
		-------
		sorted_list : list
			The list_to_be_sorted sorted in ascending order.
		"""
		sorted_list_length: int = Methods.len(list_to_be_sorted)
		sorted_list = [None for _ in Methods.range(0, sorted_list_length, 1)]

		# Initialize C with zeros
		relative_frecuency = [0 for _ in Methods.range(0, k + 1, 1)]

		# Index counting
		for i in Methods.range(0, sorted_list_length, 1):
			relative_frecuency[list_to_be_sorted[i].greatness] += 1

		# Relative frequency
		for i in Methods.range(1, k + 1, 1):
			relative_frecuency[i] += relative_frecuency[i - 1]


		print(relative_frecuency, sorted_list, sorted_list_length)
		# Assignation
		for i in Methods.range(sorted_list_length - 1, -1, -1):
			sorted_list[relative_frecuency[list_to_be_sorted[i].greatness] - 1] = list_to_be_sorted[i].greatness
			relative_frecuency[list_to_be_sorted[i].greatness] -= 1

		return sorted_list


class Methods:
	"""
	This class encapsulates all built-in methods used in our code.

	Methods
	-------
	range(start, stop)
	len(list)
	max(list)
	reverse(list)
	zip(list_to_be_sorted, left, middle, right)
	"""

	""" Return the list of integers in the range [start, stop) with a specified step.

	Parameters
	----------
	start : int
		The starting value of the sequence.

	stop : int
		The end value of the sequence.

	step : int
		The difference between each integer in the sequence.

	Returns
	-------
	list : list
		The list of integers in the range [start, stop) with a specified step.
	"""
	@staticmethod
	def range(start: int, stop: int, step: int) -> list:
		list = []

		if step < 0:
			while start > stop:
				list.append(start)
				start += step
		else:
			while start < stop:
				list.append(start)
				start += step

		return list

	""" Return the length of a list.

	Parameters
	----------
	list : list
		The list whose length is to be returned.

	Returns
	-------
	length : int
		The length of the list.
	"""
	@staticmethod
	def len(list: list) -> int:
		length = 0

		for _ in list:
			length += 1
		return length

	""" Return the maximum value in a list.

	Parameters
	----------
	list : list
		The list whose maximum value is to be returned.
	Returns
	-------
	max : int
		The maximum value in the list.
	"""
	@staticmethod
	def max(list: list) -> int:
		max = list[0]

		for i in range(Methods.len(list)):
			if list[i] > max:
				max = list[i]
		return max

	""" Return the reversed list.

	Parameters
	----------
	reversed_list : list
		The list to be reversed.

	Returns
	-------
	reversed_list : list
		The reversed list.
	"""
	@staticmethod
	def reverse(list: list) -> list:
		reversed_list = []

		for i in Methods.range(Methods.len(list) - 1, -1, -1):
			reversed_list.append(list[i])
		return reversed_list

	""" Return the list of tuples, where each tuple contains the i-th element from each of the argument sequences.

	Parameters
	----------
	list1 : list
		The list to be "zipped" with list2.

	list2 : list
		The list to be "zipped" with list1.
	Returns
	-------
	 : list
		The list of tuples, where each tuple contains the i-th element from each of the argument sequences.
	"""
	@staticmethod
	def zip(list1, list2) -> list:
		return [(list1[i], list2[i]) for i in Methods.range(0, Methods.len(list1), 1)]