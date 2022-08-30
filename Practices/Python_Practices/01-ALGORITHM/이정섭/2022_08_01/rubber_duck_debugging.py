talking = input()
values = []
question = "문제"

while (talking != "고무오리 디버깅 끝"):
 
  talking = input()
  
  if talking == "문제":
    values.append(question)
  if talking == "고무오리":
    if len(values) == 0:
      values.append(question)
      values.append(question)
    else:
      values.pop()


print("고무오리야 사랑해") if len(values) == 0 else print("힝구")