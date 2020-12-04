'''依赖模块
pip install jieba, pyecharts
'''
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import jieba


with open('danmus.csv', encoding='utf-8') as f:
    text = " ".join([line.split(',')[-1] for line in f.readlines()])


words = jieba.cut(text)
_dict = {}
for word in words:
    if len(word) >= 2:
        _dict[word] = _dict.get(word, 0)+1
items = list(_dict.items())
items.sort(key=lambda x: x[1], reverse=True)
# for i in range(10):
#     word, count = items[i]
#     print(f'{word:<5}{count:>5}')


c = (
    WordCloud()
    .add(
        "",
        items,
        word_size_range=[20, 120],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .render("wordCloud.html")
)
