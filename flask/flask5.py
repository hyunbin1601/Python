from flask import Flask, request, redirect
#request를 확인하고 싶으면 request 모듈을 import
app = Flask(__name__)
 
 
nextId = 4    #마지막 id 값이 3이니까, 그 다음 기록되는 id 값은 4부터 시작한다는 의미
topics = [   #리스트 안에 id:pwd 이런 형식의 딕셔너리를 넣을 수 있
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]
 
 
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
 
 
@app.route('/create/', methods=['GET', 'POST'])  #methods 허용 방식들을 따로 지정해야함
def create():
    print('request.method', request.method)   #request method를 통해 사용자의 요청이 get인지 post인지 확인할 수 있다 
    if request.method == 'GET':   #request.method가 get인지 post인지 확인
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId   #전역변수로 만듦, 외부에서도 동일하게 쓸 수 있, 변수로서 사용되기 이전에 global로 선언함
        title = request.form['title']   #title을 가져옴
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}  #딕셔너리 새로 생성
        topics.append(newTopic)  #딕셔너리가 추가가 된다
        url = '/read/'+str(nextId)+'/'     #post가 실행될 때마다 nextId가 url에 붙고, 1만큼 증가, 문자열과 숫자는 결합할 수 없
        nextId = nextId + 1           
        return redirect(url)   #리디렉션 -> 사용자의 웹브라우저에게 어디로 이동하라고 명령함, 리디렉트는 라이브러리
 
 #url 주소로 사용자를 보내버림
app.run(debug=True)