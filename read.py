data = []
count = 0
l = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		l += len(line)
		if count % 10000 == 0:
			print(len(data))
			

print('檔案讀取完畢，共有', count, '筆資料')

print('留言平均長度為：', l / count)