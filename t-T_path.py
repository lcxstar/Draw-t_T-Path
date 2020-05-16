import matplotlib.pyplot as plt
import pandas as pd


def read_txt(path,color):
    t_T = pd.read_csv(path,sep = '\t',encoding='utf-8')
    plt.plot(t_T['Time (Ma)'],t_T['Temperature (C)'],color = color,linewidth=1)

if __name__ == '__main__':
    # 设置图形大小及分辨率
    plt.figure(figsize=(5,5), dpi=300)
    
    #调用函数，分别输入文件路径及颜色参数
    read_txt(path1,'red')
    read_txt(path2,'lightgreen')

    #设置x,y刻度范围
    plt.xlim(0,1800)
    plt.ylim(0,300)
    #设置坐标轴的显示
    plt.xticks(range(0,1801,200))
    plt.yticks(range(0, 300, 50))
    #设置标签
    plt.ylabel('Temperature(℃)')
    plt.xlabel('time(Ma)')
    plt.tight_layout()
    
    #坐标轴反转
    ax = plt.gca()
    ax.invert_xaxis()
    ax.invert_yaxis()
    plt.show()
