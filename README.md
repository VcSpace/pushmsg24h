# pushmsg24h

**7*24小时区块链快讯, 通过开源项目[Bark-server](https://github.com/Finb/bark-server.git)将信息推送到[Bark App](https://bark.day.app)中, 信息传输使用AES-256加密**

---

### 1.docker运行bark-server:

docker run -dt --name bark --restart unless-stopped -p 8080:8080 -v /root/bark-data:/data finab/bark-server

### 2.安装Bark app, 在app中添加服务器

### 3.配置template_config.ini并改名为config.ini

- 加密密钥可用demo中的random_key本地生成

---

### 方法2: Render

https://bark.day.app/#/deploy?id=render

---

## LICENSE

- GPLV3
