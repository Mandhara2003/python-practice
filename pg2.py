import datetime

def calculate_age(birth_year):
  """Calculates the user's age based on the current year.

  Args:
    birth_year: The user's birth year.

  Returns:
    The user's age.
  """

  if not isinstance(birth_year, int):
    raise TypeError("Birth year must be an integer.")

  if birth_year < 1900 or birth_year > 2023:
    raise ValueError("Birth year must be between 1900 and 2023.")

  current_year = datetime.datetime.now().year
  age = current_year - birth_year
  return age