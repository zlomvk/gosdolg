# -*- coding: utf8 -* -heroku create myapp --buildpack heroku/python
import requests,vk_api,random,sleep
from python3_anticaptcha import ImageToTextTask
from python3_anticaptcha import errors
captcha_key=input('Введите ключ от антикаптчи')
token=input('Вставьте ссылку с токеном от страницы, которую вы получите по ссылке:\nhttps://oauth.vk.com/authorize?client_id=2685278&scope=notify%2Cphotos%2Cfriends%2Caudio%2Cvideo%2Cnotes%2Cpages%2Cdocs%2Cstatus%2Cquestions%2Coffers%2Cwall%2Cgroups%2Cmessages%2Cnotifications%2Cstats%2Cads%2Coffline&redirect_uri=https://api.vk.com/blank.html&display=page&response_type=token&revoke=1\n\n')[43:128]
def captcha_handler(captcha):
    key = ImageToTextTask.ImageToTextTask(anticaptcha_key=captcha_key, save_format='const') \
            .captcha_handler(captcha_link=captcha.get_url())
    return captcha.try_again(key['solution']['text'])
vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
vk = vk_session.get_api()

def main():
    resp = requests.get("http://www.debt-clocks.org")
    soup = BeautifulSoup(resp.content)
    debt = str(soup.find('h1').text)
    vk.status.set(text='Госдолг США --'+str(debt)+random.choice(['. (Растёт)','. (Трамп лох)','. (Америке пизда)'])+'. Обновление госдолга каждую минуту')
while True:
    try:
        main()
        time.sleep(60)
    except:
        pass
