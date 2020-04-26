# 利用 python 開啟檔案將內容存成清單
_1st_dimension = []
print('')
print('continue 迴圈內跳過語法特定字串')
print('可以用來清除 csv 標題\n')

with open('prod.csv', 'r', encoding='utf-8') as f:
	for line in f:	#每行定義為 line
		if '商品,價格' in line:
			continue
		_name, _price = line.strip().split(',')	# 用 strip 刪掉換行符號 , 用 split 切割逗點變成清單
		_1st_dimension.append([_name, _price])
print(_1st_dimension)

