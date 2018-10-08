#!/usr/bin/env python


def is_update_required(original, proposed):
	if isinstance(original, dict):
		for key, value in original.items():
			try:
				if value != proposed[key]:
					print(value, proposed[key])
					return True
			except KeyError:
				print(original[key])
				return True
			if isinstance(value, list):
				return is_update_required(value, proposed[key])
			elif isinstance(original[key], str) and isinstance(proposed[key], str):
				if original[key] != proposed[key]:
					print(original[key], proposed[key])
					return True
		return False
	elif isinstance(original, list):
		if len(original) != len(proposed):
			print(len(original), len(proposed))
			return True
		for a, b in zip(original, proposed):
			if a != b:
				print(a, b)
				return True
			if isinstance(a, dict) and isinstance(b, dict):
				is_update_required(a, b)
			return False


hobbies = ['computers', 'cooking', 'gardening']
hobbies2 = ['computers', 'cooking', 'gardening']

data = {'name': 'Kevin',
		'hobbies': hobbies,
		}

data2 = {'name': 'Kevin',
		'hobbies': hobbies2,
		}

original = [data]
proposed = [data2]
print(is_update_required(original, proposed))