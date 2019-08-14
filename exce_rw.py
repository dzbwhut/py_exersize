# -*- coding: utf-8 -*-
import xlrd
import xlwt

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook('excel_data.xls')
    # 获取所有sheet
    print(workbook.sheet_names()) # [u'sheet1', u'sheet2']
    #获取sheet2
    sheet2_name= workbook.sheet_names()[1]
    print(sheet2_name)
    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_name('Sheet3')
    # sheet的名称，行数，列数
    print(sheet2.name,sheet2.nrows,sheet2.ncols)
    rows = sheet2.row_values(3) # 获取第四行内容
    cols = sheet2.col_values(2) # 获取第三列内容
    print(rows)
    print(cols)

    #获取单元格内容的三种方法
    print(sheet2.cell(1,0).value)  # .encode('utf-8')
    print(sheet2.cell_value(1,1))  # .encode('utf-8')
    print(sheet2.row(1)[2].value)  # .encode('utf-8')

    # 获取单元格内容的数据类型
    print(sheet2.cell(1,3).ctype)

#设置表格样式
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

#写Excel
def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('学生',cell_overwrite_ok=True)
    row0 = ["姓名","年龄","出生日期","爱好"]
    colum0 = ["张三","李四","恋习Python","小明","小红","无名"]
    
    #写第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
    #写第一列
    for i in range(0,len(colum0)):
        sheet1.write(i+1,0,colum0[i],set_style('Times New Roman',220,True))

    sheet1.write(1,3,'2006/12/12')
    sheet1.write_merge(6,6,1,3,'未知')#合并行单元格
    sheet1.write_merge(1,2,3,3,'打游戏')#合并列单元格
    sheet1.write_merge(4,5,3,3,'打篮球')

    f.save('excel_write.xls')

if __name__ == '__main__':
    read_excel()
    write_excel()