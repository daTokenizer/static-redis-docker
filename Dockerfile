FROM redis
ARG data_file=data.rdb
COPY $data_file /data/data.rdb
COPY redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
