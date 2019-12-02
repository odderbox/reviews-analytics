data = []
count = 0
sum_len = 0
less_then_h = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		sum_len += len(line)
		if len(line) < 100:
			less_then_h.append(line)
		if count % 10000 == 0:
			print(len(data))
			

print('檔案讀取完畢，共有', count, '筆資料')

print('留言平均長度為：', sum_len / count)

print('留言小於100長度的筆數有：', len(less_then_h))