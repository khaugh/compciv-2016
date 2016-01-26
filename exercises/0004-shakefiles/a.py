import os

if os.path.exists('tempdata'):
	print('tempdata already exists')
else:
	os.makedirs('tempdata')
