from adapackage.Animal import Animal
from adapackage.Scene import Scene
from adapackage.Act import Act


class Algorithms:
	"""
	This class encapsulates the algorithms used for sorting.

	Methods
	-------
	merge(list_to_be_sorted, left, middle, right)
	
	merge_sort(list_to_be_sorted, left, right)

	couting_sort(list_to_be_sorted, max_value)
	"""

	@staticmethod
	def merge(list_to_be_sorted: list, left: int, middle: int, right: int) -> None:
		"""
		Merges two sublists of the list_to_be_sorted.
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
			if left_list[i]	<= right_list[j]:
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
		"""
		Sort a list using the merge sort algorithm.
		This function follows a divide and conquer approach. Its complexity is O(nlogn).

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

			


