import math  #I import this to be able to use the square root funciton


class variance:

  def __init__(
    self, user_data
  ):  #The list is being used here as a parameter which will later be passed to the function call
    self.user_data = user_data

  def mean(self):
    data_sum = 0
    for data_values_sum in self.user_data:
      data_sum += data_values_sum
    return data_sum / len(self.user_data)

  def median(self):
    user_data = self.user_data
    user_data.sort()
    data_len = len(user_data)
    middle_value = 0
    middle_value2 = 0
    median = 0
    if data_len % 2 == 0:
      middle_value = int(data_len / 2)
      middle_value2 = int(middle_value - 1)
      median = (user_data[middle_value] + user_data[middle_value2]) / 2
      return median
    else:
      middle_value = int(data_len / 2)
      return user_data[middle_value]

  def mode(self):
    user_data = self.user_data
    count = {}
    for mode_value in user_data:
      if mode_value in count:
        count[mode_value] += 1
      else:
        count[mode_value] = 1
    max_value = max(count.values())

    mode_final_value = []

    for key in count:
      if count[key] == max_value:
        mode_final_value.append(key)
    mode_val = mode_final_value
    return mode_val

  def range(self):
    user_data = self.user_data
    range = user_data[-1] - user_data[0]
    return range

  def var(self):
    user_data = self.user_data
    mean_call = variance(user_data)
    data_mean = mean_call.mean()
    values_minus_mean = []
    values_squared = []
    for data_minus_mean in user_data:
      data_minus_mean -= data_mean
      values_minus_mean.append(data_minus_mean)
    for squared_values in values_minus_mean:
      squared_values **= 2
      values_squared.append(squared_values)
    return variance(values_squared).mean()

  def stdv(self):
    user_data = self.user_data
    data_var = variance(user_data)
    data_variance = data_var.var()
    standard_deviation = math.sqrt(
      data_variance)  #used the square root function from the math library
    return standard_deviation


class quarters:

  def __init__(self, user_data):
    self.user_data = user_data

  def quarter1(self):
    user_data = self.user_data
    data_len = len(user_data)
    if data_len % 2 == 0:
      middle_value_index = data_len // 2
      lower_half_range = user_data[:middle_value_index]
      quarter3 = variance(lower_half_range)
      quarter3_median = quarter3.median()
    else:
      middle_value_index = data_len // 2
      upper_half_range = user_data[:middle_value_index + 1]
      quarter3 = variance(upper_half_range)
      quarter3_median = quarter3.median()
    return quarter3_median

  def quarter3(self):
    user_data = self.user_data
    data_len = len(user_data)
    middle_value_index = data_len // 2
    upper_half_range = user_data[middle_value_index:]
    quarter3 = variance(upper_half_range)
    quarter3_median = quarter3.median()
    return quarter3_median


print(
  "This program can do basic statistics,\nfor example: Mean, Median, Mode, etc.\nNote: leave sapace between consecutive numbers.\n(ie: 2 3 4 5)"
)

user_input = [
  int(i) for i in input("Input data: ").split()
]  #collects (directly from the user input) the user input in a list form, because the data for calculating should be in a list
user_input.sort()
varian = variance(
  user_input
)  #The user_input is being used by these funcitons to perform calculations (that will be shown in the function section)
quarts = quarters(user_input)
iq_range = quarts.quarter3() - quarts.quarter1()

user_choice_to_calculate = {
  'mean': varian.mean(),
  'median': varian.median(),
  'mode': varian.mode(
  ),  #The mode function is in the variance class (which is assigned to the "varian" variable). Just for clarification
  'range': varian.range(),
  'quarters': f"q1={quarts.quarter1()}, q3={quarts.quarter3()}",
  'std': varian.stdv(),
  'variance': varian.var(),
  'iqr': iq_range
}

all_commands = [
  'type any of the following commands below: ', 'mean', 'median', 'mode',
  'range', 'std for standard deviation', 'variance',
  'iqr for interquartile range',
  'quarters for both quarter1 and quarter3 (hence quarter is the median)',
  'to end the program type "exit()"'
]

try:
  while True:
    user_choice_input = input('what would you like me to calculate? ').lower()
    if user_choice_input in user_choice_to_calculate.keys():
      print(user_choice_to_calculate[user_choice_input])
    elif user_choice_input == '?' or user_choice_input == 'help':
      for commands in all_commands:
        print(commands)
    elif user_choice_input == 'exit()':
      break
    else:
      print(
        f"I don't recognize '{user_choice_input}'\nplease type '? or help' to see all possible commands."
      )
except Exception as e:
  print(e)

print("Program terminated successfully!")
