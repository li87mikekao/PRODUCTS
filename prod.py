_1st_dimension = []
while True:
	_name = input('請輸入名稱: ')
	if _name == 'q':	# 當輸入 q 表示離開
		break
	_price = input('請輸入價格: ')
# 寫法1 , 理解用
	# _2nd_dimension = []
	# _2nd_dimension.append(_name) 
	# _2nd_dimension.append(_price)
	# _1st_dimension.append(_2nd_dimension)
# 寫法2
	# _2nd_dimension = [_name, _price]
	# _1st_dimension.append(_2nd_dimension)
# 寫法3
# 7-10 行簡寫
	_1st_dimension.append([_name, _price])

print(_1st_dimension)

## 以下說明
# _1st_dimension[0][0]	# 第1個[0] = 大清單第1個欄位
# _1st_dimension[0][0]	# 第2個[0] = 大清單第1個欄位裡的第1個欄位

for _2nd_dimension in _1st_dimension:
	# print(_2nd_dimension)			# 測試A , 利用迴圈印出第二階所有內容
	print(_2nd_dimension[0])		# 測試B , 利用迴圈印出第二階指定內容

with open('prod.csv', 'w', encoding='utf-8') as f:	# excel 直接開會亂碼 , sublime 開 py 檔案正常
# with open('prod.csv', 'w') as f:	# excel 直接開正常 , sublime 開 py 檔案亂碼
	# 上面說明
	# with = 自動把open的檔案close , open = 打開電腦檔案(如果有會覆蓋,沒有會產生) , w = write , f = 命名, 編碼 = utf-8
	f.write('商品,名稱\n')	#增加一行
	for _2nd_dimension in _1st_dimension:
		f.write(_2nd_dimension[0] + ',' + _2nd_dimension[1] + '\n')	# write 真正寫入 , 用逗號區隔 , \n = 換行
