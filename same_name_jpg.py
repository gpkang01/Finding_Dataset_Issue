import os
import csv

def make_jpg_csv():
    # jpg 관련 파일이 들어있는 일자별 폴더 경로 입력
    parent_path = 'F:/'
    # 관련 py 및 csv 파일이 들어있는 폴더 경로 입력
    original_path = 'F:/same_jpg_space_json'
    print('JPG 중복 리스트를 추출 중입니다.\n시간이 다소 소요될 수 있습니다.')

    # jpg 폴더 및 파일 에서 총 파일수 
    jpg_date = ['210907', '210908', '210914', '210928', '211005', '211012', '211019', '211026',\
                '211102', '211110', '211116', '211123', '211130', '211203']
    class_file_count = 0
    class_file_lst = []
    class_path_file_lst = []

    for date in jpg_date:
        if os.path.isdir('{}{}'.format(parent_path, date)):
            jpg_dir = os.listdir('{}{}'.format(parent_path, date))
        for dlst in jpg_dir:
            if os.path.isdir('{}{}/{}'.format(parent_path, date, dlst)):
                jpg_file = os.listdir('{}{}/{}'.format(parent_path, date, dlst))
                class_file_count += len(jpg_file)
                for flst in jpg_file:
                    class_file_lst.append(flst)
                    class_path_file_lst.append(['{}{}/{}'.format(parent_path, date, dlst), flst])
    #     print(len(class_file_lst))
    # print(len(class_file_lst), len(class_path_file_lst), len(set(class_file_lst)))

    set_class_file_lst = sorted(list(set(class_file_lst)))

    # jpg 폴더 및 파일 에서 중복 파일 리스트
    count = 0
    f = open('{}/same_name_jpg.csv'.format(original_path), 'w', encoding = 'CP949', newline = '')
    f_field_name = ['파일 경로', '파일 이름']
    f_writer = csv.DictWriter(f, fieldnames = f_field_name)
    f_writer.writeheader()
    for slst in set_class_file_lst:
        index_lst = []
        count += 1
        print(count)
        x = class_file_lst.count(slst)
        if x > 1:
            for i in range(x):
                index = class_file_lst.index(slst)
                index_lst.append(index)
                class_file_lst.remove(slst)
            for j in index_lst:
                line_dict = {'파일 경로' : class_path_file_lst[j][0], '파일 이름' : class_path_file_lst[j][1]}
                class_path_file_lst.remove(class_path_file_lst[j])
                f_writer.writerow(line_dict)
    f.close()

    # jpg 중복 파일 수
    # set_count = 0
    # file_count = 0

    # for slst in set_class_file_lst:
    #     index_lst = []
    #     set_count += 1
    #     print(set_count)
    #     x = class_file_lst.count(slst)
    #     if x > 1:
    #         for i in range(x):
    #             file_count += 1
    # print(file_count)