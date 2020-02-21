# -*- coding:utf-8 -*-

# 要求：
# 读取 report.txt 文件中的成绩；
# 统计每名学生总成绩、计算平均并从高到低重新排名；
# 汇总每一科目的平均分和总平均分； p
# 添加名次，替换60分以下的成绩为“不及格”；
# 将处理后的成绩另存为一个新文件（result.txt）。

#读取文件数据
datas = [] #文件中读取的数据
result = [] #处理后的数据
extra = ["0","平均"]  #每科及总分的平均分汇总
with open("report.txt", mode="r", encoding="utf-8") as f:
    for l in f :
        datas.append(l.strip().split())

#迭代计算每位同学总分、平均分
for l in datas[1:] :
    score = 0
    for s in l :
        try :
            score += int(s)
        except :
            pass
    avg = float(score) / (len(l) - 1)
    l.extend([str(score),"%.1f" %avg])
    result.append(l)

#计算每科平均分、总平均分
for num in range(1,11) :
    a = 0 #每科总分
    b = 0 #学生数
    for l in result :
        a += int(l[num])
        b += 1
    avg_2 = float(a) / b
    extra.append("%.1f" %avg_2)

#排名、替换不及格成绩展示
result.sort(reverse = True, key = lambda total_points : int(total_points[-2]))
c = 1
for i in result :
    for w in range(len(i) - 1): #替换除平均分外的不及格成绩
        try:
            if int(i[w]) < 60 :
                i[w] = "不及格"
        except :
            pass
    i.insert(0,str(c)) #添加名次
    c += 1

#修改表头字段，将统计好的数据输出到另一文件
result_2 = []
header = datas[0]
header.insert(0, "名次")
header.extend(["总分", "平均分"])
result.insert(0,header)
result.insert(1,extra)
for k in result :
    k.append("\n") #添加换行符
    result_2.append(" ".join(k))
with open("result.txt", mode="w", encoding="utf-8") as f :
    f.writelines(result_2)
