from flask import Flask
import random

app = Flask(__name__)

@app.route('/')  #사용자가 패스값을 입력하지 않는다면 밑의 함수가 응대하
def index():
    return 'random : <strong>' + str(random.random()) + '</strong>'  #return값은 기본적으로 문자열을 받아야 하므로 에러가 남

app.run(port=5001, debug = True)  #디버깅 모드로 플라스크를 실행시킨다는 의미, 실제 실행 시, 디버거 모드로 하면 안됨