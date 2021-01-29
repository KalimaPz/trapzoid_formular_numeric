
arr = [
  #x0     xn f(x)
  [0,     0.2],
  [0.2,   0.3683],
  [0.4,   0.3819],
  [0.6,   0.2282],
  [0.8,   0.2486],
  [1,     0.0082],
  [1.2,   0.1441],
]

ans_arr = []

def third_formular(): #0 -0.6

  return 0

def second_formular(): #0 - 0.4 , 0 - 0.8 . 0 -1

  temp_h1 = (arr[2][0]) / 3
  temp_h2 = (arr[4][0]) / 3
  temp_h3 = (arr[5][0]) / 3
  temp_h4 = (arr[6][0]) / 3

  ans = (3)

  return 0

def first_formular() : #0 - 0. 2 
  # (b - a) / n
  # print(arr[0][1])
  # print(len(arr[0]))

  temp_h = ( arr[0][1] - 0) / len(arr[0]) # temp is h value
  temp_i = temp_h / 2 * (arr[0][1] + (0.3683*2) )
  ans_arr.append(pow(10,5) * temp_i * pow(10,-3))
  return 0

for x in arr :
  # print(x[1])
  if x[1] == 0.2 :
    first_formular()
  if x[1] == 0.4 or x[1] == 0.8 or x[1] == 1 or x[1] == 1.2 :
    second_formular()
  if x[1] == 0.6 :
    third_formular()

print(ans_arr)
  # g = (b - a) / n 