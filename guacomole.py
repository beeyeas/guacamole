# Python flask application exposing REST API for system resources
## Author : Bharath - beeyeas@gmail.com


from flask import Flask, jsonify, url_for
import json
import psutil

app = Flask(__name__)


@app.route("/", methods=["GET"])
def api_landing():
    return jsonify(gaucomole="Consume guacomole , stay Happy!!!")


@app.route("/v1/cpu", methods=["GET"])
def api_cpu():
    cpu_times = psutil.cpu_times()
    cpu_count = psutil.cpu_count()
    cpu_stats = psutil.cpu_stats()
    # cpu_freq = psutil.cpu_freq(percpu=True)
    cpu_freq = psutil.cpu_freq()
    return jsonify(cpu_freq=cpu_freq._asdict(), cpu_times=cpu_times._asdict(), cpu_stats=cpu_stats._asdict(), cpu_count=cpu_count)


@app.route("/v1/network")
def api_network():
    net_io_counters = psutil.net_io_counters(pernic=True)
    net_io_value_list = []
    for key, value in net_io_counters.iteritems():
        net_io_value_list.append({key:json.dumps(value._asdict())})


    net_connections = psutil.net_connections()
    #net_connections_value_list = []
    #for key, value in net_connections.iteritems():
    #    net_connections_value_list.append({key:json.dumps(value._asdict())})

    return jsonify(net_io_counters=net_io_value_list, net_connections=net_connections)


@app.route("/v1/memory")
def api_memory():
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()
    return jsonify(swap_memory=swap_memory._asdict(), virtual_memory=virtual_memory._asdict())


@app.route("/v1/disk")
def api_disk():
    disk_partitions = psutil.disk_partitions(all=True)
    disk_usage = psutil.disk_usage('/')
    disk_io_counters = psutil.disk_io_counters(perdisk=True)
    value_list = []
    for key, value in disk_io_counters.iteritems():
        value_list.append({key:json.dumps(value._asdict())})

    return jsonify(disk_io_counters=value_list, disk_usage=disk_usage._asdict(), disk_partitions=disk_partitions,)


def processcheck(seekitem):
    plist=psutil.get_process_list()
    str1=" ".join(str(x) for x in plist)
    if seekitem in str1:
        print ("Requested process is running")


if __name__ == "__main__":
    app.run()
