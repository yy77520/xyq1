import requests
from lxml import etree
import re
import requests

cookies = {
    'localization': 'US',
    'cart_currency': 'USD',
    '_shopify_y': 'b493ba4a-55cf-41d3-a1e9-e285c42c3583',
    'ede-i': 'f9532bc1-cbe6-4424-b11d-29ee6dda2dc8',
    'ede-expid': '0fc35cdd-71cd-49af-a641-f22dc19eb887',
    'ede-expvar': 'Edge Delivery Enabled',
    'ig-id': 'ig_a6afd411de3c9c4fd74ee6327cbe5e91b7a2',
    'ig-fv': '1784854429337',
    'ig-vars': '{%22redirectedFrom%22:%22%22}',
    '_gcl_au': '1.1.120435005.1784854430',
    '__eventn_id': '0ee1fe50-fc8c-435c-a975-e75f398de6ef',
    '__kla_id': 'eyJjaWQiOiJaR0ZsTXpOa09URXROVGhtWXkwME5EazRMV0kyTXprdE16TXpOekU1TnpKa01tVTAifQ==',
    '__spdt': 'e7cde64d6cae49c5ba6776caeef64c57',
    '_clck': '1yqu6dp%5E2%5Eg80%5E1%5E2396',
    'rrssts': '1784854432591',
    '_ga': 'GA1.1.306573059.1784854433',
    'FPID': 'FPID2.2.a9ENjtnAEXlR9aD1duDFeWx4jmlj8SkJcdcraasN3fY%3D.1784854433',
    'FPLC': 'ddPqMZUOYW0NrOHYMoCOpG7Tv1obRIEJiKUxQ961wBW2YPD8QwoMQqpp8wA0qtq97HMu0zIuLteqTx9AacTJBNP8Ek4LQ8sIJaKjd%2Fy3HisK3rtGh9qVO9Y9XjIiAw%3D%3D',
    '_shopify_marketing': ':AZ-RnTcEAAEAISZA7rqyK2XRUTv4LM88RfFddI0v0LcEV1qm_aHyJzPGeJUhHc5saTThEKtNkqzn4CjFaRPOYbVVKIZa6aE_5ncl8IHHPpfgsRIdTKGqej92NiwYPGorJnxMY8eISj0EGW5DJLw1_O2QXA:',
    '_shopify_analytics': ':AZ-RnTcDAAEAYtlLr__xZXZxj8xkHBpCiw1cEP97kDyER9884SbYtrGDCOxlj9-SwwKphNMH7N2husj4TXGdU3mzYbRm7RRoafB-x1ojh9q9sBpcCEJ8-pGEVe8ASa7BGc5MjEfv0lRDfuysH3HQG9eD700NK0NQIZZkogmRAJkNQ00pfF0HtvWFbF4pdiz9p07D4Afnu3eTHAE4F-qSPfep6_E6tA:',
    'cart': 'hWNEpVC8U58Mq9tFDa5z3LL6%3Fkey%3D3a2d75137fe86a2ced92d353bf0abf67',
    'shopify_client_id': 'b493ba4a-55cf-41d3-a1e9-e285c42c3583',
    '_ps_session': '1CxMBaEFT1X5Q4uahnFms',
    '_ps_site_visit': 'true',
    'cf_clearance': 'ZGLA2qu42LWFbgtH7j6ubPTSY0lp7NOOks0OKrhnsZo-1784858322-1.2.1.1-rASf.Wl5WdXBsJ2yxuQor.vUsQtWXIboqVLEHdHUJUHgi6Rd5CgPnUbbeaHzRhvdRHqCpj8E1Dvbpv.mvR0w81XbDTZyqtlcsCo2Xfqr.B_UJhnOpjfX4miqDqG6QC5EmgyVLKnnicnL6sYjdd2ZPCQYlrBPFtztXasYSXZACmSuHaJuYDDwn4KC77UIipsJz2ZCeR.pf7oShXBf2OuQiae6bvYcv_YzLssPy.JNqeM7LPOSa49DeDUYwtAlipjd_Hri6mOMWkfIpCl7xBQzj3X8RZbOJ_JHSKmWMPDdy8mjp7LpeW1HaqDMekT0HgGq9xMbK.ednibOZKyXiFpvGQ',
    'ig-pv': '4',
    'geolizr_data': '{%22as%22:%22AS4837%20CHINA%20UNICOM%20China169%20Backbone%22%2C%22asname%22:%22CHINA169-Backbone%22%2C%22mobile%22:false%2C%22proxy%22:false%2C%22city%22:%22Jinrongjie%22%2C%22currency%22:{%22code%22:%22CNY%22}%2C%22country%22:{%22code%22:%22CN%22%2C%22country%22:%22China%22}%2C%22countryCode%22:%22CN%22%2C%22continent%22:%22Asia%22%2C%22continentCode%22:%22AS%22%2C%22isp%22:%22China%20Unicom%20Network%22%2C%22lat%22:39.9236%2C%22lon%22:116.36%2C%22org%22:%22N/A%22%2C%22query%22:%222408:8221:5c1b:3e80:521:bc41:c3b0:db40%22%2C%22region%22:%22BJ%22%2C%22regionName%22:%22Beijing%22%2C%22status%22:%22success%22%2C%22timezone%22:%22Asia/Shanghai%22%2C%22zip%22:%22%22%2C%22cloudflare%22:%22US%22%2C%22ttl%22:1490%2C%22env%22:%22PROD%22%2C%22build%22:%22ip-api%20cached%22%2C%22currencyCode%22:%22CNY%22%2C%22countryName%22:%22China%22%2C%22service%22:%22ip.lovely-app.com%22}',
    'rrpvc': '5',
    '_ga_ZJ0X2V7S9S': 'GS2.1.s1784858324$o2$g1$t1784858502$j60$l0$h0',
    '_ga_T86KF5Z744': 'GS2.1.s1784858325$o2$g1$t1784858502$j60$l0$h0',
    '_uetsid': '25f1676086fa11f18aff3be7bf45e8f8',
    '_uetvid': '25f15f1086fa11f1b3770bb3976490c5',
    'rrv2id.094a': 'c5af97f6-b114-4733-842f-82ead293ed92.1784854433.2.1784858506.1784854578.090d2651-bc8e-49f4-b614-6f7224af9c5e',
    '_ga_LV31RDQLDF': 'GS2.1.s1784858324$o2$g1$t1784858505$j57$l0$h479891005',
    '_ps_session_site_visit': '%7B%22sessionId%22%3A%22ab5aa766-dcc6-46de-a783-49adf6673fee%22%2C%22startTime%22%3A1784858544246%7D',
    '_clsk': '1e9hbln%5E1784861971249%5E1%5E1%5Ea.clarity.ms%2Fcollect',
    'ede-s': '0ab1be5f-b776-4548-9b1b-5aebffc131fc',
    '__cf_bm': 'g2ePY_x8EP9HNlFpibPZ03mSbeWj_7kGOUVk.fW.zEE-1784861971.5084517-1.0.1.1-Fvl.3JZv7amN0XsY88sXQt3qowVkZ_8G9n3Y_cdmhF0Hm2yyyhVJbKv3tMqQNJxemTql6Q7OP8D8a5FmepVRIs3qVN9Ez4iUsvo6YVbTDsDn3q7QMY5Y2jakYeLbDvHI',
    '_shopify_s': '0b7854d2-decf-4c02-81b4-48058e729add',
    '_shopify_essential': ':AZ-RnTSYAAEADrPoYPx1UPG7w77aomC1EIGBMthTGGcu_tnR6EB3Gt_a7mXAqeiyycq-DE15tOIXHyBmTu0NvElNZrIHCn-nw6Mlx939s7Zod4cOE4EUOXfwaoI-adESBbUau9_L_-KzBdhxstDtZ2YKuN3x6sedKgR60099vba39RYV0BEm2H6owk2o6qXAUDEoHGSSzJmPhOQuw_KgQqgsYR7JsLNbtsjgFiDBgG6lV-qMg6bU4hQJga9Opo41PpXl1TTpAI3A8-i1lfU0KIyEhR4hELuT0NBEuY_F6yZnvHvqPacm69ThzZ-hbC_6EVWLlXCTcshSQPkuWMs474_iDIseWpjGbSNG7L4sbhNytooNdCKogzKCyVzlDn9UJPeHqKPqbXVmAC5TS8ZOVGR1QlUCRcozGkjxZYrT9bEHf9XXYKgI1bpPMUJCQTWxKnZLvt-JqmKYXk8vR1G44Iy4IlCnWhPAh9iABUpT_z5pnhF5F1xGXncbYSEP0QlWHkF7B7UQvHExTuXghOWKChcWGqjK8bKDeHreMyDQIVFLmLXPkV69OyJcUAet4Cp7ajVLIBXNNpYkqe984m8sgLTh8ufMYKrd_C2Zq7tT4Io1fJq3WWZ-lkRvavcN98eRQ7PR_BmUuaAUzK5w4uk1XSf0Km6H:',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,ko;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    # 'cookie': 'localization=US; cart_currency=USD; _shopify_y=b493ba4a-55cf-41d3-a1e9-e285c42c3583; ede-i=f9532bc1-cbe6-4424-b11d-29ee6dda2dc8; ede-expid=0fc35cdd-71cd-49af-a641-f22dc19eb887; ede-expvar=Edge Delivery Enabled; ig-id=ig_a6afd411de3c9c4fd74ee6327cbe5e91b7a2; ig-fv=1784854429337; ig-vars={%22redirectedFrom%22:%22%22}; _gcl_au=1.1.120435005.1784854430; __eventn_id=0ee1fe50-fc8c-435c-a975-e75f398de6ef; __kla_id=eyJjaWQiOiJaR0ZsTXpOa09URXROVGhtWXkwME5EazRMV0kyTXprdE16TXpOekU1TnpKa01tVTAifQ==; __spdt=e7cde64d6cae49c5ba6776caeef64c57; _clck=1yqu6dp%5E2%5Eg80%5E1%5E2396; rrssts=1784854432591; _ga=GA1.1.306573059.1784854433; FPID=FPID2.2.a9ENjtnAEXlR9aD1duDFeWx4jmlj8SkJcdcraasN3fY%3D.1784854433; FPLC=ddPqMZUOYW0NrOHYMoCOpG7Tv1obRIEJiKUxQ961wBW2YPD8QwoMQqpp8wA0qtq97HMu0zIuLteqTx9AacTJBNP8Ek4LQ8sIJaKjd%2Fy3HisK3rtGh9qVO9Y9XjIiAw%3D%3D; _shopify_marketing=:AZ-RnTcEAAEAISZA7rqyK2XRUTv4LM88RfFddI0v0LcEV1qm_aHyJzPGeJUhHc5saTThEKtNkqzn4CjFaRPOYbVVKIZa6aE_5ncl8IHHPpfgsRIdTKGqej92NiwYPGorJnxMY8eISj0EGW5DJLw1_O2QXA:; _shopify_analytics=:AZ-RnTcDAAEAYtlLr__xZXZxj8xkHBpCiw1cEP97kDyER9884SbYtrGDCOxlj9-SwwKphNMH7N2husj4TXGdU3mzYbRm7RRoafB-x1ojh9q9sBpcCEJ8-pGEVe8ASa7BGc5MjEfv0lRDfuysH3HQG9eD700NK0NQIZZkogmRAJkNQ00pfF0HtvWFbF4pdiz9p07D4Afnu3eTHAE4F-qSPfep6_E6tA:; cart=hWNEpVC8U58Mq9tFDa5z3LL6%3Fkey%3D3a2d75137fe86a2ced92d353bf0abf67; shopify_client_id=b493ba4a-55cf-41d3-a1e9-e285c42c3583; _ps_session=1CxMBaEFT1X5Q4uahnFms; _ps_site_visit=true; cf_clearance=ZGLA2qu42LWFbgtH7j6ubPTSY0lp7NOOks0OKrhnsZo-1784858322-1.2.1.1-rASf.Wl5WdXBsJ2yxuQor.vUsQtWXIboqVLEHdHUJUHgi6Rd5CgPnUbbeaHzRhvdRHqCpj8E1Dvbpv.mvR0w81XbDTZyqtlcsCo2Xfqr.B_UJhnOpjfX4miqDqG6QC5EmgyVLKnnicnL6sYjdd2ZPCQYlrBPFtztXasYSXZACmSuHaJuYDDwn4KC77UIipsJz2ZCeR.pf7oShXBf2OuQiae6bvYcv_YzLssPy.JNqeM7LPOSa49DeDUYwtAlipjd_Hri6mOMWkfIpCl7xBQzj3X8RZbOJ_JHSKmWMPDdy8mjp7LpeW1HaqDMekT0HgGq9xMbK.ednibOZKyXiFpvGQ; ig-pv=4; geolizr_data={%22as%22:%22AS4837%20CHINA%20UNICOM%20China169%20Backbone%22%2C%22asname%22:%22CHINA169-Backbone%22%2C%22mobile%22:false%2C%22proxy%22:false%2C%22city%22:%22Jinrongjie%22%2C%22currency%22:{%22code%22:%22CNY%22}%2C%22country%22:{%22code%22:%22CN%22%2C%22country%22:%22China%22}%2C%22countryCode%22:%22CN%22%2C%22continent%22:%22Asia%22%2C%22continentCode%22:%22AS%22%2C%22isp%22:%22China%20Unicom%20Network%22%2C%22lat%22:39.9236%2C%22lon%22:116.36%2C%22org%22:%22N/A%22%2C%22query%22:%222408:8221:5c1b:3e80:521:bc41:c3b0:db40%22%2C%22region%22:%22BJ%22%2C%22regionName%22:%22Beijing%22%2C%22status%22:%22success%22%2C%22timezone%22:%22Asia/Shanghai%22%2C%22zip%22:%22%22%2C%22cloudflare%22:%22US%22%2C%22ttl%22:1490%2C%22env%22:%22PROD%22%2C%22build%22:%22ip-api%20cached%22%2C%22currencyCode%22:%22CNY%22%2C%22countryName%22:%22China%22%2C%22service%22:%22ip.lovely-app.com%22}; rrpvc=5; _ga_ZJ0X2V7S9S=GS2.1.s1784858324$o2$g1$t1784858502$j60$l0$h0; _ga_T86KF5Z744=GS2.1.s1784858325$o2$g1$t1784858502$j60$l0$h0; _uetsid=25f1676086fa11f18aff3be7bf45e8f8; _uetvid=25f15f1086fa11f1b3770bb3976490c5; rrv2id.094a=c5af97f6-b114-4733-842f-82ead293ed92.1784854433.2.1784858506.1784854578.090d2651-bc8e-49f4-b614-6f7224af9c5e; _ga_LV31RDQLDF=GS2.1.s1784858324$o2$g1$t1784858505$j57$l0$h479891005; _ps_session_site_visit=%7B%22sessionId%22%3A%22ab5aa766-dcc6-46de-a783-49adf6673fee%22%2C%22startTime%22%3A1784858544246%7D; _clsk=1e9hbln%5E1784861971249%5E1%5E1%5Ea.clarity.ms%2Fcollect; ede-s=0ab1be5f-b776-4548-9b1b-5aebffc131fc; __cf_bm=g2ePY_x8EP9HNlFpibPZ03mSbeWj_7kGOUVk.fW.zEE-1784861971.5084517-1.0.1.1-Fvl.3JZv7amN0XsY88sXQt3qowVkZ_8G9n3Y_cdmhF0Hm2yyyhVJbKv3tMqQNJxemTql6Q7OP8D8a5FmepVRIs3qVN9Ez4iUsvo6YVbTDsDn3q7QMY5Y2jakYeLbDvHI; _shopify_s=0b7854d2-decf-4c02-81b4-48058e729add; _shopify_essential=:AZ-RnTSYAAEADrPoYPx1UPG7w77aomC1EIGBMthTGGcu_tnR6EB3Gt_a7mXAqeiyycq-DE15tOIXHyBmTu0NvElNZrIHCn-nw6Mlx939s7Zod4cOE4EUOXfwaoI-adESBbUau9_L_-KzBdhxstDtZ2YKuN3x6sedKgR60099vba39RYV0BEm2H6owk2o6qXAUDEoHGSSzJmPhOQuw_KgQqgsYR7JsLNbtsjgFiDBgG6lV-qMg6bU4hQJga9Opo41PpXl1TTpAI3A8-i1lfU0KIyEhR4hELuT0NBEuY_F6yZnvHvqPacm69ThzZ-hbC_6EVWLlXCTcshSQPkuWMs474_iDIseWpjGbSNG7L4sbhNytooNdCKogzKCyVzlDn9UJPeHqKPqbXVmAC5TS8ZOVGR1QlUCRcozGkjxZYrT9bEHf9XXYKgI1bpPMUJCQTWxKnZLvt-JqmKYXk8vR1G44Iy4IlCnWhPAh9iABUpT_z5pnhF5F1xGXncbYSEP0QlWHkF7B7UQvHExTuXghOWKChcWGqjK8bKDeHreMyDQIVFLmLXPkV69OyJcUAet4Cp7ajVLIBXNNpYkqe984m8sgLTh8ufMYKrd_C2Zq7tT4Io1fJq3WWZ-lkRvavcN98eRQ7PR_BmUuaAUzK5w4uk1XSf0Km6H:',
}

params = {
    'variant': '41988608131143',
}

#发送请求
response = requests.get(
    'https://roark.com/products/mens-bless-up-breathable-stretch-shirt-fossil-print',
    params=params,
    cookies=cookies,
    headers=headers,
)



res=response.text
print(res)
# 数据解析 用xpath提取所需内容
result=etree.HTML(res)


#提取商品名称
name=result.xpath('//div[@class="product-header__title type-headline my-0"]/text()')[0]
print(f'商品的名称:{name}')

#提取商品颜色
color_match = re.search(r'"color":"([^"]*)"', res).group(1)
print(f'商品颜色{color_match}')

#提取商品价格
price= re.search(r'"price":(\d+)', res).group(1)
print(f'商品价格{price}')

#提取商品尺码
size_tag=re.search(r'"tags":(\[.*?\])', res, re.DOTALL).group(1)

# 提取所有尺寸
sizes = re.findall(r'"(L|M|S|XS|XL|XXL)"', size_tag)
print(f'商品尺码为{sizes}')  # ['L', 'M', 'S', 'XL', 'XS', 'XXL']





#dp自动化提取
# from DrissionPage import Chromium
#
# #实例化浏览器对象
# browser=Chromium()
#
# #获取标签页
# tab=browser.latest_tab
#
# #加载网站
# tab.get('https://roark.com/products/mens-bless-up-breathable-stretch-shirt-fossil-print?variant=41988608131143')
#
# #等待所有标签显示在页面中
# tab.wait.eles_loaded('x://div[@id="frame-e9a02234-239e-4e5a-817b-3aaad72b99a7"]')
#
# #提取商品名称
# name=tab.ele('x://div[@class="product-header__title type-headline my-0"]').text
# print(f'商品的名称:{name}')
#
# #提取商品价格
# price=tab.ele('x://p[@class="product-header__prices"]/span[@class="product-header__price type-item"]').text
# print(f'商品的价格:{price}')
#
# #提取商品图片链接
# img_url=tab.ele('x://img[@class="w-full h-full object-center object-contain zoomable product-media-object opacity-100"]').attr('src')
# print(f'商品图片链接{img_url}')
#
# #提取商品颜色
# color=tab.ele('x://span[@class="product-form__option-color-label__value"]').text
# print(f'商品的颜色:{color}')
#
# #提取商品尺码
# size=tab.eles('x://div[@class="field__buttons field__buttons--colors"]').text
# print(f'商品的大小:{size}')
