import os
import csv
from same_name_jpg import make_jpg_csv

def make_final_jpg_csv():
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
    if not os.path.isfile('{}/same_name_jpg.csv'.format(original_path)):
        make_jpg_csv()
    print('JPG 중복 리스트를 작성 중입니다.')
    wrong_class_name = []
    f = open('{}/same_name_jpg.csv'.format(original_path), 'r', encoding = 'CP949')
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

        print(len(tot_same_instance_lst))

        same_class_name = ''
        same_class_lst = []
        for y in tot_same_instance_lst:
            if same_class_name == '':
                same_class_name = y[2].split('_')[0]
                same_instance_name = y[2]
                count = 0
                ins_count = 1
                changed_name = ''
                y.append(changed_name)
                same_class_lst.append(y)
            elif same_class_name == y[2].split('_')[0]:
                if same_instance_name == y[2]:
                    count += 1
                    ins_count += 1
                    if ins_count <= 20:
                        changed_name = ''
                    else:
                        ins_num = 300 + (count // 20)
                        str_count = str('{0:03d}'.format(ins_num))
                        changed_name = '{}_{}_{}_{}'.format(y[1].split('_')[0], str_count, y[1].split('_')[2], y[1].split('_')[3])
                    y.append(changed_name)
                    same_class_lst.append(y)
                elif same_instance_name != y[2]:
                    same_instance_name = y[2]
                    count -= 19
                    ins_count = 1
                    changed_name = ''
                    y.append(changed_name)
                    same_class_lst.append(y)
            elif same_class_name != y[2].split('_')[0]:
                same_class_name = y[2].split('_')[0]
                same_instance_name = y[2]
                count = 0
                ins_count = 1
                changed_name = ''
                y.append(changed_name)
                same_class_lst.append(y)

        print(len(same_class_lst))

        f = open('{}/same_jpg_class_ins.csv'.format(original_path), 'w', encoding = 'CP949', newline = '')
        f_field_name = ['작업 경로', '이전 파일명', '변경 파일명']
        f_writer = csv.DictWriter(f, fieldnames = f_field_name)
        f_writer.writeheader()
        for i in range(len(same_class_lst)):
            report = {'작업 경로' : same_class_lst[i][0], '이전 파일명' : same_class_lst[i][1], '변경 파일명' : same_class_lst[i][3]}
            f_writer.writerow(report)
        f.close()