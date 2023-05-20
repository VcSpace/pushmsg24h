# pushmsg24h
7*24小时区块链快讯

获取快讯，使用Bark-server推送到Bark App中

install:

docker run -dt --name bark --restart unless-stopped -p 8080:8080 -v /root/bark-data:/data finab/bark-server