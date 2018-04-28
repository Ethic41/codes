n = input()

vals = []
for i in range(n):
	v = input()
	vals.append(v)

def calc(vals):
	ans_list = []
	tgt_val = round(round(sum(vals)/n,3),2)
	for val in vals:
		if val > tgt_val:
			c = val - tgt_val
			ans_list.append(round(c,2))
	print("%.2f" % sum(ans_list))

calc(vals)