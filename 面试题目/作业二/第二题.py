import csv
import re
import requests
from lxml import etree

list=[]

#循环遍历实现翻页
for i in range(1,7):
    url=f'https://www.cosrx.com/collections/all?page={i}&section_id=template--22575445016792__main'

    head={
        'cookie':'wm_cv=1.0.7; wm_frt=2026-07-24T06:13:03.698Z; test=test; test; __apex_test__=; localization=US; cart_currency=USD; _shopify_y=fbb3d23b-ea1d-4145-a477-82f063cc5984; _shopify_s=46b4859d-30b2-425b-b425-cb97ed6abb8e; _shopify_analytics=:AZ-SwSd7AAEAK8mho63r4VDTcDBnf1P0XsY2clOu6EIlRzCbMFLh5kce6ul74RzXagVhzeB8aXscv_fOrNy11jDVlt-hayGbIUhwRlYoLrXNQqrDMr9sO5kTvWiBvTjg9cX7P9HsDCwR3DlSCB5aa4TpPEqaoKgq9EHL:; cart=hWNEq1UgxXH30aCnJclMAO64%3Fkey%3Df6104792c113cca197dc93bb01b4a39e; _picky.widget.discounts.sessionId%3Acosrx-renewal.myshopify.com=84dd6376-e97d-4f8d-a659-e3a939c05f77; _picky.widget.discounts.isDiscountActive=false; _shopify_marketing=:AZ-SwSd7AAEAegpIkicVTPtQ-8KqjK6oUGYAiQ9a3XiUJwMQz-mxMylBWsLTsiIsvkflMyxDdqDZaLLlB7Mx9hoVhtmVcMjSBh6YqJDLU_JnJpzrJRy8bar-YFIzd5hJD27YOfZCL_kfvbhuQOMNyUn8Ht_z:; shopify_client_id=fbb3d23b-ea1d-4145-a477-82f063cc5984; _scid=wJftDJTweniXmpolLJwfV6-sqYMz_0fO; _ld_ss=1; __attentive_id=95b6644d388f40f49a768e6bd3fdccef; __attentive_session_id=c3054095dd85489fb45e5e4fb4e9f893; _attn_=eyJ1Ijoie1wiY29cIjoxNzg0ODczNTg4Mzg1LFwidW9cIjoxNzg0ODczNTg4Mzg1LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjk1YjY2NDRkMzg4ZjQwZjQ5YTc2OGU2YmQzZmRjY2VmXCJ9In0=; __attentive_cco=1784873588386; ajs_anonymous_id=b0d21aaf-3811-4a00-a5e4-cecb89988d87; __attentive_dv=1; __attentive_ss_referrer=ORGANIC; yotpo_pixel=aad8b31b-528f-409a-bb1d-867b08fd3842; _sp_ses.9947=*; _gid=GA1.2.5634902.1784873596; lo-uid=1b2031f6-1784873641425-a622b310ee1b6038; lo-visits=1; cto_bundle=hBcfVV9ZVSUyQjg5QjFnN2ZwYU5ZVTVyTCUyQnVISjFHb0JRMHolMkJJWlhCMEVmMGpMRU9WOG9QWlJnTkw3Tk80emdrajhOdUtPRHhPa0FLbWYlMkY3UmFZJTJGYmwzSnZvSmVyZ0ZWaGt3R2xkMVV6SHBkT3UlMkJZUWl2RzRVSFAzdGl5RXJOU3JlWXBRZ2xxdmVCQmp1d0ZtRE83S2U4WDc3c3clM0QlM0Q; Shoplift_Session={"isMerchant":false,"timestamp":"2026-07-24T06:30:33.916Z","entryPage":"https://www.cosrx.com/collections/all","lastSeen":1784874633916}; Shoplift_Essential={"timestamp":"2026-07-24T06:30:55.683Z","consentApproved":true,"hasConsentInteraction":false,"debugMode":false,"initialState":{"createdAt":"2026-07-24T06:12:40.601Z","utmSource":"","utmMedium":"","utmCampaign":"","utmContent":"","referrer":"","device":"desktop"},"visitorTests":[],"isFirstLoad":false}; Shoplift_Analytics={"timestamp":"2026-07-24T06:30:55.683Z","visitor":{"id":"019f92c1-832a-73d3-8f44-75d4da0fc6bf","shop":"cosrx-renewal.myshopify.com","createdAt":"2026-07-24T06:12:40.601Z","shopifyAnalyticsId":"fbb3d23b-ea1d-4145-a477-82f063cc5984","device":"desktop","utmSource":"","utmMedium":"","utmCampaign":"","utmContent":"","referrer":"","country":"CN","needsPersistence":false,"storedAt":"2026-07-24T06:30:36.181Z"},"queue":[]}; __wtba=eyJ1aSI6eyJ0IjoxNzg0ODczNTgzLjY4MywibSI6MCwidWEiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQwLjAuMC4wIFNhZmFyaS81MzcuMzYifSwicSI6W1siY29sbGVjdGlvbl92aWV3ZWQiLHsiZW50aXR5X3R5cGUiOiJjb2xsZWN0aW9uIiwiZW50aXR5X2lkIjoiMzkyOTk4ODQ2NjgwIiwicGFnZSI6Ii9jb2xsZWN0aW9ucy9hbGwiLCJ0aW1lc3RhbXAiOjE3ODQ4NzM1ODMuNjk3fV0sWyJwcm9kdWN0X3ZpZXdlZCIseyJlbnRpdHlfdHlwZSI6InByb2R1Y3QiLCJlbnRpdHlfdmFyaWFudCI6IjUxMDk4MDI1MjMwNTUyIiwiZW50aXR5X2lkIjoiOTA3MjkwNzcxNDc3NiIsInBhZ2UiOiIvY29sbGVjdGlvbnMvYWxsL3Byb2R1Y3RzL3RoZS1wZXB0aWRlLWNvbGxhZ2VuLWh5ZHJvZ2VsLWV5ZS1wYXRjaCIsInRpbWVzdGFtcCI6MTc4NDg3MzcxNS41NzV9XSxbImNvbGxlY3Rpb25fdmlld2VkIix7ImVudGl0eV90eXBlIjoiY29sbGVjdGlvbiIsImVudGl0eV9pZCI6IjM5Mjk5ODg0NjY4MCIsInBhZ2UiOiIvY29sbGVjdGlvbnMvYWxsIiwidGltZXN0YW1wIjoxNzg0ODczODc3LjI0Mn1dLFsicHJvZHVjdF92aWV3ZWQiLHsiZW50aXR5X3R5cGUiOiJwcm9kdWN0IiwiZW50aXR5X3ZhcmlhbnQiOiI1MTA5ODAyNTIzMDU1MiIsImVudGl0eV9pZCI6IjkwNzI5MDc3MTQ3NzYiLCJwYWdlIjoiL2NvbGxlY3Rpb25zL2FsbC9wcm9kdWN0cy90aGUtcGVwdGlkZS1jb2xsYWdlbi1oeWRyb2dlbC1leWUtcGF0Y2giLCJ0aW1lc3RhbXAiOjE3ODQ4NzM5NDcuMDI4fV0sWyJjb2xsZWN0aW9uX3ZpZXdlZCIseyJlbnRpdHlfdHlwZSI6ImNvbGxlY3Rpb24iLCJlbnRpdHlfaWQiOiIzOTI5OTg4NDY2ODAiLCJwYWdlIjoiL2NvbGxlY3Rpb25zL2FsbCIsInRpbWVzdGFtcCI6MTc4NDg3Mzk2Ni44Nzh9XSxbInByb2R1Y3Rfdmlld2VkIix7ImVudGl0eV90eXBlIjoicHJvZHVjdCIsImVudGl0eV92YXJpYW50IjoiNTEwOTgwMjUyMzA1NTIiLCJlbnRpdHlfaWQiOiI5MDcyOTA3NzE0Nzc2IiwicGFnZSI6Ii9jb2xsZWN0aW9ucy9hbGwvcHJvZHVjdHMvdGhlLXBlcHRpZGUtY29sbGFnZW4taHlkcm9nZWwtZXllLXBhdGNoIiwidGltZXN0YW1wIjoxNzg0ODc0MzQ2LjN9XSxbImNvbGxlY3Rpb25fdmlld2VkIix7ImVudGl0eV90eXBlIjoiY29sbGVjdGlvbiIsImVudGl0eV9pZCI6IjM5Mjk5ODg0NjY4MCIsInBhZ2UiOiIvY29sbGVjdGlvbnMvYWxsP3BhZ2U9MSIsInRpbWVzdGFtcCI6MTc4NDg3NDUwNi4zMDR9XSxbImNvbGxlY3Rpb25fdmlld2VkIix7ImVudGl0eV90eXBlIjoiY29sbGVjdGlvbiIsImVudGl0eV9pZCI6IjM5Mjk5ODg0NjY4MCIsInBhZ2UiOiIvY29sbGVjdGlvbnMvYWxsP3BhZ2U9MSIsInRpbWVzdGFtcCI6MTc4NDg3NDY1NS43MDZ9XV0sInBpIjp7Im5hbWUiOiIvY29sbGVjdGlvbnMvYWxsIiwiY291bnQiOjF9fQ==; _scsrid_r=; _scid_r=3xftDJTweniXmpolLJwfV6-sqYMz_0fO54QsnA; _shopify_essential=:AZ-SwSXyAAEAw_703nISy-YLTczQ3jdfc2BkEJNQcK6Nv_LpqV_Hj-JPvru6_XzrhqCtD5FGyUY3Yg04XYsN_mqW3cWv7uyhhtQFg8rckifLz1Uy-NdLXJWDo0ytqq-h8mZFK1SzHAsq908MlDfyXo9tFlEW7Zi-vrJem8vibReJC4ZJ2Nyj2Ngx6sx9e1Dx7xyYi2BW6WVw1SeS6vcVReVThehyH378S0dxN-jSs-9QVJDkxRswmjR2re8h3k07ZPWMqVbBkghSL3BapiWW8RPK_tLC5Yb3TUryFDJbu8cG5B1-zWicl6jHQCbq_Y5I9HOehPViVLscSRpZ14-sKrg3v1J6XFjYjgdtKebIzYNFaMMBune7mzF4lk8p9XeV-eWBq2yX8FJIpilC5jdUoQ8VEPp10zVkBWL4gSb23Pi5FSpVAItc9m_1WjYmCdcChdVLgbh0wz14flW4hibWAIf8Qzl0yDVwKkuKNzLFB98myr7atvO_MjEhhGaJvdeClhQ51D_yoPbFA-K216nvtwoUCieX-jyho4y27Z8w0-5kYCHurvt5S7_q6C6LSj8WV3I6kcMcBYkADel77OhTaUfgbzDDxxvMIjjsPSjzmN8JcTksnEXU3yQfCue75b4q1m4nZajwzy1_4os6nTEj1xmic0sdm5bd_iAXpo5Yj657Cyh7rsKRx19NjB8LAxOLYgo8z18qkLoCO6pN:; _gcl_au=1.1.491369772.1784873583.-.-.1784873588.1489461726.1784873588.1784874658; _ga_YHFLQG260N=GS2.1.s1784873588$o1$g1$t1784874658$j35$l0$h0; _ga=GA1.2.1241561706.1784873588; _gat_gtag_UA_142286643_3=1; __attentive_pv=7; _sp_id.9947=19ad3e95fd7f79d0.1784873596.1.1784874668.1784873596; _ga_WKPS9C5F1P=GS2.1.s1784873588$o1$g1$t1784874669$j24$l0$h0',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    }
    res=requests.get(url,headers=head)
    # print(res.text)

    ## 数据解析 用xpath提取所需内容
    result=etree.HTML(res.text)


    # 先获取商品列表
    name_list=result.xpath('//div[@class="innerer"]')
    # print(name_list)

    for data in name_list:
        dic={}
        #获取商品名称
        dic['商品名称']=data.xpath('./a/div[@class="product-block__title"]/text()')[0]
        #获取商品价格
        dic['商品价格']=data.xpath('./a/div[@class="product-price"]/div[@class="product-price-data"]/span/text()')[0]

        #获取详情页的url 这样发请求后可以获得成分信息
        data_url='https://www.cosrx.com'+data.xpath('./a[@class="product-link"]/@href')[0]

        #json格式的url 发送请求用来获取图片链接
        detail=data_url+'.json'
        # print(detail)
        #对详情页发送请求
        response=requests.get(detail,headers=head)

        detail_data=response.json()['product']

        # dic['信息']=detail_data['body_html']

        # #获取图片
        imgs=detail_data['images']
        # print(imgs)
        for img in imgs:
            # print(img)
            img_url=img['src']
        dic['图片链接']=img_url

        #对详情页url发送请求 获取成分 以及型号
        response1=requests.get(data_url,headers=head)
        # print(response1.text)
        result1=etree.HTML(response1.text)

        #xpath定位大的列表
        div_list = result1.xpath('//div[@class="product-description rte cf"]')

        #循环遍历大列表 以便取出p标签里面的 成分 和 型号文本
        for div in div_list:
            p_count = len(div.xpath('./p'))

            if p_count >= 3:
                # 有3个或以上p标签
                dic['成分'] = div.xpath('./p[2]/text()')[0] if div.xpath('./p[2]/text()') else 'null'
                dic['型号'] = div.xpath('./p[3]/text()')[0] if div.xpath('./p[3]/text()') else 'null'

            elif p_count >= 2:
                # 至少有2个p标签，检查是否有em
                p2 = div.xpath('./p[2]')
                if p2 and p2[0].xpath('./em'):  # 检查p[2]中是否有em
                    dic['成分'] = 'null'
                    dic['型号'] = div.xpath('./p[2]/em/text()')[0] if div.xpath('./p[2]/em/text()') else 'null'
                else:
                    dic['成分'] = 'null'
                    dic['型号'] = div.xpath('./p[2]/text()')[0] if div.xpath('./p[2]/text()') else 'null'

            else:
                # 只有1个或没有p标签
                dic['成分'] = 'null'
                dic['型号'] = div.xpath('./p[1]/text()')[0] if div.xpath('./p[1]/text()') else 'null'
        # if div_list:  # 确保找到了元素
        #     div = div_list[0]  # 取出第一个元素
        #     # print(div)
        #     # 方法1：统计p标签数量
        #     p_count = len(div.xpath('./p'))
        #     if p_count >= 3:
        #         dic['成分'] = div.xpath('./p[2]/text()')[0]  # 注意：p[2]是第二个p标签
        #         dic['型号'] = div.xpath('./p[3]/text()')[0]  # p[3]是第三个p标签
        #     else:
        #         dic['型号'] = div.xpath('./p[2]/text()')[0]
        # print(dic['商品名称'], dic['商品价格'],dic['图片链接'],dic['成分'],dic['型号'])
        # break
        list.append(dic)
print(list)

with open('作业二.csv','a',encoding='utf-8-sig',newline='')as f:
    writer=csv.DictWriter(f,fieldnames=('商品名称','商品价格','图片链接','成分','型号'))

    writer.writeheader()

    writer.writerows(list)



