_1st_dimension = []
while True:
	_name = input('請輸入名稱: ')
	if _name == 'q':
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

print(_1st_dimension) # 測試 A1

## 以下說明
# _1st_dimension[0][0] # 第1個[0] = 大清單第1個欄位
# _1st_dimension[0][0] # 第2個[0] = 大清單第1個欄位裡的第1個欄位
# print(_1st_dimension[0][0]) # 測試 B