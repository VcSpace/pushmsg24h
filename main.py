from src.jinse import Js

# https://www.vcvc.link/AgCXLFdUwrikg4xQa4boT6/推送标题/这里改成你自己的推送内容
# docker run -d -p 8080:8080 finab/bark-server

if __name__ == '__main__':
    Js.get_news()
