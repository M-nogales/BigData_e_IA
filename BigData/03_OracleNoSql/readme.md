```powershell
docker pull ghcr.io/oracle/nosql:latest-ce
docker tag ghcr.io/oracle/nosql:latest-ce oracle/nosql:ce
docker run -d --name=kvlite --hostname=kvlite --env KV_PROXY_PORT=8080 -p 8080:8080 oracle/nosql:ce

```
```powershell
ver estado haciendo un ping
docker run --rm -ti --link kvlite:store oracle/nosql:ce java -jar lib/kvstore.jar ping -host store -port 5000
```

```powershell
PS C:\Users\Manuel Nogales> docker run --rm -ti --link kvlite:store oracle/nosql:ce java -jar lib/kvstore.jar runadmin -host store -port 5000 -store kvstore

kv-> execute "CREATE TABLE myTable1 (id INTEGER, name STRING, age INTEGER, PRIMARY KEY(id))"
Statement completed successfully
```