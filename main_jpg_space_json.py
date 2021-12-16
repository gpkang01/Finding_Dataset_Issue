import os
import csv
from same_jpg_class_ins import make_final_jpg_csv
from same_json_class_ins import make_final_json_csv

# 관련 py 및 csv 파일이 들어있는 폴더 경로 입력
original_path = 'F:/same_jpg_space_json'

# read space image list
# 허공이미지 리스트에서 인스턴스 리스트 추출
print('허공이미지 리스트에서 인스턴스 리스트를 추출 중입니다.')
space_img_lst = []
f = open('{}/space_image.csv'.format(original_path), 'r', encoding = 'CP949')
f_field_name = ['허공이미지']
change_line = csv.DictReader(f, fieldnames = f_field_name)
for line in change_line:
    if line['허공이미지'] == '허공이미지':
        continue
    else:
        space_cls_ins = '{}_{}'.format(line['허공이미지'].strip().split('_')[0], line['허공이미지'].strip().split('_')[1])
        space_img_lst.append(space_cls_ins)
        
set_space_img_lst = sorted(set(space_img_lst))
print(len(space_img_lst), len(set_space_img_lst))

# read same image file
if not os.path.isfile('{}/same_jpg_class_ins.csv'.format(original_path)):
    make_final_jpg_csv()
print('중복이미지 리스트에서 인스턴스 리스트를 추출 중입니다.')
same_img_lst = []
f = open('{}/same_jpg_class_ins.csv'.format(original_path), 'r', encoding = 'CP949')
f_field_name = ['작업 경로', '이전 파일명', '변경 파일명', '참고 사항']
change_line = csv.DictReader(f, fieldnames = f_field_name)
for line in change_line:
    if line['이전 파일명'] == '이전 파일명':
        continue
    else:
        same_img_lst.append([line['작업 경로'], line['이전 파일명'], line['변경 파일명'], line['참고 사항'],\
                            '{}_{}'.format(line['이전 파일명'].strip().split('_')[0], line['이전 파일명'].strip().split('_')[1])])

# read same json file
same_json_lst = []
same_json_name_lst = []
if not os.path.isfile('{}/same_json_class_ins.csv'.format(original_path)):
    make_final_json_csv()
print('중복 JSON 리스트에서 인스턴스 리스트를 추출 중입니다.')
f = open('{}/same_json_class_ins.csv'.format(original_path), 'r', encoding = 'CP949')
f_field_name = ['파일 경로', '파일 이름']
change_line = csv.DictReader(f, fieldnames = f_field_name)
for line in change_line:
    if line['파일 경로'] == '파일 경로':
        continue
    else:
        same_json_name_lst.append(line['파일 이름'].strip().split('.')[0])
        same_json_lst.append([line['파일 경로'], line['파일 이름']])

print('추출된 데이타를 통합 작성 중입니다.')
# 중복 이미지와 허공 이미지 겹치는 list
same_img_space_lst = []
for ilst in same_img_lst:
    if ilst[4] in set_space_img_lst:
        if not ilst[2]:
            same_img_space_lst.append([ilst[0], ilst[1], ilst[2], ilst[3], ''])
        else:
            same_img_space_lst.append([ilst[0], ilst[1], ilst[2], ilst[3], '존재'])
    else:
        same_img_space_lst.append([ilst[0], ilst[1], ilst[2], ilst[3], ''])
        
# 중복 이미지와 중복 json 겹치는 list
same_img_space_json_lst = []
count = 0
for islst in same_img_space_lst:
    exist = ''
    change_json_name = ''
    count += 1
    if islst[2]:
        change_json_name = '{}.json'.format(islst[2].strip().split('.')[0])
    if islst[1].strip().split('.')[0] in same_json_name_lst:
        index = same_json_name_lst.index(islst[1].strip().split('.')[0])
        same_img_space_json_lst.append([islst[0], islst[1], islst[2], islst[3], islst[4],\
                                       same_json_lst[index][0], same_json_lst[index][1], change_json_name])
        same_json_name_lst.remove(same_json_name_lst[index])
        same_json_lst.remove(same_json_lst[index])
    else:
        same_img_space_json_lst.append([islst[0], islst[1], islst[2], islst[3], islst[4], '경로 없음', '파일 없음', '없음'])
    print(count)

f = open('{}/main_jpg_space_json.csv'.format(original_path), 'w', encoding = 'CP949', newline = '')
f_field_name = ['이미지 경로', '이전 파일명', '변경 파일명', '참고 사항', '허공 이미지', 'JSON 경로', '이전 JSON명', '변경 JSON명']
f_writer = csv.DictWriter(f, fieldnames = f_field_name)
f_writer.writeheader()
for lst in same_img_space_json_lst:
    line = {'이미지 경로' : lst[0], '이전 파일명' : lst[1], '변경 파일명' : lst[2], '참고 사항' : lst[3],\
            '허공 이미지' : lst[4], 'JSON 경로' : lst[5], '이전 JSON명' : lst[6], '변경 JSON명' : lst[7]}
    f_writer.writerow(line)
f.close()