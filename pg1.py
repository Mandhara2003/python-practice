def greet_user(name):
  """Greets the user with a personalized message.

  Args:
    name: The user's name.

  Returns:
    A greeting message.
  """

  if not name:
    raise ValueError("Name cannot be empty.")

  if not name.isalpha():
    raise ValueError("Name cannot contain special characters or numbers.")

  return f"Hello, {name}!"