from app.config import get_secret
import aiohttp
import asyncio
class NaverShoppingScrapper:

    NAVER_API_BOOK = "https://openapi.naver.com/v1/search/shop"
    NAVER_API_ID = get_secret("NAVER_API_ID")
    NAVER_API_SECRET = get_secret("NAVER_API_SECRET")

    @staticmethod
    async def fetch(session,url,headers):
        async with session.get(url,headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                return result["items"]

    def unit_url(self,keyword,start):
        return {
            "url" : f"{self.NAVER_API_BOOK}?query={keyword}&display=10&start={start}&sort=sim",
            "headers" : {
                "X-Naver-Client-Id" : self.NAVER_API_ID,
                "X-Naver-Client-Secret" : self.NAVER_API_SECRET
            }
        }
    
    async def search(self, keyword, total_page):
        # 해당하는 api url들이 들어가게 됨
        apis = [self.unit_url(keyword, 1 + i*10) for i in range(total_page)]
        print(apis)
        async with aiohttp.ClientSession() as session:
            all_data = await asyncio.gather(*[NaverShoppingScrapper.fetch(session,api["url"],api["headers"]) for api in apis])
            # print(all_data)
            result = []
            for data in all_data:
                if data is not None:
                    for shop in data:
                        result.append(shop)
            return result

    def run(self,keyword,total_page):
        return asyncio.run(self.search(keyword,total_page))

if __name__ == '__main__':
    scrapper = NaverShoppingScrapper()
    scrapper.run("마르지엘라", 1)

