import folium
import random

#设置要标记的地点名称，坐标与编号并返回
def init_data():
    names = ["解放碑", "长江索道", "黄葛古道", "鹅岭公园", "李子坝",
             "湖广会馆", "南滨路", "东水门大桥", "山城步道", "牛角沱",
             "洪崖洞","彩云湖","千厮门大桥","科园四路","十八梯",
             "人民大礼堂","两江汇"]
    length = len(names)
    locations = [[29.56025, 106.57334],
                 [29.5577, 106.5851],
                 [29.53453, 106.59380],
                 [29.55269, 106.53211],
                 [29.55667, 106.53440],
                 [29.56046, 106.58292],
                 [29.5488, 106.5853],
                 [29.56051, 106.58765],
                 [29.55324, 106.56289],
                 [29.56326, 106.53881],
                 [29.56523,106.57558],
                 # [ 29.5580684, 106.6039634],
                 [29.51319,106.48031],
                 [ 29.5680790, 106.5752375],
                 [29.5322,106.4881],
                 [29.55360,106.56963],
                 [29.56437,106.55035],
                 [29.5776,106.5851]]
    numbers = [i for i in range(1, length + 1)]
    return names,length,locations,numbers

#获取数据基本信息
names,length,locations,numbers=init_data()
#导入城市地图的中心视角经纬度，缩放比例为14，类型为OpenStreetMap
city_map = folium.Map(location=[29.55269, 106.53211], zoom_start=13,
                      )
# city_map = folium.Map(location=[29.55324,106.56289], zoom_start=14,
#                     attr='彩色版',
#                       tiles='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineCommunity/MapServer/tile/{z}/{y}/{x}')

#创建标记地点列表
markers=[]
#将地点字典加入到列表中
for i in range(length):
    temp={"location":locations[i],"name":names[i],"number":numbers[i]}
    markers.append(temp)
#打印验证是否正确
# print(markers)
#创建使用过颜色集合与后续要用的HTML语句列表
used_colors=[]
html_list=[]
#在一定范围内随机颜色生成
for marker in markers:
    # 生成随机颜色，直到找到一个不重复的颜色
    while True:
        random_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 128), random.randint(128,255))
        if random_color not in used_colors:
            used_colors.append(random_color)
            break

    tem_name=f"{marker['name']}"
    tem_num = f"{marker['number']}"
    tem_color = random_color
    # temp=f'&nbsp; {tem_name} &nbsp; <i class="fa fa-map-marker fa-2x" style="color:{random_color}"></i><br>'
    #暂存语句待后续复用
    if int(tem_num)<10:
        temp_need = f'<i class="fa fa-map-marker fa-2x " style="color:{random_color}; margin-left: 12px;" ></i>&nbsp; {tem_num}&emsp;{tem_name} &nbsp;<br>'
        text_style = 'font-size: 15px; font-weight: bold; color: red; position: relative;top: -3px; left: 8px;'
    else:
        temp_need = f'<i class="fa fa-map-marker fa-2x " style="color:{random_color}; margin-left: 12px;" ></i>&nbsp; {tem_num}&nbsp;&nbsp;{tem_name} &nbsp;<br>'
        text_style = 'font-size: 15px; font-weight: bold; color: red; position: relative;top: -3px; left: 3px;'
    # 设置文本格式
    # 设置字体大小和颜色
    formatted_tem_num = f'<span style="{text_style}"> {tem_num}</span>'  # 应用样式
    # 设置图标格式
    Icon_style = f'<i class="fa fa-map-marker fa-3x " style="color:{random_color}" ></i>{formatted_tem_num}<br>'
    html_list.append(temp_need)
    #设置自定义marker
    folium.Marker(marker['location'],
                  tooltip=marker['name'],
                  popup=marker['name'],
                  number=marker['number'],
                  icon=folium.DivIcon( icon_size=(30, 30),
                                       icon_anchor=(15, 30),
                                       html=Icon_style)
    ).add_to(city_map)
#设置图例
legend_html= """
<div style="position: fixed;
     bottom: 10px; /* 底部边距调整为20px */
     left: 50px; /* 左边边距调整为50px */
     display: inline-block;
     width: 150px;
     height: 520px;
     background-color: white;
     border: 2px solid grey;
     z-index:9999;
     text-align: left;
     font-size:14px;">
"""
#将之前暂存的标签加入
for item in html_list:
    legend_html+=item
legend_html+='</div>'
#将图例显示出来
city_map.get_root().html.add_child(folium.Element(legend_html))


#保存为HTML文件
city_map.save("city_map.html")