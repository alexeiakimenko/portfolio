from jinja2 import Environment, FileSystemLoader

title = 'Домашнее задание'
h1 = 'Страница с домашним заданием'
p = 'Домашнее задание выполнено!!!'

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
tm = env.get_template('middle.html')
msg = tm.render(title=title, h_1=h1, p=p)

print(msg)
