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
	def counting_sort(n: int, list_to_be_sorted: list, criterion: int, k: int, original_list: list):
		""" Sort a list in ascending order using the counting sort algorithm.

		- Its complexity is O(n).

		Parameters
		----------
		n : int
			The number of elements (length) in the list "list_to_be_sorted".

		list_to_be_sorted : list
			The list to be sorted.

		criterion : int
			The index of the element in the "list_to_be_sorted" by which it will be sorted.

		k : int
			The max greatness in the list "list_to_be_sorted".

		original_list : list
			The original list (without any tranformation).

		Returns
		-------
		sorted_list : list
			The "list_to_be_sorted" sorted in ascending order just keeping in mind the elements in the criterion index.
		"""
		relative_frecuency = [0] * k
		sorted_list = [None] * n

		# Index counting
		for element in list_to_be_sorted:
			relative_frecuency[element[0][criterion] - 1] += 1

		# Relative frecuency
		for i in range(1, k):
			relative_frecuency[i] += relative_frecuency[i - 1]

		# Sorting list
		for i in range(n - 1, -1, -1):
			sorted_list[relative_frecuency[list_to_be_sorted[i][0][criterion] - 1] - 1] = original_list[list_to_be_sorted[i][1]]
			relative_frecuency[list_to_be_sorted[i][0][criterion] - 1] -= 1

		return sorted_list
	
	@staticmethod
	def participation_per_animal(sorted_list, animals) -> dict:
		"""
		Still to be implemented.....
		"""

		dictionary = {}
		for animal in animals:
			dictionary[animal.name] = 0

		for act in sorted_list:
			for scene in act:
				for animal in scene:
					dictionary[animal.name] += 1

		return dictionary

class Methods:
	"""
	This class encapsulates all built-in methods used in our code.

	Methods
	-------
	- len(list)
	- sum(list)
	- max(list)
	- reverse(list)
	- zip(list1, list2)
	"""

	@staticmethod
	def len(list: list) -> int:
		""" Returns the length of a list.

		Parameters
		----------
		list : list
			The list whose length is to be returned.

		Returns
		-------
		length : int
			The length of the list.
		"""
		length = 0

		for _ in list:
			length += 1
		return length

	@staticmethod
	def sum(numbers : list) -> 'number':
		""" Returns the sum of the elements of a list.

		Parameters
		----------
		numbers : list
			The list whose elements are to be summed.

		Returns
		-------
		total : int
			The sum of the elements of the list.
		"""
		total = 0

		for number in numbers:
			total += number
		return total

	@staticmethod
	def max(list: list) -> 'number':
		""" Returns the maximum value in a list.

		Parameters
		----------
		list : list
			The list whose maximum value is to be returned.
		Returns
		-------
		max : int
			The maximum value in the list.
		"""
		max_element = list[0]

		for i in range(Methods.len(list)):
			if list[i] > max_element:
				max_element = list[i]
		return max_element

	@staticmethod
	def reverse(list: list) -> list:
		""" Returns the reversed list.

		Parameters
		----------
		reversed_list : list
			The list to be reversed.

		Returns
		-------
		reversed_list : list
			The reversed list.
		"""
		reversed_list = []

		for i in range(Methods.len(list) - 1, 0, -1):
			reversed_list.append(list[i])
		return reversed_list


	@staticmethod
	def zip(list1, list2) -> list:
		""" Returns the list of tuples, where each tuple contains the i-th element from each of the argument sequences.

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
		return [(list1[i], list2[i]) for i in range(Methods.len(list1))]
