from flask import Flask, request, redirect
 
app = Flask(__name__)
 
#삭제버튼을 만들어 id와 연결시킨 후 활성화시킴
#삭제 기능은 post 방식, url로 접근시키면 안됨
nextId = 4
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]
 
#form 태그 사용
#전송한 데이터가 /delete/{id} 이 곳으로 이동
def template(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}/" method="POST"><input type="submit" value="delete"></form></li>
        '''
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
                {contextUI}
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
    return template(getContents(), f'<h2>{title}</h2>{body}', id)
 
 
@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET': 
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)
 
 
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET': 
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)
 

@app.route('/delete/<int:id>/', methods=['POST'])  #post 방식만 허용하겠
def delete(id):
    for topic in topics:
        if id == topic['id']:   #id 가 동일할 경우
            topics.remove(topic)    #파라미터로 삭제하고자 하는 값을 전달하면 제거해주는 함수
            break
    return redirect('/')    #root로 가면 됨, 글을 삭제하면 상세보기 페이지로 갈 수 없으므로
 
 
app.run(debug=True)