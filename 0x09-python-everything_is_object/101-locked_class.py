#!/usr/bin/python3
class LockedClass:
	"""LockedClass that prevents the user from dynamically creating
	new instance attributes """
	__slots__ = ['first_name']
