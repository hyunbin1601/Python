from flask import Flask
 
app = Flask(__name__)
 
 
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]
 
#create 페이지로 이동할 링크가 있어야함, template 수정하기
#li tag는 목록으로 표현하기 위해 묶어줄 때 쓰임, ul은 순서가 없는 리스트라는 의미
def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>
        </body>
    </html>
    '''
 
 
def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags
 
 
@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')
 
 
@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')
 
 
@app.route('/create/')  #/create 로 리다이렉트함
def create():
    content = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
    '''
    
    return template(getContents(), content)  #placeholder라는 속성은 입력바에 무엇을 적어여 하는지 알려주는 역할을 함
#줄바꿈은 p 태그를 이용해 정돈할 수 있음
#우리가 입력한 title과 body -> home tag를 이용해 입력값을 어디로 보내는지 정할 수 있다
#데이터를 수정하고 싶을 땐 method = "POST"
#post 방식의 데이터 전송 -> url로 데이터 전송 x, 서버로 은밀하게 전송, payload에 감춰진 형식으로 데이터 전송
#데이터를 가져올 때는 get, 입력할 때는 post
#직접 url 입력 -> get방식으로 처리
#특별한 처리를 하지 않으면 get 방식으로만

 
app.run(debug=True)