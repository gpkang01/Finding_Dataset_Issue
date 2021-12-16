import os
import csv
from same_name_json import make_json_csv

def make_final_json_csv():
    tot_file_lst = []
    tot_file_name_lst = []
    class_lst = []
    tot_same_instance_lst = []
    # 관련 py 및 csv 파일이 들어있는 폴더 경로 입력
    original_path = 'F:/same_jpg_space_json'

    # class name list
    with open('{}/class_list.txt'.format(original_path), 'rt', encoding = 'utf-8') as file:
        while True:
            tmp_line1 = file.readline().strip()
            if not tmp_line1:
                break
            class_name = tmp_line1.split('|')[1]
            class_lst.append(class_name)

    # make a sole file list
    wrong_class_name = []
    if not os.path.isfile('{}/same_name_json.csv'.format(original_path)):
        make_json_csv()
    print('JSON 중복 리스트를 작성 중입니다.')
    f = open('{}/same_name_json.csv'.format(original_path), 'r', encoding = 'CP949')
    f_field_name = ['파일 경로', '파일 이름']
    change_line = csv.DictReader(f, fieldnames = f_field_name)
    for line in change_line:
        if line['파일 경로'] == '파일 경로':
            continue
        else:
            parent_path = line['파일 경로']
            file_name = line['파일 이름']
            class_name = file_name.split('_')[0]
            ins_num = file_name.split('_')[1]
            if class_name not in class_lst:
                wrong_class_name.append([parent_path, file_name])
            tot_file_name_lst.append('{}_{}'.format(class_name, ins_num))
            tot_file_lst.append([parent_path, file_name, '{}_{}'.format(class_name, ins_num)])

    if len(wrong_class_name) > 0:
        print('잘못된 클래스명 {}이 존재합니다.\n확인 후 진행해 주세요.'.format(wrong_class_name))
        quit()
    else:
        unique_file_name_lst = sorted(set(tot_file_name_lst))
        sort_tot_file_lst = sorted(tot_file_lst)
        print(len(unique_file_name_lst), len(sort_tot_file_lst))
        print(sort_tot_file_lst)

        for x in unique_file_name_lst:
            count = 0
            same_instance_lst = []
            for flst in sort_tot_file_lst:
                if flst[2] == x:
                    count += 1
                    if count <= 20:
                        same_instance_lst.append(flst)
                    elif count == 21:
                        for ilst in same_instance_lst:
                            tot_same_instance_lst.append(ilst)
                        tot_same_instance_lst.append(flst)
                    else:
                        tot_same_instance_lst.append(flst)

        f = open('{}/same_json_class_ins.csv'.format(original_path), 'w', encoding = 'CP949', newline = '')
        f_field_name = ['파일 경로', '파일 이름']
        f_writer = csv.DictWriter(f, fieldnames = f_field_name)
        f_writer.writeheader()
        for lst in tot_same_instance_lst:
            line = {'파일 경로' : lst[0], '파일 이름' : lst[1]}
            f_writer.writerow(line)
        f.close()