import folium
import random


def init_data():
    names = ["解放碑", "长江索道", "黄葛古道", "鹅岭公园", "李子坝",
             "湖广会馆", "南滨路", "东水门大桥", "山城步道", "牛角沱", ]
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
                 [29.56326, 106.53881], ]
    numbers = [i for i in range(1, length + 1)]
    return names,length,locations,numbers

names,length,locations,numbers=init_data()
city_map = folium.Map(location=[29.55324,106.56289], zoom_start=14,tiles='OpenStreetMap')

markers=[]
for i in range(length):
    temp={"location":locations[i],"name":names[i],"number":numbers[i]}
    markers.append(temp)

# print(markers)
used_colors=[]
html_list=[]
for marker in markers:
    # 生成随机颜色，直到找到一个不重复的颜色
    while True:
        random_color = "#{:02x}{:02x}{:02x}".format(random.randint(20, 128), random.randint(20, 128), random.randint(128,255))
        if random_color not in used_colors:
            used_colors.append(random_color)
            break

    tem_name=f"{marker['name']}"
    tem_num = f"{marker['number']}"
    tem_color = random_color
    text_style = 'font-size: 15px; font-weight: bold; color: red; position: relative;top: -3px; left: 8px;'  # 设置字体大小和颜色
    formatted_tem_num = f'<span style="{text_style}"> {tem_num}</span>'  # 应用样式

    # temp=f'&nbsp; {tem_name} &nbsp; <i class="fa fa-map-marker fa-2x" style="color:{random_color}"></i><br>'
    Icon_style=f'<i class="fa fa-map-marker fa-3x " style="color:{random_color}" ></i>{formatted_tem_num}<br>'
    temp_need = f'<i class="fa fa-map-marker fa-2x " style="color:{random_color}; margin-left: 12px;" ></i>&nbsp; {tem_num}{tem_name} &nbsp;<br>'
    html_list.append(temp_need)

    folium.Marker(marker['location'],
                  tooltip=marker['name'],
                  popup=marker['name'],
                  number=marker['number'],
                  icon=folium.DivIcon( icon_size=(30, 30),
                                       icon_anchor=(15, 30),
                                       html=Icon_style)
    ).add_to(city_map)

legend_html= """
<div style="position: fixed;
     bottom: 20px; /* 底部边距调整为20px */
     left: 50px; /* 左边边距调整为50px */
     display: inline-block;
     width: 150px;
     height: 320px;
     background-color: white;
     border: 2px solid grey;
     z-index:9999;
     text-align: left;
     font-size:14px;">
"""
for item in html_list:
    legend_html+=item
legend_html+='</div>'
city_map.get_root().html.add_child(folium.Element(legend_html))



city_map.save("city_map.html")