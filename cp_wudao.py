import shutil 
import os 
import argparse 
import sys 

input_root = './WuDao_processed' 
output_root = '/dataset/fd5061f6/chinese_data/WuDao_processed'
fs = os.listdir(input_root)
fs = [os.path.join(input_root, i) for i in fs] 
nums = sys.argv[1] 
print('will copy {} files'.format(nums))
nums = int(nums)
existed_files = os.listdir(output_root)
need_file = [i for i in fs if os.path.basename(i) not in existed_files] 
nums = nums-len(existed_files)
for i in range(nums):
    shutil.copy(need_file[i], os.path.join(output_root, os.path.basename(need_file[i])))
