from flask import Flask, request
from flask_restx import Resource, Api
import re
import controller
import visualization as vs
import redis
import steam_API_data as sad


# Flask 객체 생성
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

api = Api(app, version='1.0', title='steammend-swagger', description='steammend-swagger', doc='/api-docs')

'''
# Swagger
http://127.0.0.1:5000/api-docs
'''

steammend_api = api.namespace('api2', description='steammend-API')


@app.route("/tospring")
def spring():
    return "test"


def login_check(id):
    '''
    redis routing
    '''
    # password는 설정
    conn = redis.StrictRedis(host='localhost', password='abcd1234', port=6379, db=0)
    # 세션 존재하는 경우 판별
    # return login 상태면 steam id, 아닌 경우 no login
    if len(conn.keys()) != 0:
        # 세션이 존재하는 경우 key 가져옴
        for i in conn.keys(pattern='*spring:session:sessions:*'):
            if "expires" not in str(i):
                sessionId = str(i)
                sessionId = sessionId[2:len(sessionId)-1]
                break

        if str(conn.hget(name=sessionId, key="sessionAttr:"+id)) != "b''":
            steamId = conn.hget(name=sessionId, key="sessionAttr:"+id)
            numbers = re.sub(r'[^0-9]', '', str(steamId))
            return numbers
        else:
            return 'no login'
    else:
        return 'no login'





'''
메인페이지에서 보여주는 추천 게임 리스트 api
http://127.0.0.1:5000/api2/main-recomm

    - param : id(str)
    - return : result(dict) 최대 총 5개의 게임을 추천

    {   
        "success" : True,
        appid(사용자가 플레이했던 게임1 id):{
            "name": 사용자가 플레이했던 게임1 이름,
            "recommend":
                {
                    "_id": 추천된 게임 id,
                    "_score":,
                    "categories": ,
                    ...
                }
        },
        appid(사용자가 플레이했던 게임2 id):{
            "name": 사용자가 플레이했던 게임2 이름,
            "recommend":
                {
                    "_id": 추천된 게임 id,
                    "_score":,
                    "categories": ,
                    ...
                }
        },
        ...
    }

    {
        "success":False
    }
'''
@steammend_api.route("/main-recomm", methods=['get'])
class MainRecomm(Resource):
    def get(self):

        id= str(request.args['id'])
        steamid64=login_check(id)

        if steamid64=="no login":
            data={
                    "is_success":False,
                    "error_code":0,
                    "error_description":"Login Error"
                }
            return data

        playtime_success=sad.get_play_times_by_steamid(steamid64)

        if playtime_success==False:
            data={
                    "is_success":False,
                    "error_code":1,
                    "error_description":"No Playtime Data"
                }
            return data

        top5_games, not_top5_games=controller.get_top5_playtime_games(steamid64)
        result=controller.get_main_recomm(top5_games, not_top5_games)
        
        return result


'''
마이페이지에서 보여주는 추천 게임 리스트 api

http://127.0.0.1:5000/api2/my-recomm

    - param : id(str)
    - return: result(dict) 최대 25개의 게임을 추천
    {
        "success" : True,
        appid(사용자가 플레이했던 게임 id):{
            "name": 사용자가 플레이했던 게임 이름,
            "recommend_list":[
                추천된 게임 list
                {
                    "_id": 추천된 게임1 id,
                    "_score":,
                    "categories": ,
                    ...
                },
                {
                    "_id": 추천된 게임2 id,
                    "_score":,
                    "categories": ,
                    ...
                }
            ]
        },
        appid(사용자가 플레이했던 게임 id):{
            "name": 사용자가 플레이했던 게임 이름,
            "recommend_list":[
                추천된 게임 list
                {
                    "_id": 추천된 게임1 id,
                    "_score":,
                    "categories": ,
                    ...
                },
                {
                    "_id": 추천된 게임2 id,
                    "_score":,
                    "categories": ,
                    ...
                }
            ]
        },
        ...
    }

    {
        "success" : False
    }
'''
@steammend_api.route("/my-recomm", methods=['get','post'])
class MyRecomm(Resource):
    def post(self):
        id= str(request.args['id'])
        steamid64=login_check(id)

        if steamid64=="no login":
            data={
                    "is_success":False,
                    "error_code":0,
                    "error_description":"login error"
                }
            return data

        playtime_success=sad.get_play_times_by_steamid(steamid64)

        if playtime_success==False:
            data={
                    "is_success":False,
                    "error_code":1,
                    "error_description":"No Playtime Data"
                }
            return data

        top5_games, not_top5_games=controller.get_top5_playtime_games(steamid64)
        result=controller.get_my_recomm(top5_games, not_top5_games)

        return result



'''
steam user가 플레이한 모든 게임 데이터 중 플레이 타임이 가장 많은 
상위 5개의 게임 디테일을 반환하는 api
http://127.0.0.1:5000/api2/top5 
'''
@steammend_api.route("/top5", methods=['get', 'post'])
class PlayedTop5Games(Resource):
    def get(self):
        
        id= str(request.args['id'])
        steamid64=login_check(id)

        if steamid64=="no login":
            data={
                    "is_success":False,
                    "error_code":0,
                    "error_description":"login error"
                }
            return data

        result=controller.get_top5_playtime_games(steamid64)
        result['is_success']=True

        return result



'''
steam user가 플레이한 모든 게임 데이터 디테일 반환 api
http://127.0.0.1:5000/api2/played
'''
@steammend_api.route("/played", methods=['get', 'post'])
class PlayedAllGames(Resource):
    def get(self):

        id= str(request.args['id'])
        steamid64=login_check(id)

        if steamid64=="no login":
            data={
                    "is_success":False,
                    "error_code":0,
                    "error_description":"login error"
                }
            return data

        result = controller.get_all_played_games(steamid64)

        if result==False:
            data={
                    "is_success":False,
                    "error_code":2,
                    "error_description":"Too Many Playtime Data"
                }
            return data

        result['is_success']=True

        return result



'''
전체 top seller games 반환 api
http://127.0.0.1:5000/api2/all
'''
@steammend_api.route("/all", methods=['get', 'post'])
class AllGames(Resource):
    def get(self):
        start=int(request.args['start'])
        result = controller.get_all_games(start)
        return result

    def post(self):
        start=int(request.args['start'])
        result = controller.get_all_games(start)

        return result


'''
top seller games 중 무료인 게임 반환 api
http://127.0.0.1:5000/api2/free
    - param : start(int)
'''
@steammend_api.route("/free", methods=['get', 'post'])
class FreeGames(Resource):
    def get(self):
        start=int(request.args['start'])
        result = controller.get_free_games(start)
        
        return result



'''
top seller games 중 세일중인 게임 반환 api
http://127.0.0.1:5000/api2/sale
    - param : start(int)
    - return : result (dict)
'''
@steammend_api.route("/sale", methods=['get', 'post'])
class SaleGames(Resource):
    def get(self):
        start=int(request.args['start'])
        result = controller.get_sale_games(start)
        
        return result



'''
top seller games 중 새로 출시된 게임(2022년 10월 출시된 게임) 반환 api
http://127.0.0.1:5000/api2/new
'''
@steammend_api.route("/new", methods=['get', 'post'])
class NewGames(Resource):
    def get(self):
        
        start=int(request.args['start'])
        result = controller.get_new_games(start)

        return result



'''
게임 이름 검색 api
http://127.0.0.1:5000/api2/search
    - param : keword(str), start(int)
    - return : result(dict)
    {
        appid1:{
            "categories":[],
            "header_image":,
            "is_free":,
            ...
        },
        appid2:{
            "categories":[],
            "header_image":,
            "is_free":,
            ...
        },
        ...
    }
'''
@steammend_api.route("/search", methods=['get', 'post'])
class SearchGames(Resource):
    def get(self):
        keyword = str(request.args['keyword'])
        start = int(request.args['start'])
        result= controller.search_games_by_keyword(keyword, start)
        
        return result


'''
<<대시보드 시각화 api>>
http://127.0.0.1:5000/api2/charts 
    - param : id(str)
    - return: data(dict)

    <redis에서 steamid 받아오기를 성공했을 때>
        {
            "success":True
            "total_playtime" : total_playtime, 
            ...
        }
        
    <redis에서 steamid 받아오기를 실패했을 때>
        {
            "success":False
        }
'''
@steammend_api.route("/charts", methods=['get', 'post'])
class ShowCharts(Resource):
    
    def post(self):
        id= str(request.args['id'])
        steamid64=login_check(id)

        if steamid64=="no login":
            data={
                    "is_success":False,
                    "error_code":0,
                    "error_description":"login error"
                }
            return data

        playtime_success=sad.get_play_times_by_steamid(steamid64)

        if playtime_success==False:
            data={
                    "is_success":False,
                    "error_code":1,
                    "error_description":"No Playtime Data"
                }
            return data

        if len(playtime_success)>150:
            data={
                    "is_success":False,
                    "error_code":2,
                    "error_description":"Too Many Playtime Data"
                }
            return data

        played_games = controller.get_all_played_games(steamid64)


        total_playtime, total_count = vs.show_total_playtime_count(played_games)
        playtime_label, playtime_data = vs.show_playtime_chart(played_games)
        genre_label, genre_data = vs.show_genre_chart(played_games)
        publishers = vs.show_publisher_chart(played_games)
        wordcloud_data = vs.show_wordcloud(played_games)

        data = {
            "is_success":True,
            "total_playtime" : total_playtime, 
            "total_count" : total_count, 
            "playtime_label":playtime_label, 
            "playtime_data":playtime_data, 
            "genre_label":genre_label, 
            "genre_data":genre_data, 
            "publishers":publishers, 
            "wordcloud_data":wordcloud_data}

        return data

if __name__ == '__main__':
    app.run(debug=True)