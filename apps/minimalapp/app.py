from flask import Flask
from flask import Flask, render_template, url_for, current_app, g, request

#flask 클래스를 인스턴스화
app = Flask(__name__)

#url과 실행할 함수를 매핑
@app.route("/", methods=["GET","POST"]) #허가할 HTTP 메서드 지정가능. 아무것도 지정x -> GET
def index():
    return "Hello, Flaskbook!!!"

@app.route("/hello/<name>", #route에 변수 지정. <name> 자리에 변수 아무거나 올 수 있음
           methods = ["GET"],
           endpoint="hello-endpoint") #endpoint를 지정하지 않으면 함수명이 엔드포인트가 된다.
def hello(name):
    return f"Hello, {name}!"
#flask2부터는 @app.get("/hello")로 기술하는 것이 가능

#show_name 엔드포인트 작성
@app.route("/name/<name>")
def show_name(name):
    #변수를 템플릿 엔진에게 건넨다.
    return render_template("index.html", name=name)


with app.test_request_context(): #플라스크의 테스트용 함수. 실제 요청없이 앱의 동작을 확인하기 위해 사용
    print(url_for("index"))
    print(url_for("hello-endpoint", name="world"))
    print(url_for("show_name", name="mina", page="1"))


#애플리케이션 컨텍스트를 취득하여 스택에 push
ctx = app.app_context()
ctx.push()

#current_app에 접근가능해짐
print(current_app.name) #>> apps.minimalapp.app
#앱 규모가 커지면 상호 참조로 인한 순환 참조 방지하기 위해 플라스크 앱의 인스턴스인 app을 직접 참조하는 것이 아니라, current_app에 접근한다.

#전역 임시 영역에 값을 설정
g.connection = "connection"
print(g.connection) #>> connection
#g 이용 예: 데이터베이스의 커넥션(접속)


#요청 컨텍스트
with app.test_request_context("users?updated=true"):
    print(request.args.get("updated")) #>true