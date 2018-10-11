# static-redis-docker
a docker container you can start with some static data from any rdb dump

to set the data for the container copy the `dump.rdb` file into this directory, rename it to `data.rdb` and run
`sudo docker image build -t static_data_redis:<datetime for data> .`

the attached `data.rdb` contains a single key. feel free to expiriment with it before copying your data in.
