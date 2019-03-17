# static-redis-docker
a docker container you can start with some static data from any rdb dump

To create a container using an rdb file put it under `data` dir right here and run:
`sudo docker image build --build-arg data_file=data/<rdb file> -t static_data_redis:<data version> .`

You can also create a set of images using:
`run.py file1.rdb file2.rdb file3.rdb`

Once the docker image is built, you can run it using:
`docker run -p<some local port>:6379 static_data_redis:<datetime for data>` 
and connect to it by running: 
`redis-cli -p <same local port>`

the attached `data.rdb` contains a single key. feel free to expiriment with it before copying your data in.
