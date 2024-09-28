def calculate_area(length, width):
  """Calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """

  if not (1 <= length <= 1000 and 1 <= width <= 1000):
    raise ValueError("Length and width must be between 1 and 1000.")

  return length * width

# Example usage:
length = 5
width = 10
area = calculate_area(length, width)
print(f"The area of the rectangle is {area}")