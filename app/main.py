from ast import keyword
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import mongodb
from app.models.shopping import ShoppingModel
from app.shop_scraper import NaverShoppingScrapper
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent


app = FastAPI()
# Jinja2Template사용
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

# 하나의 라우터임 => 요청을 받고 해당하는 요청에 의한 응답을 해주는 것
# response_class=HTMLResponse => response 했을때 html을 서빙 해주겠다!
# 템플릿엔진으로 html을 보낼때 request: Request를 꼭 해주어야 함
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title":"현명한 쇼핑러(feat.최저가 scoper)"})

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, query: str):
    '''
    1. 쿼리에서 검색어 추출
    - 예외처리
    - 검색어가 없다면 사용자에게 검색을 요구 return
    - 해당 검색어에 대해 수집된 데이터가 이미 db에 존재한다면 해당 데이터를 사용자에게 보여준다. return
    2. 데이터 수집기로 해당 검색어에 대해 데이터를 수집한다.
    3. db에 수집된 데이터를 저장한다.
    - 수집된 각각의 데이터에 대해서 db에 들어갈 모델 인스턴스를 찍는다.
    - 각 모델 인스턴스를 db에 저장한다.
    '''
    naver_shopping_scrapper = NaverShoppingScrapper()
    shops = await naver_shopping_scrapper.search(query,10)
    # 오름차순 가격 정렬
    shops = sorted(shops,key = lambda x: int(x["lprice"]))
    # print(shops)
    shop_models = []
    for shop in shops:
        shop["title"] = BeautifulSoup(shop["title"], "lxml").text
        shop_model = ShoppingModel(
            keyword = query,
            title =  shop["title"],
            price = shop["lprice"],
            image = shop["image"],
            category = shop["category3"],
            brand = shop["brand"],
            link = shop["link"]
        )
        shop_models.append(shop_model)
    
    # save라는 함수가 async함수라 await을 붙혀줘야함
    # save_all 이라는 메소드는 asyncio.gather 메소드와 동일한 로직으로 비동기적으로 db에 저장한다.
    await mongodb.engine.save_all(shop_models) # db에 shop 객체 저장

    return templates.TemplateResponse(
        "index.html", {"request": request, "title":"현명한 쇼핑러(feat.최저가 scoper)","shops":shops,"keyword":query}
        )

# 앱서버가 처음 구동될때 이벤트를 발생시킴(이 함수가 실행됨)
@app.on_event("startup")
def on_app_start():
    # before app starts
    mongodb.connect()
    print("hello server")


# 앱서버가 셧다운이 됐을떄 실행되는 메소드 
@app.on_event("shutdown")
def on_app_shutdown():
    # after app shutdown
    mongodb.close()
    print("bye server")

