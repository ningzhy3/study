redis

brew install redis --install

Redis-server /usr/local/etc/redis.conf --start redis



Usage: ./redis-server [/path/to/redis.conf] [options]
       ./redis-server - (read config from stdin)
       ./redis-server -v or --version
       ./redis-server -h or --help
       ./redis-server --test-memory <megabytes>

Examples:
       ./redis-server (run the server with default conf)
       ./redis-server /etc/redis/6379.conf
       ./redis-server --port 7777
       ./redis-server --port 7777 --replicaof 127.0.0.1 8888
       ./redis-server /etc/myredis.conf --loglevel verbose

Sentinel mode:
       ./redis-server /etc/sentinel.conf --sentinel

redis快的原因
1. 内存数据库
2. 单线程+多路IO复用
epoll

BIO 一次连接一个线程 
NIO 一次请求一个线程
AIO 一次有效请求一个线程

redis数据类型
key+
string
set
list
hash
zset

对于key

keys* 列出所有的key
exists(key) 判断key是否存在
type(key) 判断类型
del(key) 删除某键
expire(key) (secongd) 设置失效时间
ttl(key) 查看剩余时间 -1不过期 -2过期
dbsize 查看key的数量，最多 
flushdb 清空redis
flushall 清空所有redis库

对于value

get
set
append
strlen
setnx 防止value改变，只有key存在才设置
