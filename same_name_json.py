import os
import shutil
import csv

# JSON 관련 파일이 들어있는 일자별 폴더 경로 입력
json_path = 'F:/label'
# 관련 py 및 csv 파일이 들어있는 폴더 경로 입력
original_path = 'F:/same_jpg_space_json'

def correct_json():
    # class name 가져오기
    class_lst = []
    with open('{}/class_list.txt'.format(original_path), 'rt', encoding = 'utf-8') as file:
        while True:
            tmp_line = file.readline().strip()
            if not tmp_line:
                break
            class_name = tmp_line.split('|')[1]
            class_lst.append(class_name)

    file_name_lst = []
    file_path_lst = []
    wrong_class_paths_name = []
    wrong_class_paths_path = []
    Wrong_class_name = ['cigarettes', 'CoffeeMug', 'Dishsoap', 'Electric_Switch', 'FrenchLoaf', 'HairBrush',\
                        'MicroPhone', 'Mobilephone', 'Pencilcase', 'Pennybank', 'ScrewDriver', 'Stepler', 'SweatShirt',\
                        'ToolKit', 'T-Shirt', 'Wineglass']
    change_class_name = ['Cigarettes', 'Mug', 'DishSoap', 'ElectricSwitch', 'Loaf', 'HairBrushComb',\
                        'Microphone', 'MobilePhone', 'PencilCase', 'PennyBank', 'Screwdriver', 'Stapler', 'Sweatshirt',\
                        'Toolkit', 'T-shirt', 'WineGlass']

    # 1. json 폴더 및 파일에서 잘못된 클래스명 찾기 
    #    - 찾은 클래스명이 Wrong_class_name과 change_class_name 에 없으면 추가
    json_date = ['210917', '211022', '211104', '211115', '211119', '211125', '211201', '211205', '211208', '211214']
    wrong_class_dir = []
    wrong_class_file = []
    print('json 폴더 및 파일에서 잘못된 클래스명을 찾고 있습니다.')
    for date in json_date:
        json_dir = os.listdir('{}/{}/polygon'.format(json_path, date))
        for dlst in json_dir:
            if dlst not in class_lst:
                wrong_class_dir.append('{}_{}'.format(date, dlst))
            json_file = os.listdir('{}/{}/polygon/{}'.format(json_path, date, dlst))
            for flst in json_file:
                if flst.strip().split('_')[0] not in class_lst:
                    wrong_class_file.append('{}_{}'.format(date, flst.strip().split('_')[0]))
                    if flst.strip().split('_')[0] == 'Electric':
                        wrong_class_file.append('{}_{}'.format(date, flst))

    print(list(set(wrong_class_dir)), list(set(wrong_class_file)))

    # 2. json 폴더 및 파일에서 잘못된 클래스명 변경 
    #    - len(same_class_file)이 '0'보다 크면 폴더 안에 같은 클래스명의 폴더가 이미 존재
    go_no = 0
    if len(wrong_class_dir) == 0 and len(wrong_class_file) == 0:
        print('json 폴더 및 파일에서 잘못된 클래스명을 수정 중입니다.')
        json_date = ['210917', '211022', '211104', '211115', '211119', '211125', '211201', '211205', '211208', '211214']
        same_class_file = []
        for date in json_date:
            json_dir = os.listdir('{}/{}/polygon'.format(json_path, date))
            for dlst in json_dir:
                json_file = os.listdir('{}/{}/polygon/{}'.format(json_path, date, dlst))
                for flst in json_file:
                    if flst.strip().split('_')[0] in Wrong_class_name:
                        class_nm = change_class_name[Wrong_class_name.index(flst.strip().split('_')[0])]
                        os.rename('{}/{}/polygon/{}/{}'.format(json_path, date, dlst, flst), '{}/{}/polygon/{}/{}_{}_{}_{}'\
                                .format(json_path, date, dlst, class_nm, flst.strip().split('_')[1], flst.strip().split('_')[2], flst.strip().split('_')[3]))
                    if 'Electric_Switch' in flst:
                        os.rename('{}/{}/polygon/{}/{}'.format(json_path, date, dlst, flst), '{}/{}/polygon/{}/{}_{}_{}_{}'\
                                .format(json_path, date, dlst, 'ElectricSwitch', flst.strip().split('_')[2], flst.strip().split('_')[3], flst.strip().split('_')[4]))
                if dlst == 'Humidifier':
                        shutil.rmtree('{}/{}/polygon/{}'.format(json_path, date, dlst))
                if dlst in Wrong_class_name:
                    class_nm = change_class_name[Wrong_class_name.index(dlst)]
                    if class_nm in json_dir:
                        class_file_nm = os.listdir('{}/{}/polygon/{}'.format(json_path, date, dlst))
                        for nm in class_file_nm:
                            if os.path.isfile('{}/{}/polygon/{}/{}'.format(json_path, date, class_nm, nm)):
                                same_class_file.append(['{}/{}/polygon/{}'.format(json_path, date, dlst), nm])
                                print('{}에서 이동시킬 {}/{}/polygon/{}에 {} 파일명이 존재합니다.\n\
{}/same_classname_json.csv에서 확인 후 조치해 주세요.'.format(dlst, json_path, date, class_nm, nm, original_path))
                                go_no = 1
                            else:
                                shutil.move('{}/{}/polygon/{}/{}'.format(json_path, date, dlst, nm),\
                                            '{}/{}/polygon/{}/{}'.format(json_path, date, class_nm, nm))

                        class_file_nm1 = os.listdir('{}/{}/polygon/{}'.format(json_path, date, dlst))
                        if len(class_file_nm1) == 0:
                            shutil.rmtree('{}/{}/polygon/{}'.format(json_path, date, dlst))
                    else:
                        os.rename('{}/{}/polygon/{}'.format(json_path, date, dlst),\
                                  '{}/{}/polygon/{}'.format(json_path, date, class_nm))
        if len(same_class_file) > 0:
            f = open('{}/same_classname_json.csv'.format(original_path), 'w', encoding = 'CP949', newline = '')
            f_field_name = ['파일 경로', '파일 이름']
            f_writer = csv.DictWriter(f, fieldnames = f_field_name)
            f_writer.writeheader()
            for line in same_class_file:
                line_dict = {'파일 경로' : line[0], '파일 이름' : line[1]}
                f_writer.writerow(line_dict)
            f.close()
    else:
        print('등록되지 않은 잘못된 JSON 폴더명이나 파일명이 존재합니다. 등록 후 다시 진행해 주세요.')
        go_no = 1
    return go_no

def make_json_csv():
    go_no = correct_json()
    if go_no == 0:
        print('JSON 중복 리스트를 추출 중입니다.\n시간이 다소 소요될 수 있습니다.')
        # json 폴더 및 파일 에서 총 파일수 
        json_date = ['210917', '211022', '211104', '211115', '211119', '211125', '211201', '211205', '211208', '211214']
        class_file_count = 0
        class_file_lst = []
        class_path_file_lst = []

        for date in json_date:
            json_dir = os.listdir('{}/{}/polygon'.format(json_path, date))
            for dlst in json_dir:
                json_file = os.listdir('{}/{}/polygon/{}'.format(json_path, date, dlst))
                class_file_count += len(json_file)
                for flst in json_file:
                    class_file_lst.append(flst)
                    class_path_file_lst.append(['{}/{}/polygon/{}'.format(json_path, date, dlst), flst])
        #     print(len(class_file_lst))
        # print(len(class_file_lst), len(class_path_file_lst), len(set(class_file_lst)))

        set_class_file_lst = sorted(list(set(class_file_lst)))

        # json 폴더 및 파일 에서 중복 파일 리스트
        count = 0
        f = open('{}same_name_json.csv'.format(original_path), 'w', encoding = 'CP949', newline = '')
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
    else:
        quit()

    # json 중복 파일 수
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

    # # original_paths.txt 에서 잘못된 클래스명 찾기
    # with open('{}label/new_original_paths.txt'.format(original_path), 'r') as file:
    #     while True:
    #         tmp_line = file.readline().strip()
    #         if not tmp_line:
    #             break
    #         # tmp_line = tmp_line.replace('.jpg', '.jpg|')
    #         file_name = tmp_line.split('|')[0].strip()
    #         file_path = tmp_line.split('|')[1].strip()
    #         file_name_lst.append(file_name)
    #         file_path_lst.append(file_path)
    #         if file_name.strip().split('/')[0] not in class_lst:
    #             wrong_class_paths_name.append(file_name.strip().split('/')[0])
    #         if file_path.strip().split('/')[1] not in class_lst:
    #             wrong_class_paths_path.append(file_path.strip().split('/')[1])

    # print(list(set(wrong_class_paths_name)), list(set(wrong_class_paths_path)))

    # original_paths.txt 에서 잘못된 클래스명 변경
    # new_line_lst = []
    # with open('{}label/original_paths.txt'.format(original_path), 'r') as file:
    #     while True:
    #         tmp_line = file.readline().strip()
    #         if not tmp_line:
    #             break
    #         tmp_line = tmp_line.replace('.jpg', '.jpg|')
    #         file_name = tmp_line.split('|')[0].strip()
    #         file_path = tmp_line.split('|')[1].strip()
    #         file_name_lst.append(file_name)
    #         file_path_lst.append(file_path)
    #         if file_name.strip().split('/')[0] in Wrong_class_name:
    #             tmp_line = tmp_line.replace(file_name.strip().split('/')[0], \
    #                        change_class_name[Wrong_class_name.index(file_name.strip().split('/')[0])])
    #         if file_name.strip().split('/')[0] == 'Humidifier':
    #             continue
    #         else:
    #             new_line_lst.append(tmp_line)

    # with open('{}label/new_original_paths.txt'.format(original_path), 'w') as file:
    #     for lst in new_line_lst:
    #         file.writelines('{}\n'.format(lst))