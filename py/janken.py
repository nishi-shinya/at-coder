hands_dict = {
  '1': 'グー',
  '2': 'チョキ',
  '3': 'パー'
}


teki = 0
teki_arr = ["グー", "チョキ", "パー"]
count = 0
flg = True
while flg:
  tmp = input()
  if tmp != "グー" and tmp != "チョキ" and tmp != "パー":
    print('再入力してください')
    continue

  teki_te = teki_arr[teki % 3]

  if tmp == teki_te:
    print("あいこ")
    teki += 1
    continue

  if (tmp == "グー" and teki_te == "チョキ") or (tmp == "チョキ" and teki_te == "パー") or (tmp == "パー" and teki_te == "グー"):
    print("あなたの出した手:" + tmp)
    print("相手の出した手:" + teki_te)
    print("あなたは勝ちました")
    flg = False
    break

  if (tmp == "チョキ" and teki_te == "グー") or (tmp == "パー" and teki_te == "チョキ") or (tmp == "グー" or teki_te == "パー"):
    print("あなたの出した手:" + tmp)
    print("相手の出した手:" + teki_te)
    count += 1
    teki += 1
    if count == 3:
      print("あなたは負けました")
      flg = False
      break
    else:
      print("あなたの負け、再チャレンジ")
