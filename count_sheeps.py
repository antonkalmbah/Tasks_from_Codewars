sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]


def count_sheeps(sheep):
  count = 0
  for i in sheep:
      if i == True:
          count += 1
      elif i == 'null' or i == 'indefined':
          pass
      else:
          pass
  print(count)


# более простой способ
# print(sheep.count(True))


count_sheeps(sheep)
