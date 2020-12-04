'''依赖模块
pip install snownlp, pyecharts
'''
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Line
from pyecharts.charts import Line, Grid
import pyecharts.options as opts


with open('danmus.csv', encoding='utf-8') as f:
    text = [float(line.split(',')[0]) for line in f.readlines()[1:]]


text = sorted([int(item) for item in text])
data = {}
for item in text:
    item = int(item/60)
    data[item] = data.get(item, 0)+1


x_data = list(data.keys())
y_data = list(data.values())
background_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
)
area_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
)
c = (
    Line(init_opts=opts.InitOpts(bg_color=JsCode(background_color_js)))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="弹幕数量",
        y_axis=y_data,
        is_smooth=True,
        symbol="circle",
        symbol_size=6,
        linestyle_opts=opts.LineStyleOpts(color="#fff"),
        label_opts=opts.LabelOpts(is_show=True, position="top", color="white"),
        itemstyle_opts=opts.ItemStyleOpts(
            color="red", border_color="#fff", border_width=3
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
        areastyle_opts=opts.AreaStyleOpts(
            color=JsCode(area_color_js), opacity=1),
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(type_="max")])
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="",
            pos_bottom="5%",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(
                color="#fff", font_size=16),
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            boundary_gap=False,
            axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
            ),
            axistick_opts=opts.AxisTickOpts(
                is_show=True,
                length=25,
                linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
            )
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            position="left",
            axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
            ),
            axistick_opts=opts.AxisTickOpts(
                is_show=True,
                length=15,
                linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
            ),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line")
    )
    .render("highlights.html")
)
