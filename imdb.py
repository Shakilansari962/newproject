import requests_html
from requests_html import HTMLSession, HTMLResponse, HtmlElement

session=HTMLSession()

source=session.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth').html

boxes = source.find('div.list.detail.sub-list')[0]
print(boxes)
blocks = boxes.find('.nm-title-overview-widget-layout')[1]

title = blocks.find('h4 a')[0]
print(title.text)

time = blocks.find('p time')[0]
print(time.text)

plot = blocks.find('div.outline')[0]
print(plot.text)

direc = blocks.find('div.txt-block span')[2]
print(direc.text)