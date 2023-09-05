from jinja2 import Template

markup = [
    {'href': '/index', 'cl': 'class="active"', 'text': 'Главная'},
    {'href': '/news', 'cl': '', 'text': 'Новости'},
    {'href': '/about', 'cl': '', 'text': 'О компании'},
    {'href': '/shop', 'cl': '', 'text': 'Магазин'},
    {'href': '/contacts', 'cl': '', 'text': 'Контакты'},
]
string = """
<ul>
    {%- for m in markup %}
        {% if m.cl=='' -%}
            <li><a href='{{ m.href }}'>{{ m.text }}</a></li>
        {%- else -%}
            <li><a href='{{ m.href }}' {{ m.cl }}>{{ m.text }}</a></li>    
        {%- endif %}
    

    {%- endfor %}
</ul>    

"""

tm = Template(string)
msg = tm.render(markup=markup)
print(msg)