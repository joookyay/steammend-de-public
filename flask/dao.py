from elasticsearch import Elasticsearch

es = Elasticsearch(
    hosts=["http://127.0.0.1:9200"],
)

def get_all_games_for_recomm():
    doc = {"query": {"match_all": {}}}
    res = es.search(index='top_seller_games_02', body=doc, size=2226)

    return res


# 모든 게임 받아오기
def get_all_games(start):
    if start==0 :
        start=0
    else:
        start=start*30
    doc = {"from":start, "size":30, "query": {"match_all": {}}}
    res = es.search(index='top_seller_games_02', body=doc)

    allgames=[]

    for hit in res['hits']['hits']:
        temp=hit["_source"]
        allgames.append(temp)
    return allgames


# 무료 게임 받아오기
def get_free_games(start):

    start=start*30

    doc = {"from":start, "size":30, "query": {"term": {"is_free": {"value": "true"}}}}
    res = es.search(index="top_seller_games_02", body=doc)

    freegames = []
    for hit in res['hits']['hits']:
        temp=hit["_source"]
        freegames.append(temp)
    
    return freegames


# sale 중인 게임 받아오기
def get_sale_games(start):

    if start==0 :
        start=0
    else:
        start=start*30
    
    doc = {"from":start, "size":30, "query": {"range": {"price_overview.discount_percent": {"gt": 0}}}}
    res = es.search(index="top_seller_games_02", body=doc)

    salegames = []
    for hit in res['hits']['hits']:
        temp=hit["_source"]
        salegames.append(temp)
            
    return salegames


# new game 받아오기(2022년 10월 출시된 게임)
def get_new_games(start):
    if start==0 :
        start=0
    else:
        start=start*30
    
    doc = {"from":start, "size": 30, "query": {"bool": {"must": [{"wildcard": {"release_date.date": {
        "value": "Oct"}}}, {"term": {"release_date.date": {"value": "2022"}}}]}}}
    res = es.search(index="top_seller_games_02", body=doc)

    newgames = []
    
    for hit in res['hits']['hits']:
        temp=hit["_source"]
        newgames.append(temp)

    return newgames


# keyword 받아서 게임 이름으로 검색
def search_games_by_keyword(keyword, start):

    if start==0 :
        start=0
    else:
        start=start*30
    
    doc = {"from":start, "size": 30, "query": {"match": {"name": keyword}}}
    res = es.search(index='top_seller_games_02', body=doc)

    keywordgames = []
    for hit in res['hits']['hits']:
        temp=hit["_source"]
        keywordgames.append(temp)
    
    return keywordgames