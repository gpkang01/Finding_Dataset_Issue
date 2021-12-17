from __future__ import print_function
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import os
import tkinter.messagebox as msgbox
import os.path
import time
import shutil
import csv

class frameInit:
    def __init__(self):
        self.root = Tk()
        self.root.title("파일명/폴더명 에러 수정 및 최종 분류")
        self.root.geometry('415x440+500+150') 
        self.root.resizable(False, False) 
        
        self.current_path = os.getcwd()

        # select work folder frame
        sele_folder_frame = LabelFrame(self.root, text = '작업 폴더 선택')
        sele_folder_frame.pack(side = 'top', fill = 'both', pady = 8)

        # select jpg work folder button frame
        sele_folder_top1 = Frame(sele_folder_frame)
        sele_folder_top1.pack(side = 'top', fill = 'both')

        sele_folder1 = Label(sele_folder_top1, text = '다운받은 JPG 폴더들이 들어있는 상위 폴더를 선택하세요.')
        sele_folder1.pack(side = 'left', fill = 'x', padx = 5)

        self.sele_folder1 = Button(sele_folder_top1, text = '열기', width = 8, command = self.jpg_open_dir)
        self.sele_folder1.pack(side = 'right', fill = 'x', padx = 5)
        
        # select jpg work folder Entry frame
        sele_folder_top3 = Frame(sele_folder_frame)
        sele_folder_top3.pack(side = 'top', fill = 'both')

        self.sele_folder3 = Entry(sele_folder_top3, width = 57)
        self.sele_folder3.pack(side = 'left', fill = 'x', padx = 5, pady = 5)
        
        # select json work folder button frame
        sele_folder_top2 = Frame(sele_folder_frame)
        sele_folder_top2.pack(side = 'top', fill = 'both')
        
        sele_folder2 = Label(sele_folder_top2, text = '다운받은 JSON 폴더들이 들어있는 상위 폴더를 선택하세요.')
        sele_folder2.pack(side = 'left', fill = 'x', padx = 5)

        self.sele_folder2 = Button(sele_folder_top2, text = '열기', width = 8, command = self.json_open_dir)
        self.sele_folder2.pack(side = 'right', fill = 'x', padx = 5)
        
        # select json work folder Entry frame
        sele_folder_top4 = Frame(sele_folder_frame)
        sele_folder_top4.pack(side = 'top', fill = 'both')

        self.sele_folder4 = Entry(sele_folder_top4, width = 57)
        self.sele_folder4.pack(side = 'left', fill = 'x', padx = 5, pady = 5)

        # select save folder frame
        save_folder_frame = LabelFrame(self.root, text = '저장 폴더 선택')
        save_folder_frame.pack(side = 'top', fill = 'both', pady = 8)
        
        # select jpg save folder button frame
        save_folder_top1 = Frame(save_folder_frame)
        save_folder_top1.pack(side = 'top', fill = 'both')

        save_folder1 = Label(save_folder_top1, text = 'JPG 파일을 저장할 폴더를 선택하세요.')
        save_folder1.pack(side = 'left', fill = 'x', padx = 5)

        self.save_folder1 = Button(save_folder_top1, text = '열기', width = 8, command = self.jpg_save_dir)
        self.save_folder1.pack(side = 'right', fill = 'x', padx = 5)

        # select jpg save folder Entry frame
        save_folder_top2 = Frame(save_folder_frame)
        save_folder_top2.pack(side = 'top', fill = 'both')

        self.save_folder2 = Entry(save_folder_top2, width = 57)
        self.save_folder2.pack(side = 'left', fill = 'x', padx = 5, pady = 5)
        
        # select json save folder button frame
        save_folder_top3 = Frame(save_folder_frame)
        save_folder_top3.pack(side = 'top', fill = 'both')

        save_folder3 = Label(save_folder_top3, text = 'JSON 파일을 저장할 폴더를 선택하세요.')
        save_folder3.pack(side = 'left', fill = 'x', padx = 5)

        self.save_folder3 = Button(save_folder_top3, text = '열기', width = 8, command = self.json_save_dir)
        self.save_folder3.pack(side = 'right', fill = 'x', padx = 5)

        # select save folder Entry frame
        save_folder_top4 = Frame(save_folder_frame)
        save_folder_top4.pack(side = 'top', fill = 'both')

        self.save_folder4 = Entry(save_folder_top4, width = 57)
        self.save_folder4.pack(side = 'left', fill = 'x', padx = 5, pady = 5)

        # final saving button frame
        save_folder_btn = Frame(self.root)
        save_folder_btn.pack(side = 'top', fill = 'both')

        self.save_btn = Button(save_folder_btn, text = '작업 시작', width = 15, command = self.save, state = 'disabled')
        self.save_btn.pack(side = 'right', fill = 'x', padx = 5)

        # save status frame
        save_status_frame = LabelFrame(self.root, text = '작업 현황')
        save_status_frame.pack(fill = 'both', pady = 8)

        # progressbar
        save_status_top1 = Frame(save_status_frame)
        save_status_top1.pack(side = 'top', fill = 'both')
        
        self.pro_var = DoubleVar()
        self.progressbar = ttk.Progressbar(save_status_top1, maximum =100, length = 400, variable = self.pro_var)
        self.progressbar.pack(side = 'top', padx =5, pady = 5)

        self.prog_rate1 = Label(save_status_top1, text = 'JPG 폴더 열기 하면 파일 Count로 시간 소요되니 잠시 기다려 주세요.')
        self.prog_rate1.pack(side = 'top', fill = 'x', padx = 5, pady = 5)
        
        self.prog_rate2 = Label(save_status_top1, text = 'JSON 폴더 열기 하면 파일 Count로 시간 소요되니 잠시 기다려 주세요.')
        self.prog_rate2.pack(side = 'top', fill = 'x', padx = 5, pady = 5)
        
        self.jpg_save_path = ''
        self.json_save_path = ''
        self.tot_open = 0
        self.root.mainloop()
        
    def jpg_open_dir(self):
        self.jpg_open_path = filedialog.askdirectory(title = '작업 폴더 열기', initialdir = self.current_path)
        self.sele_folder3.configure(state = 'normal')
        self.sele_folder3.delete(0, END)
        self.sele_folder3.insert(0, self.jpg_open_path)
        self.sele_folder3.configure(state = 'readonly')
        self.save_btn.configure(state = 'disabled')
        self.pro_var.set(0)
        self.progressbar.update()
        self.prog_rate1.configure(text = '')
        
        self.original_list = ['210907', '210908', '210914', '210928', '211005', '211012', '211019', '211026',\
                              '211102', '211110', '211116', '211123', '211130', '211203', '210907_None', '210908_None',\
                              '210914_None', '210928_None', '211005_None', '211012_None', '211019_None', '211026_None',\
                              '211102_None', '211110_None', '211116_None', '211123_None', '211130_None', '211203_None']
        self.jpg_date_list = os.listdir(self.jpg_open_path)
        tot_file_qy = 0
        dele_lst = []
        for dlst in self.jpg_date_list:
            if dlst in self.original_list:
                if '_' in dlst:
                    continue
                else:
                    class_list = os.listdir('{}/{}'.format(self.jpg_open_path, dlst))
                    for clst in class_list:
                        if os.path.isdir('{}/{}/{}'.format(self.jpg_open_path, dlst, clst)):
                            open_file_list = os.listdir('{}/{}/{}'.format(self.jpg_open_path, dlst, clst))
                            cls_file_qy = len(open_file_list)
                            if cls_file_qy % 20 == 0:
                                tot_file_qy += cls_file_qy
                            else:
                                msgbox.showwarning('경고', '[{}/{}] 폴더 안의 파일 수가 맞지 않습니다.\n확인 후 다시 시작해 주세요.'\
                                    .format(dlst, clst))
                                self.root.quit()
            else:
                if os.path.isdir('{}/{}'.format(self.jpg_open_path, dlst)):
                    self.gono_check = msgbox.askyesno('예 / 아니오', '작업 폴더 안에 리스트에 없는 [{}] 폴더가 존재합니다.\n이 폴더를 \
포함하려면 [예], 포함하지 않으려면 [아니오]를 눌러주세요.'.format(dlst))
                    if self.gono_check:
                        if '_' in dlst:
                            continue
                        else:
                            class_list = os.listdir('{}/{}'.format(self.jpg_open_path, dlst))
                            for clst in class_list:
                                if os.path.isdir('{}/{}/{}'.format(self.jpg_open_path, dlst, clst)):
                                    open_file_list = os.listdir('{}/{}/{}'.format(self.jpg_open_path, dlst, clst))
                                    cls_file_qy = len(open_file_list)
                                    if cls_file_qy % 20 == 0:
                                        tot_file_qy += cls_file_qy
                                    else:
                                        msgbox.showwarning('경고', '[{}/{}] 폴더 안의 파일 수가 맞지 않습니다.\n확인 후 다시 시작해 주세요.'\
                                            .format(dlst, clst))
                                        self.root.quit()
                    else:
                        dele_lst.append(dlst)
                        continue
                
        for lst in dele_lst:
            if lst in self.jpg_date_list:
                self.jpg_date_list.remove(lst)
                
        self.prog_rate1.configure(text = '분류할 총 JPG 파일 수 : {:,}'.format(tot_file_qy))
        self.tot_open += 1
        if self.tot_open >= 4:
            self.save_btn.configure(state = 'normal')
        
    def json_open_dir(self):
        self.json_open_path = filedialog.askdirectory(title = '작업 폴더 열기', initialdir = self.current_path)
        self.sele_folder4.configure(state = 'normal')
        self.sele_folder4.delete(0, END)
        self.sele_folder4.insert(0, self.json_open_path)
        self.sele_folder4.configure(state = 'readonly')
        self.save_btn.configure(state = 'disabled')
        self.pro_var.set(0)
        self.progressbar.update()
        self.prog_rate2.configure(text = '')
        
        self.original_list = ['210917', '211022', '211104', '211115', '211119', '211125', '211201', '211205', '211208', '211214']
        self.json_date_list = os.listdir(self.json_open_path)
        tot_file_qy = 0
        dele_lst = []
        for dlst in self.json_date_list:
            if dlst in self.original_list:
                if '_' in dlst:
                    continue
                else:
                    class_list = os.listdir('{}/{}/polygon'.format(self.json_open_path, dlst))
                    for clst in class_list:
                        if os.path.isdir('{}/{}/polygon/{}'.format(self.json_open_path, dlst, clst)):
                            open_file_list = os.listdir('{}/{}/polygon/{}'.format(self.json_open_path, dlst, clst))
                            cls_file_qy = len(open_file_list)
                            tot_file_qy += cls_file_qy
                            # if cls_file_qy % 20 == 0:
                            #     tot_file_qy += cls_file_qy
                            # else:
                            #     msgbox.showwarning('경고', '[{}/{}] 폴더 안의 파일 수가 맞지 않습니다.\n확인 후 다시 시작해 주세요.'\
                            #         .format(dlst, clst))
                            #     self.root.quit()
            else:
                if os.path.isdir('{}/{}/polygon'.format(self.json_open_path, dlst)):
                    self.gono_check = msgbox.askyesno('예 / 아니오', '작업 폴더 안에 리스트에 없는 [{}] 폴더가 존재합니다.\n이 폴더를 \
포함하려면 [예], 포함하지 않으려면 [아니오]를 눌러주세요.'.format(dlst))
                    if self.gono_check:
                        if '_' in dlst:
                            continue
                        else:
                            class_list = os.listdir('{}/{}/polygon'.format(self.json_open_path, dlst))
                            for clst in class_list:
                                if os.path.isdir('{}/{}/polygon/{}'.format(self.json_open_path, dlst, clst)):
                                    open_file_list = os.listdir('{}/{}/polygon/{}'.format(self.json_open_path, dlst, clst))
                                    cls_file_qy = len(open_file_list)
                                    tot_file_qy += cls_file_qy
                                    # if cls_file_qy % 20 == 0:
                                    #     tot_file_qy += cls_file_qy
                                    # else:
                                    #     msgbox.showwarning('경고', '[{}/{}] 폴더 안의 파일 수가 맞지 않습니다.\n확인 후 다시 시작해 주세요.'\
                                    #         .format(dlst, clst))
                                    #     self.root.quit()
                    else:
                        dele_lst.append(dlst)
                        continue
                
        for lst in dele_lst:
            if lst in self.json_date_list:
                self.json_date_list.remove(lst)
                
        self.prog_rate2.configure(text = '분류할 총 JSON 파일 수 : {:,}'.format(tot_file_qy))
        self.tot_open += 1
        if self.tot_open >= 4:
            self.save_btn.configure(state = 'normal')
        
    def jpg_save_dir(self):
        self.jpg_save_path = filedialog.askdirectory(title = '저장 폴더 열기', initialdir = self.current_path)
        if self.jpg_save_path:
            self.save_folder2.configure(state = 'normal')
            self.save_folder2.delete(0, END)
            self.save_folder2.insert(0, self.jpg_save_path)
            self.save_folder2.configure(state = 'readonly')
        else:
            msgbox.showwarning('경고', '저장 폴더를 선택하지 않으셨습니다.')
        self.tot_open += 1
        if self.tot_open >= 4:
            self.save_btn.configure(state = 'normal')

    def json_save_dir(self):
        self.json_save_path = filedialog.askdirectory(title = '저장 폴더 열기', initialdir = self.current_path)
        if self.json_save_path:
            self.save_folder4.configure(state = 'normal')
            self.save_folder4.delete(0, END)
            self.save_folder4.insert(0, self.json_save_path)
            self.save_folder4.configure(state = 'readonly')
        else:
            msgbox.showwarning('경고', '저장 폴더를 선택하지 않으셨습니다.')
        self.tot_open += 1
        if self.tot_open >= 4:
            self.save_btn.configure(state = 'normal')

    def save(self):
        self.save_btn.configure(state = 'disabled')
        self.sele_folder1.configure(state = 'disabled')
        self.sele_folder2.configure(state = 'disabled')
        self.save_folder1.configure(state = 'disabled')
        self.save_folder3.configure(state = 'disabled')
        self.work_ok = 0
        # self.jpg_delete_class()
        # if self.work_ok == 0:
        #     self.jpg_change_class()
        # else:
        #     self.root.quit()
        # if self.work_ok == 0:
        #     self.jpg_change_name()
        # else:
        #     self.root.quit()
        # if self.work_ok == 0:
        #     self.json_change_name()
        # else:
        #     self.root.quit()
        # if self.work_ok == 0:
        #     self.jpg_classify_file()
        # else:
        #     self.root.quit()
        # if self.work_ok == 0:
        #     self.json_classify_file()
        # else:
        #     self.root.quit()
        if self.work_ok == 0:
            self.prog_rate1.configure(text = '작업 완료')
            self.sele_folder1.configure(state = 'normal')
            self.sele_folder2.configure(state = 'normal')
            self.save_folder1.configure(state = 'normal')
            self.save_folder3.configure(state = 'normal')
        else:
            self.root.quit()
            
    def progress(self, current_qy, total_qy, title):
        self.current_qy = current_qy + 1
        self.total_qy = total_qy
        i = (self.current_qy / self.total_qy) * 100

        self.pro_var.set(i)
        self.progressbar.update()

        state = '{} : {} / {}'.format(title, self.current_qy, self.total_qy)
        self.prog_rate1.configure(text = state)
        self.prog_rate2.configure(text = '')
           
    def jpg_delete_class(self):
        try:
            self.filename_path = 'filename_error'
            del_data = []
            f = open('{}/1_delete_Humidifier.csv'.format(self.filename_path), 'r', encoding = 'CP949')
            f_field_name = ['No.', '작업 경로', '저장 경로', '이전 파일명']
            delete_line = csv.DictReader(f, fieldnames = f_field_name)
            for line in delete_line:
                if len(line['저장 경로'].strip().split('/')) == 1:
                    continue
                del_data.append([line['저장 경로'].strip().split('/')[1], line['저장 경로'].strip().split('/')[2]])

            # delete class folder in delete list
            line_qy = len(del_data)
            cur_qy = 0
            target_list = []
            for data in del_data:
                if os.path.isdir('{}/{}/{}'.format(self.json_open_path, data[0], data[1])):
                    shutil.rmtree('{}/{}/{}'.format(self.json_open_path, data[0], data[1]))
                target_list.append('{}/{}/{}'.format(self.json_open_path, data[0], data[1]))
                cur_qy += 1
                self.progress(cur_qy, line_qy, '미사용 클래스 삭제')
            self.save_log(target_list, '1_del')
        except:
            msgbox.showwarning('경고', '작업이 완료되지 않았습니다. 처음부터 다시 진행해 주세요. 1')
            self.work_ok = 1
        
    def jpg_change_class(self):
        try:
            change_data = []
            f = open('{}/2_wrong_class_name.csv'.format(self.filename_path), 'r', encoding = 'CP949')
            f_field_name = ['No.', '저장 경로', '이전 파일명', '변경 파일명', '참고 사항']
            change_line = csv.DictReader(f, fieldnames = f_field_name)
            for line in change_line:
                if len(line['저장 경로'].strip().split('/')) == 1:
                    continue
                
                change_data.append([line['저장 경로'].strip().split('/')[1], line['저장 경로'].strip().split('/')[2],\
                                    line['이전 파일명'], line['변경 파일명']])

            cur_cls_name = ''
            wrong_cls_name = ['Mobilephone', 'ScrewDriver', 'Wineglass']
            new_cls_name = ['MobilePhone', 'Screwdriver', 'WineGlass']
            # rename class folder/file in change list
            line_qy = len(change_data)
            cur_qy = 0
            target_list = []
            for data in change_data:
                if cur_cls_name == '':
                    cur_date = data[0]
                    cur_cls_name = data[1]
                    if cur_cls_name in wrong_cls_name:
                        change_cls_name = new_cls_name[wrong_cls_name.index(cur_cls_name)]
                        if os.path.isdir('{}/{}/{}'.format(self.jpg_open_path, data[0], data[1])):
                            os.rename('{}/{}/{}'.format(self.jpg_open_path, data[0], data[1]),\
                                    '{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name))
                            target_list.append('{}/{}/{}|{}/{}/{}'.format(self.jpg_open_path, data[0], data[1], self.jpg_open_path,\
                                                data[0], change_cls_name))
                        if os.path.isfile('{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2])):
                            os.rename('{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2]),\
                                    '{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[3]))
                            target_list.append('{}/{}/{}/{}|{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2],\
                                                self.jpg_open_path, data[0], change_cls_name, data[3]))
                        # else:
                        #     msgbox.showwarning('경고', '변경할 {}/{}/{}/{} 파일이 없습니다. 확인이 필요합니다.'\
                        #         .format(self.jpg_open_path, data[0], change_cls_name, data[2]))
                elif cur_date == data[0] and cur_cls_name == data[1]:
                    if os.path.isfile('{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2])):
                        os.rename('{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2]),\
                                  '{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[3]))
                        target_list.append('{}/{}/{}/{}|{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2],\
                                            self.jpg_open_path, data[0], change_cls_name, data[3]))
                    # else:
                    #     msgbox.showwarning('경고', '변경할 {}/{}/{}/{} 파일이 없습니다. 확인이 필요합니다.'\
                    #         .format(self.jpg_open_path, data[0], change_cls_name, data[2]))
                elif cur_date != data[0] and cur_cls_name == data[1]:
                    cur_date = data[0]
                    if os.path.isdir('{}/{}/{}'.format(self.jpg_open_path, data[0], data[1])):
                        os.rename('{}/{}/{}'.format(self.jpg_open_path, data[0], data[1]),\
                                '{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name))
                        target_list.append('{}/{}/{}|{}/{}/{}'.format(self.jpg_open_path, data[0], data[1], self.jpg_open_path,\
                                            data[0], change_cls_name))
                    if os.path.isfile('{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2])):
                        os.rename('{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2]),\
                                  '{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[3]))
                        target_list.append('{}/{}/{}/{}|{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2],\
                                            self.jpg_open_path, data[0], change_cls_name, data[3]))
                    # else:
                    #     msgbox.showwarning('경고', '변경할 {}/{}/{}/{} 파일이 없습니다. 확인이 필요합니다.'\
                    #         .format(self.jpg_open_path, data[0], change_cls_name, data[2]))
                elif cur_date == data[0] and cur_cls_name != data[1]:
                    cur_cls_name = data[1]
                    if cur_cls_name in wrong_cls_name:
                        change_cls_name = new_cls_name[wrong_cls_name.index(cur_cls_name)]
                        if os.path.isdir('{}/{}/{}'.format(self.jpg_open_path, data[0], data[1])):
                            os.rename('{}/{}/{}'.format(self.jpg_open_path, data[0], data[1]),\
                                    '{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name))
                            target_list.append('{}/{}/{}|{}/{}/{}'.format(self.jpg_open_path, data[0], data[1], self.jpg_open_path,\
                                                data[0], change_cls_name))
                        if os.path.isfile('{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2])):
                            os.rename('{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2]),\
                                    '{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[3]))
                            target_list.append('{}/{}/{}/{}|{}/{}/{}/{}'.format(self.jpg_open_path, data[0], change_cls_name, data[2],\
                                                self.jpg_open_path, data[0], change_cls_name, data[3]))
                        # else:
                        #     msgbox.showwarning('경고', '변경할 {}/{}/{}/{} 파일이 없습니다. 확인이 필요합니다.'\
                        #         .format(self.jpg_open_path, data[0], change_cls_name, data[2]))
                cur_qy += 1
                self.progress(cur_qy, line_qy, '클래스 오기 클래스명 변경')
            self.save_log(target_list, '2_class')
        except:
            msgbox.showwarning('경고', '작업이 완료되지 않았습니다. 처음부터 다시 진행해 주세요. 2')
            self.work_ok = 1
            
    def jpg_change_name(self):
        try:
            self.change_data = []
            f = open('{}/main_jpg_space_json.csv'.format(self.filename_path), 'r', encoding = 'CP949')
            f_field_name = ['이미지 경로', '이전 파일명', '변경 파일명', '참고 사항', '허공 이미지', 'JSON 경로',\
                            '이전 JSON명', '변경 JSON명']
            change_line = csv.DictReader(f, fieldnames = f_field_name)
            for line in change_line:
                if line['이미지 경로'] == '이미지 경로':
                    continue
                if line['변경 파일명'] != '':
                    self.change_data.append([line['이미지 경로'], line['이전 파일명'], line['변경 파일명'], line['참고 사항'],\
                                        line['허공 이미지'], line['JSON 경로'], line['이전 JSON명'], line['변경 JSON명']])
            
            wrong_cls_name = ['HairBrush']
            new_cls_name = ['HairBrushComb']
            # rename class jpg folder/file in change list
            line_qy = len(self.change_data)
            cur_qy = 0
            target_list = []
            for data in self.change_data:
                data_date = data[0].strip().split('/')[0]
                data_class = data[0].strip().split('/')[1]
                if not data[2]:
                    continue
                else:
                    if not data[3]:
                        if os.path.isfile('{}/{}/{}'.format(self.jpg_open_path, data[0], data[1])):
                            os.rename('{}/{}/{}'.format(self.jpg_open_path, data[0], data[1]),\
                                      '{}/{}/{}'.format(self.jpg_open_path, data[0], data[2]))
                            target_list.append('{}/{}/{}|{}/{}/{}'.format(self.jpg_open_path, data[0], data[1],\
                                                self.jpg_open_path, data[0], data[2]))
                        # else:
                        #     msgbox.showwarning('경고', '변경할 {}/{}/{} 파일이 없습니다. 확인이 필요합니다.'\
                        #         .format(self.jpg_open_path, data[0], data[1]))
                    else:
                        if data[3] == '폴더명 변경 필요':
                            if data_class in wrong_cls_name:
                                change_cls_name = new_cls_name[wrong_cls_name.index(data_class)]
                                if os.path.isdir('{}/{}/{}'.format(self.jpg_open_path, data_date, data_class)):
                                    os.rename('{}/{}/{}'.format(self.jpg_open_path, data_date, data_class),\
                                            '{}/{}/{}'.format(self.jpg_open_path, data_date, change_cls_name))
                                    target_list.append('{}/{}/{}|{}/{}/{}'.format(self.jpg_open_path, data_date, data_class,\
                                                       self.jpg_open_path, data_date, change_cls_name))
                                if os.path.isfile('{}/{}/{}/{}'.format(self.jpg_open_path, data_date, change_cls_name, data[1])):
                                    os.rename('{}/{}/{}/{}'.format(self.jpg_open_path, data_date, change_cls_name, data[1]),\
                                              '{}/{}/{}/{}'.format(self.jpg_open_path, data_date, change_cls_name, data[2]))
                                    target_list.append('{}/{}/{}/{}|{}/{}/{}/{}'.format(self.jpg_open_path, data_date, change_cls_name, data[1],\
                                                        self.jpg_open_path, data_date, change_cls_name, data[2]))
                                # else:
                                #     msgbox.showwarning('경고', '변경할 {}/{}/{}/{} 파일이 없습니다. 확인이 필요합니다.'\
                                #         .format(self.jpg_open_path, data_date, change_cls_name, data[1]))
                        elif data[3] == '폴더 이동 필요':
                            if os.path.isfile('{}/{}/{}/{}'.format(self.jpg_open_path, data_date, data_class, data[1])):
                                os.rename('{}/{}/{}/{}'.format(self.jpg_open_path, data_date, data_class, data[1]),\
                                          '{}/{}/{}/{}'.format(self.jpg_open_path, data_date, data_class, data[2]))
                                target_list.append('{}/{}/{}/{}|{}/{}/{}/{}'.format(self.jpg_open_path, data_date, data_class, data[1],\
                                                    self.jpg_open_path, data_date, data_class, data[2]))
                                new_class = data[2].strip().split('_')[0]
                                if os.path.isdir('{}/{}/{}'.format(self.jpg_open_path, data_date, new_class)):
                                    shutil.move('{}/{}/{}/{}'.format(self.jpg_open_path, data_date, data_class, data[2]),\
                                                '{}/{}/{}/{}'.format(self.jpg_open_path, data_date, new_class, data[2]))
                                    target_list.append('{}/{}/{}/{}|{}/{}/{}/{}'.format(self.jpg_open_path, data_date, data_class, data[2],\
                                                        self.jpg_open_path, data_date, new_class, data[2]))
                                else:
                                    os.mkdir('{}/{}/{}'.format(self.jpg_open_path, data[0], new_class))
                                    shutil.move('{}/{}/{}/{}'.format(self.jpg_open_path, data_date, data_class, data[2]),\
                                                '{}/{}/{}/{}'.format(self.jpg_open_path, data_date, new_class, data[2]))
                                    target_list.append('{}/{}/{}/{}|{}/{}/{}/{}'.format(self.jpg_open_path, data_date, data_class, data[2],\
                                                        self.jpg_open_path, data_date, new_class, data[2]))
                            # else:
                            #     msgbox.showwarning('경고', '변경할 {}/{}/{}/{} 파일이 없습니다. 확인이 필요합니다.'\
                            #         .format(self.jpg_open_path, data_date, data_class, data[1]))
                cur_qy += 1
                self.progress(cur_qy, line_qy, 'JPG 파일명 중복 등 파일명 변경')
            self.save_log(target_list, '3_jpg_file')
        except:
            msgbox.showwarning('경고', '작업이 완료되지 않았습니다. 처음부터 다시 진행해 주세요. 3')
            self.work_ok = 1
            
    def json_change_name(self):
        try:
            # rename class json folder/file in change list
            line_qy = len(self.change_data)
            cur_qy = 0
            target_list = []
            for data in self.change_data:
                data_date = data[5].strip().split('/')[0]
                data_class = data[5].strip().split('/')[2]
                if not data[7]:
                    continue
                else:
                    if not data[3]:
                        if data[5] != '경로 없음':
                            if os.path.isfile('{}/{}/polygon/{}'.format(self.json_open_path, data[5], data[6])):
                                os.rename('{}/{}/polygon/{}'.format(self.json_open_path, data[5], data[6]),\
                                        '{}/{}/polygon/{}'.format(self.json_open_path, data[5], data[7]))
                                target_list.append('{}/{}/{}|{}/{}/{}'.format(self.json_open_path, data[5], data[6],\
                                                    self.json_open_path, data[5], data[7]))
                            # else:
                            #     msgbox.showwarning('경고', '변경할 {}/{}/{} 파일이 없습니다. 확인이 필요합니다.'\
                            #         .format(self.json_open_path, data[5], data[6]))
                    else:
                        if data[3] == '폴더명 변경 필요':
                            continue
                        elif data[3] == '폴더 이동 필요':
                            if data[5] != '경로 없음':
                                if os.path.isfile('{}/{}/polygon/{}/{}'.format(self.json_open_path, data_date, data_class, data[6])):
                                    os.rename('{}/{}/polygon/{}/{}'.format(self.json_open_path, data_date, data_class, data[6]),\
                                              '{}/{}/polygon/{}/{}'.format(self.json_open_path, data_date, data_class, data[7]))
                                    target_list.append('{}/{}/polygon/{}/{}|{}/{}/polygon/{}/{}'.format(self.json_open_path,\
                                                       data_date, data_class, data[6], self.json_open_path, data_date,\
                                                       data_class, data[7]))
                                    new_class = data[7].strip().split('_')[0]
                                    if os.path.isdir('{}/{}/polygon/{}'.format(self.json_open_path, data_date, new_class)):
                                        shutil.move('{}/{}/polygon/{}/{}'.format(self.json_open_path, data_date, data_class, data[6]),\
                                                    '{}/{}/polygon/{}/{}'.format(self.json_open_path, data_date, new_class, data[7]))
                                        target_list.append('{}/{}/polygon/{}/{}|{}/{}/polygon/{}/{}'.format(self.json_open_path,\
                                                           data_date, data_class, data[6], self.json_open_path, data_date,\
                                                           new_class, data[7]))
                                    else:
                                        os.mkdir('{}/{}/polygon/{}'.format(self.json_open_path, data[0], new_class))
                                        shutil.move('{}/{}/polygon/{}/{}'.format(self.json_open_path, data_date, data_class, data[6]),\
                                                    '{}/{}/polygon/{}/{}'.format(self.json_open_path, data_date, new_class, data[7]))
                                        target_list.append('{}/{}/polygon/{}/{}|{}/{}/polygon/{}/{}'.format(self.json_open_path,\
                                                           data_date, data_class, data[2], self.json_open_path, data_date,\
                                                           new_class, data[2]))
                                # else:
                                #     msgbox.showwarning('경고', '변경할 {}/{}/polygon/{}/{} 파일이 없습니다. 확인이 필요합니다.'\
                                #         .format(self.json_open_path, data_date, data_class, data[6]))
                cur_qy += 1
                self.progress(cur_qy, line_qy, 'JSON 파일명 중복 등 파일명 변경')
            self.save_log(target_list, '3_json_file')
        except:
            msgbox.showwarning('경고', '작업이 완료되지 않았습니다. 처음부터 다시 진행해 주세요. 3')
            self.work_ok = 1
            
    def jpg_classify_file(self):
        try:
            self.class_lst = []
            cur_qy = 0
            with open('class_list.txt', 'rt', encoding = 'utf-8') as file:
                while True:
                    tmp_line = file.readline().strip()
                    if not tmp_line:
                        break
                    class_name = tmp_line.split('|')[1]
                    self.class_lst.append(class_name)
            
            for lst in self.class_lst:
                if os.path.isdir('{}/{}'.format(self.jpg_save_path, lst)):
                    continue
                else:
                    os.mkdir('{}/{}'.format(self.jpg_save_path, lst))
                    
            tot_file_qy = 0
            for dlst in self.jpg_date_list:
                if '_' in dlst:
                    continue
                else:
                    class_list = os.listdir('{}/{}'.format(self.jpg_open_path, dlst))
                    for clst in class_list:
                        if os.path.isdir('{}/{}/{}'.format(self.jpg_open_path, dlst, clst)):
                            open_file_list = os.listdir('{}/{}/{}'.format(self.jpg_open_path, dlst, clst))
                            cls_file_qy = len(open_file_list)
                            if cls_file_qy % 20 == 0:
                                tot_file_qy += cls_file_qy
                            else:
                                msgbox.showwarning('경고', '[{}/{}] 폴더 안의 파일 수가 맞지 않습니다.\n확인 후 다시 시작해 주세요.'\
                                    .format(dlst, clst))
                                self.root.quit()

            target_list = []
            for dlst in self.jpg_date_list:
                if '_' in dlst:
                    continue
                else:
                    class_list = os.listdir('{}/{}'.format(self.jpg_open_path, dlst))
                    for clst in class_list:
                        if os.path.isdir('{}/{}/{}'.format(self.jpg_open_path, dlst, clst)):
                            open_file_list = os.listdir('{}/{}/{}'.format(self.jpg_open_path, dlst, clst))
                            cls_file_qy = len(open_file_list)
                            if cls_file_qy % 20 != 0:
                                msgbox.showwarning('경고', '[{}/{}] 폴더 안의 파일 수가 맞지 않습니다.\n확인 후 다시 시작해 주세요.'\
                                    .format(dlst, clst))
                                self.root.quit()
                            for flst in open_file_list:
                                if not os.path.isfile('{}/{}/{}'.format(self.jpg_save_path, clst, flst)):
                                    shutil.copyfile('{}/{}/{}/{}'.format(self.jpg_open_path, dlst, clst, flst),\
                                                    '{}/{}/{}'.format(self.jpg_save_path, clst, flst))
                                    target_list.append('{}/{}/{}/{}|{}/{}/{}'.format(self.jpg_open_path, dlst, clst, flst,\
                                                        self.jpg_save_path, clst, flst))
                                    cur_qy += 1
                                    self.progress(cur_qy, tot_file_qy, 'JPG 파일 분류')
                                else:
                                    msgbox.showwarning('경고', '[{}/{}] 폴더 안에 같은 이름의 파일이 존재합니다.\n확인 후 다시 시작해 주세요.'\
                                    .format(dlst, flst))
                                    self.root.quit()
            self.save_log(target_list, '4_jpg_classify')
        except:
            msgbox.showwarning('경고', '작업이 완료되지 않았습니다. 처음부터 다시 진행해 주세요. 4')
            self.work_ok = 1
            
    def json_classify_file(self):
        try:
            self.class_lst = []
            cur_qy = 0
            with open('class_list.txt', 'rt', encoding = 'utf-8') as file:
                while True:
                    tmp_line = file.readline().strip()
                    if not tmp_line:
                        break
                    class_name = tmp_line.split('|')[1]
                    self.class_lst.append(class_name)
            
            for lst in self.class_lst:
                if os.path.isdir('{}/{}'.format(self.json_save_path, lst)):
                    continue
                else:
                    os.mkdir('{}/{}'.format(self.json_save_path, lst))
                    
            tot_file_qy = 0
            for dlst in self.json_date_list:
                if '_' in dlst:
                    continue
                else:
                    class_list = os.listdir('{}/{}/polygon'.format(self.json_open_path, dlst))
                    for clst in class_list:
                        if os.path.isdir('{}/{}/polygon/{}'.format(self.json_open_path, dlst, clst)):
                            open_file_list = os.listdir('{}/{}/polygon/{}'.format(self.json_open_path, dlst, clst))
                            cls_file_qy = len(open_file_list)
                            if cls_file_qy % 20 == 0:
                                tot_file_qy += cls_file_qy
                            else:
                                msgbox.showwarning('경고', '[{}/{}] 폴더 안의 파일 수가 맞지 않습니다.\n확인 후 다시 시작해 주세요.'\
                                    .format(dlst, clst))
                                self.root.quit()

            target_list = []
            for dlst in self.json_date_list:
                if '_' in dlst:
                    continue
                else:
                    class_list = os.listdir('{}/{}/polygon'.format(self.json_open_path, dlst))
                    for clst in class_list:
                        if os.path.isdir('{}/{}/polygon/{}'.format(self.json_open_path, dlst, clst)):
                            open_file_list = os.listdir('{}/{}/polygon/{}'.format(self.json_open_path, dlst, clst))
                            cls_file_qy = len(open_file_list)
                            if cls_file_qy % 20 != 0:
                                msgbox.showwarning('경고', '[{}/{}] 폴더 안의 파일 수가 맞지 않습니다.\n확인 후 다시 시작해 주세요.'\
                                    .format(dlst, clst))
                                self.root.quit()
                            for flst in open_file_list:
                                if not os.path.isfile('{}/{}/{}'.format(self.json_save_path, clst, flst)):
                                    shutil.copyfile('{}/{}/{}/{}'.format(self.json_open_path, dlst, clst, flst),\
                                                    '{}/{}/{}'.format(self.json_save_path, clst, flst))
                                    target_list.append('{}/{}/{}/{}|{}/{}/{}'.format(self.json_open_path, dlst, clst, flst,\
                                                        self.json_save_path, clst, flst))
                                    cur_qy += 1
                                    self.progress(cur_qy, tot_file_qy, 'JSON 파일 분류')
                                else:
                                    msgbox.showwarning('경고', '[{}/{}] 폴더 안에 같은 이름의 파일이 존재합니다.\n확인 후 다시 시작해 주세요.'\
                                    .format(dlst, flst))
                                    self.root.quit()
            self.save_log(target_list, '4_json_classify')
        except:
            msgbox.showwarning('경고', '작업이 완료되지 않았습니다. 처음부터 다시 진행해 주세요. 4')
            self.work_ok = 1
            
    def save_log(self, target, logname):
        cur_time = time.localtime()
        save_date = time.strftime('%Y%m%d', cur_time)
        with open('{}-{}.log'.format(logname, save_date), 'w') as file:
            for i in range(len(target)):
                file.writelines('{}|{}\n'.format(i + 1, target[i]))
            tot_file_qy = 0
            empty_class = []
            if logname == '4_jpg_classify':
                for lst in self.class_lst:
                    cls_file_qy = len(os.listdir('{}/{}'.format(self.jpg_save_path, lst)))
                    if cls_file_qy == 0:
                        empty_class.append(lst)
                    cls_ins_qy = int(cls_file_qy / 20)
                    tot_file_qy += cls_file_qy
                    file.writelines('{} 클래스 총 파일 수 : {:,},   총 인스턴스 수 : {}\n'.format(lst, cls_file_qy, cls_ins_qy))
                if len(empty_class) == 0:
                    file.writelines('총 파일 수 : {:,},   작업된 총 클래스 수 : 200\n'.format(tot_file_qy))
                else:
                    empty_cls_qy = len(empty_class)
                    full_cls_qy = 200 - empty_cls_qy
                    file.writelines('총 파일 수 : {:,},   작업된 총 클래스 수 : {}\n'.format(tot_file_qy, full_cls_qy))
            if logname == '4_json_classify':
                for lst in self.class_lst:
                    cls_file_qy = len(os.listdir('{}/{}'.format(self.json_save_path, lst)))
                    if cls_file_qy == 0:
                        empty_class.append(lst)
                    cls_ins_qy = int(cls_file_qy / 20)
                    tot_file_qy += cls_file_qy
                    file.writelines('{} 클래스 총 파일 수 : {:,},   총 인스턴스 수 : {}\n'.format(lst, cls_file_qy, cls_ins_qy))
                if len(empty_class) == 0:
                    file.writelines('총 파일 수 : {:,},   작업된 총 클래스 수 : 200\n'.format(tot_file_qy))
                else:
                    empty_cls_qy = len(empty_class)
                    full_cls_qy = 200 - empty_cls_qy
                    file.writelines('총 파일 수 : {:,},   작업된 총 클래스 수 : {}\n'.format(tot_file_qy, full_cls_qy))
frameInit()