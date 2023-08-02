from flask import Flask
 
app = Flask(__name__)
 
 
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]
 

def template(contents, content):  #<a href>는 리다이렉트
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''
#template의 contents, content의 입력을 받아야 하므로
#중복을 처리하기 위해 getContents()라는 함수를 만듦
def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags
 
 
@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')
 
# id값을 정수로 받기 위해서 int로 지정
@app.route('/read/<int:id>/')  #id에 들어오는 것은 숫자
def read(id): 
    print(type(id))  #print문은 아래 터미널에 출력되므로 헷갈리지 말자!
    title = ''
    body = ''
    for topic in topics:   #topics 리스트에서 topic 이라는 변수명으로서 무언가를 가져옴, 딕셔너리는 id:pwd 이런 형태이기 때문에 데베로 저장할 만한 목록에 잘 쓰임
        if id == topic['id']:
            title = topic['title']   #토픽은 리스트에서 무언가를 가져온다는 의미
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')
 
 
@app.route('/create/')
def create():
    return 'Create'
 
 
app.run(debug=True)