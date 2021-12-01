from stream_derivator import stream_to_s3 as derivator
import os
import logging
import argparse

#os.environ['JAVA_HOME'] = "C:\Program Files\OpenJDK\jdk-8.0.262.10-hotspot"
log = logging.getLogger('loan_driver')
def main():
    args = get_args()
    topic = args["topic"]
    brokers = "127.0.0.1:9092"
    schemaregistry = "http://localhost:8081"
    checkpoint_dir = "C:\\Users\\shravan.kamidi\\PycharmProjects\\check_point_dir"
    #data_dir = "C:\\Users\\shravan.kamidi\\PycharmProjects\\data\\loans"
    data_dir = "{}/{}".format("s3://data/",topic)
    derivator.derive(topic, checkpoint_dir, data_dir,schemaregistry,brokers)

def get_args() -> dict:
    parser = argparse.ArgumentParser(description='Driver streaming data')
    parser.add_argument('--topic', required=True, type=int, help='job ID')
    parser.add_argument('--s3dir', required=True, type=str,
                        help='s3 directory')
    args = vars(parser.parse_args())
    log.info(f'Parsed args: {args}')
    return args

if __name__ == '__main__':
    try:
        main()
    except:
        log.error("Uncaught error while executing driver. exc_info:", exc_info=True)
        raise