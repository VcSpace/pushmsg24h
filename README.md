# pushmsg24h

7*24小时区块链快讯, 使用[Bark-server](https://github.com/Finb/bark-server.git)推送到Bark App中

信息传输使用AES-256加密，先配置config.ini

---

## docker安装bark-server:

docker run -dt --name bark --restart unless-stopped -p 8080:8080 -v /root/bark-data:/data finab/bark-server

---

## LICENSE

- GPLV3