class MyList(list):
    """MyList class inherits from list and provides a method to print."""

    def print_sorted(self):
        """Print the elements of the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
