import json 
from multiprocessing import Pool 
import os 


def save_jsonl(data, file_path):
    jsonl = [] 
    for di in data:
        j = json.dumps(di, ensure_ascii=False) 
        jsonl.append(j)
    f = open(file_path, 'w', encoding='utf-8')
    f.write('\n'.join(jsonl))
    f.close()
    print("{} written. Path: {}".format(len(jsonl), file_path)) 

def process(file, save_root):
    file_name = os.path.basename(file)
    new_file = os.path.join(save_root, file_name)
    if os.path.exists(new_file):
        print("file {} is exsisted and will be skipped".format(new_file))
        return 
    f = open(file,encoding='utf-8')
    data = json.load(f)
    f.close() 
    data_new = {"RECORDS": data} 
    f = open(new_file, 'w', encoding='utf-8')
    f.write(json.dumps(data_new))
    f.close() 
    print("{} written. Path: {}".format(len(data), new_file))

if __name__ == "__main__":
    data_root = "/dataset/fd5061f6/chinese_data/WuDao"
    #save_root = "/dataset/fd5061f6/chinese_data/WuDao_processed"
    save_root="./WuDao_processed"
    os.makedirs(save_root, exist_ok=True)
    fs = os.listdir(data_root) 
    fs = [os.path.join(data_root, i) for i in fs] 
    p = Pool(1) 
    for file in fs:
        p.apply_async(process, args = (file, save_root))
    p.close() 
    p.join()
    print('All is ok')
