# static-redis-docker
a docker container you can start with some static data from any rdb dump

To create a container using an rdb file run
`sudo docker image build --build-arg data_file=<rdb file> -t static_data_redis:<datetime for data> .`

Once the docker image is built, you can run it using `docker run -p6379:<some local port> static_data_redis:<datetime for data>` and connect to it by running `redis-cli -p <same local port>`

the attached `data.rdb` contains a single key. feel free to expiriment with it before copying your data in.
