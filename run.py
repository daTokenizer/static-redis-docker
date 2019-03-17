#! python
import argparse
import os
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(
        description="Turn a list of .rdb files into a set of static redis docker images"
    )
    parser.add_argument(dest='files', nargs='*', default=["data/data.rdb"], help="the files from which to create images")
    parser.add_argument('-v', '--version', dest='version', default=None, help="the data version")

    run_args = parser.parse_args()
    return run_args


def main(args):
    for rdb_file in args.files:
        data_version = args.version
        if not data_version:
            data_date = os.path.getmtime(rdb_file)
            data_version = datetime.fromtimestamp(data_date).strftime("%Y%m%d-%H")

        filename = os.path.basename(rdb_file).split(".")[0]
        docker_build_command = f"sudo docker build --build-arg data_file={rdb_file} -t mvdb_{filename}:{data_version} ."
        print(f"building docker image using command: {docker_build_command}")
        os.system(docker_build_command)


if __name__ == '__main__':
    main(parse_args())
