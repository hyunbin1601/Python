from flask import Flask
import random
 
app = Flask(__name__)
 
 

 
topics = [   #딕셔너리에 내용을 저장하는게 편함
    {'id': 1, 'title': 'html', 'body': 'html is ...'},   #아이디로 나눈 것은 아마도 라우팅할 때 필요해서 그런듯
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascruot', 'body': 'javascript is ...'}
]   #위의 딕셔너리를 일종의 목록으로 표시해야함
 
#일반적으로 위의 내용들은 데이터베이스에서 읽어오는 코드 형식으로 바꾼
 
@app.route('/')
def index():
    liTags = ''  #빈 문자열 생성
    for topic in topics:  #for문으로 topics 순회    a 태그는 링크를 걸기 위해 추가함 -> /read 로 간다
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''<!doctype html>   
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {liTags}   
            </ol>
            <h2>Welcome</h2>
            Hello, Web
        </body>
    </html>
    '''
 
 
@app.route('/create/')
def create():
    return 'Create'
 
 
@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read '+id
 
 
app.run(debug=True)