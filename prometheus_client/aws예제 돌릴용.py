#!/usr/bin/env python3

""" neuron-monitor frontend which acts as a Prometheus instance
"""
import sys
import json
import argparse
import signal
import os


try:
    from prometheus_client import start_http_server, Gauge, Counter, Info
except:
    print("Missing package - please install prometheus_client and then try again. 'pip install prometheus_client'")
    sys.exit(1)

global data_js
data_js = {'neuron_runtime_data': [{'pid': 15439, 'neuron_runtime_tag': '15439', 'error': '', 'report': {'execution_stats': {'period': 0.062386649, 'error_summary': {'generic': 0, 'numerical': 0, 'transient': 0, 'model': 0, 'runtime': 0, 'hardware': 0}, 'execution_summary': {'completed': 14, 'completed_with_err': 0, 'completed_with_num_err': 0, 'timed_out': 0, 'incorrect_input': 0, 'failed_to_queue': 0}, 'latency_stats': {'total_latency': {'p0': 0.0032498836517333984, 'p1': 0.0032498836517333984, 'p100': 0.0033423900604248047, 'p25': 0.0032606124877929688, 'p50': 0.003278970718383789, 'p75': 0.0033016204833984375, 'p99': 0.003339529037475586}, 'device_latency': {'p0': 0.003128528594970703, 'p1': 0.003128528594970703, 'p100': 0.0032167434692382812, 'p25': 0.0031554698944091797, 'p50': 0.003170490264892578, 'p75': 0.0031723976135253906, 'p99': 0.0031936168670654297}}, 'error': ''}, 'memory_used': {'period': 0.062512119, 'neuron_runtime_used_bytes': {'host': 1119887360, 'neuron_device': 63118912, 'usage_breakdown': {'host': {'application_memory': 1117293568, 'constants': 0, 'dma_buffers': 16512, 'tensors': 2577280}, 'neuroncore_memory_usage': {'0': {'constants': 61766864, 'model_code': 1308832, 'model_shared_scratchpad': 0, 'runtime_memory': 43216, 'tensors': 0}, '1': {'constants': 0, 'model_code': 0, 'model_shared_scratchpad': 0, 'runtime_memory': 0, 'tensors': 0}, '2': {'constants': 0, 'model_code': 0, 'model_shared_scratchpad': 0, 'runtime_memory': 0, 'tensors': 0}, '3': {'constants': 0, 'model_code': 0, 'model_shared_scratchpad': 0, 'runtime_memory': 0, 'tensors': 0}}}}, 'loaded_models': [{'name': '1.13.5.0+7dcf000a6-/tmp/tmpg0xeg0mi', 'uuid': '59e693c8a68c11edaad302a141b792b4', 'model_id': 10001, 'is_running': True, 'subgraphs': {'sg_00': {'memory_used_bytes': {'host': 12328, 'neuron_device': 62547744, 'usage_breakdown': {'host': {'application_memory': 12328, 'constants': 0, 'dma_buffers': 0, 'tensors': 0}, 'neuron_device': {'constants': 61766864, 'model_code': 737664, 'runtime_memory': 43216, 'tensors': 0}}}, 'neuroncore_index': 0, 'neuron_device_index': 0}}}], 'error': ''}, 'neuron_runtime_vcpu_usage': {'period': 0.062523811, 'vcpu_usage': {'user': 4, 'system': 0}, 'error': ''}, 'neuroncore_counters': {'period': 0.062463159, 'neuroncores_in_use': {'0': {'neuroncore_utilization': 89.01827638996558}, '1': {'neuroncore_utilization': 0}, '2': {'neuroncore_utilization': 0}, '3': {'neuroncore_utilization': 0}}, 'error': ''}}}], 'system_data': {'memory_info': {'period': 0.047664199, 'memory_total_bytes': 8033951744, 'memory_used_bytes': 6720876544, 'swap_total_bytes': 0, 'swap_used_bytes': 0, 'error': ''}, 'neuron_hw_counters': {'period': 0.047726075, 'neuron_devices': [{'neuron_device_index': 0, 'mem_ecc_corrected': 0, 'mem_ecc_uncorrected': 0, 'sram_ecc_uncorrected': 0, 'sram_ecc_corrected': 0}], 'error': ''}, 'vcpu_usage': {'period': 0.047687008, 'average_usage': {'user': 26.32, 'nice': 0, 'system': 0, 'idle': 73.68, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, 'usage_data': {'0': {'user': 50, 'nice': 0, 'system': 0, 'idle': 50, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '1': {'user': 16.67, 'nice': 0, 'system': 0, 'idle': 83.33, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '2': {'user': 0, 'nice': 0, 'system': 0, 'idle': 100, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '3': {'user': 20, 'nice': 0, 'system': 0, 'idle': 80, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}}, 'context_switch_count': 1978, 'error': ''}}, 'instance_info': {'instance_name': '', 'instance_id': 'i-0823d657f57057590', 'instance_type': 'inf1.xlarge', 'instance_availability_zone': 'us-east-2a', 'instance_availability_zone_id': 'use2-az1', 'instance_region': 'us-east-2', 'ami_id': 'ami-071c33e7823c066b5', 'subnet_id': 'subnet-dd4589b6', 'error': ''}, 'neuron_hardware_info': {'neuron_device_count': 1, 'neuroncore_per_device_count': 4, 'error': ''}}

def get_instance_labels(instance_info):
    instance_labels = {
        'instance_name': instance_info['instance_name'],
        'instance_id': instance_info['instance_id'],
        'instance_type': instance_info['instance_type'],
        'availability_zone': instance_info['instance_availability_zone'],
        'region': instance_info['instance_region'],
        'subnet_id': instance_info['subnet_id']
    }
    return instance_labels


def get_runtime_labels(instance_info, runtime_tag):
    label_dict = instance_info.copy()
    label_dict['runtime_tag'] = runtime_tag
    return label_dict


def process_neuroncore_counters(group_obj, data, labels):
    in_use_neroncore = str(os.getenv('NEURON_RT_VISIBLE_CORES'))
    use_core_list = []
    if '-' in in_use_neroncore:
        use_core_range = [int(x) for x in in_use_neroncore.split('-')]
        use_core_list = [*range(use_core_range[0],use_core_range[1]+1)]
    elif ',' in in_use_neroncore:
        use_core_list = [int(x) for x in in_use_neroncore.split(',')]
    else:
        pass    
    use_core_list_flg = [None] * len(data['neuroncores_in_use'])
    for i in use_core_list:
        use_core_list_flg[i]=True
    
    gauge_name = 'neuroncore_utilization_ratio'
    labels['neuroncore'] = None
    labels['using'] = None
    if gauge_name not in group_obj:
        group_obj[gauge_name] = Gauge(gauge_name, 'NeuronCore utilization ratio', labels.keys())
    for nc_idx, nc_data in data['neuroncores_in_use'].items():
        labels['neuroncore'] = int(nc_idx)
        labels['using']= use_core_list_flg[int(nc_idx)]
        group_obj[gauge_name].labels(**labels).set(nc_data['neuroncore_utilization'] / 100.0)


def process_neuron_runtime_vcpu_usage(group_obj, data, labels):
    gauge_name = 'neuron_runtime_vcpu_usage_ratio'
    labels['usage_type'] = None
    if gauge_name not in group_obj:
        group_obj[gauge_name] = Gauge(gauge_name, 'Runtime vCPU utilization ratio', labels.keys())
    cpu_usage_fields = ['user', 'system']
    for field in cpu_usage_fields:
        labels['usage_type'] = field
        group_obj[gauge_name].labels(**labels).set(data['vcpu_usage'][field] / 100.0)


def process_memory_used(group_obj, data, labels):
    gauge_name = 'neuron_runtime_memory_used_bytes'
    labels['memory_location'] = None
    if gauge_name not in group_obj:
        group_obj[gauge_name] = Gauge(gauge_name, 'Runtime memory used bytes', labels.keys())
    mem_locations = ['host', 'neuron_device']
    for mem_location_type in mem_locations:
        labels['memory_location'] = mem_location_type
        group_obj[gauge_name].labels(**labels).set(data['neuron_runtime_used_bytes'][mem_location_type])


def process_inference_stats(group_obj, data, labels):
    counter_name = 'inference_errors_total'
    err_labels = labels.copy()
    err_labels['error_type'] = None
    if counter_name not in group_obj:
        group_obj[counter_name] = Counter(counter_name, 'Inference errors total', err_labels.keys())
    error_summary = data['error_summary']
    for error_type in error_summary:
        err_labels['error_type'] = error_type
        group_obj[counter_name].labels(**err_labels).inc(error_summary[error_type])

    counter_name = 'inference_status_total'
    status_labels = labels.copy()
    status_labels['status_type'] = None
    if counter_name not in group_obj:
        group_obj[counter_name] = Counter(counter_name, 'Inference status total', status_labels.keys())
    inference_summary = data['inference_summary']
    for inference_outcome in inference_summary:
        status_labels['status_type'] = inference_outcome
        group_obj[counter_name].labels(**status_labels).inc(inference_summary[inference_outcome])

    gauge_name = 'inference_latency_seconds'
    latency_labels = labels.copy()
    latency_labels['percentile'] = None
    if gauge_name not in group_obj:
        group_obj[gauge_name] = Gauge(gauge_name, 'Inference latency in seconds', latency_labels.keys())
    latency_stats = data['latency_stats']
    if latency_stats['total_latency'] is not None:
        for percentile in latency_stats['total_latency']:
            latency_labels['percentile'] = percentile
            group_obj[gauge_name].labels(**latency_labels).set(latency_stats['total_latency'][percentile])


def process_neuron_hw_counters(group_obj, data, labels):
    counter_name = 'hardware_ecc_events_total'
    labels['event_type'] = None
    labels['neuron_device_index'] = None
    if counter_name not in group_obj:
        group_obj[counter_name] = Counter(counter_name, 'Hardware ecc events total', labels.keys())
    hw_counters = ['mem_ecc_corrected', 'mem_ecc_uncorrected', 'sram_ecc_uncorrected']
    for device in data['neuron_devices']:
        for counter in hw_counters:
            labels['event_type'] = counter
            labels['neuron_device_index'] = device['neuron_device_index']
            group_obj[counter_name].labels(**labels).inc(device[counter])


def process_vcpu_usage(group_obj, data, labels):
    cpu_usage_aggregation = {
        'user': ['user', 'nice'],
        'system': ['system', 'io_wait', 'irq', 'soft_irq']
    }
    gauge_name = 'system_vcpu_count'
    if gauge_name not in group_obj:
        group_obj[gauge_name] = Gauge(gauge_name, 'System vCPU count', labels.keys())
    group_obj[gauge_name].labels(**labels).set(len(data['usage_data']))

    labels['usage_type'] = None
    gauge_name = 'system_vcpu_usage_ratio'
    if gauge_name not in group_obj:
        group_obj[gauge_name] = Gauge(gauge_name, 'System CPU utilization ratio', labels.keys())
    for field, aggregated in cpu_usage_aggregation.items():
        aggregate_value = sum([data['average_usage'][item] for item in aggregated])
        aggregate_value = min(aggregate_value, 100.0)
        labels['usage_type'] = field
        group_obj[gauge_name].labels(**labels).set(aggregate_value / 100.0)


def process_memory_info(group_obj, data, labels):
    for entries in [('memory', 'system_memory'), ('swap', 'system_swap')]:
        for stat in ['total_bytes', 'used_bytes']:
            gauge_name = '{}_{}'.format(entries[1], stat)
            if gauge_name not in group_obj:
                group_obj[gauge_name] = Gauge(gauge_name,
                                              'System {} {} bytes'.format(entries[0], stat), labels.keys())
            src_entry = '{}_{}'.format(entries[0], stat)
            group_obj[gauge_name].labels(**labels).set(data[src_entry])


def process_instance_info(metric_objects, instance_data):
    if 'instance_info' not in metric_objects:
        metric_objects['instance_info'] = Info('instance', 'EC2 instance information')
        metric_objects['instance_info'].info(instance_data)


def process_report_entries(metric_objects, report_entries, labels, runtime_tag=None):
    for metric_group_name, metric_group_data in report_entries.items():
        handler_name = 'process_{}'.format(metric_group_name)
        if handler_name in globals():
            crt_error = metric_group_data['error']
            if crt_error == '':
                if metric_group_name not in metric_objects:
                    metric_objects[metric_group_name] = {}
                metric_group_object = metric_objects[metric_group_name]
                globals()[handler_name](metric_group_object, metric_group_data, labels.copy())
            else:
                if runtime_tag is not None:
                    print('Error getting {} for runtime tag {}: {}'.format(
                        metric_group_name, runtime_tag, crt_error), file=sys.stderr)
                else:
                    print('Error getting {}: {}'.format(metric_group_name, crt_error), file=sys.stderr)


def process_data(metric_objects, monitor_data, instance_info):
    if monitor_data['neuron_runtime_data'] is not None:
        for runtime in monitor_data['neuron_runtime_data']:
            runtime_tag = runtime['neuron_runtime_tag']
            ## runtime_tag 는 PID 엿음
            if runtime['error'] != '':
                print('Runtime {} error: {}'.format(runtime_tag, runtime['error']), file=sys.stderr)
                continue

            process_report_entries(metric_objects, runtime['report'],
                                   get_runtime_labels(instance_info, runtime_tag), runtime_tag)
    if monitor_data['system_data'] is not None:
        process_report_entries(metric_objects, monitor_data['system_data'], instance_info)
    process_instance_info(metric_objects, instance_info)


def update_loop():
    running = True

    def signal_handler(*_):
        nonlocal running
        running = False
    signal.signal(signal.SIGINT, signal_handler)

    """ Dictionary containing all prometheus client objects, first by metric group and
        then by metric, for example, for neuroncore_counters:
        all_metric_objects['neuroncore_counters']['neuroncore_utilization_ratio'] = Gauge(...)
    """
    all_metric_objects = {}
    instance_labels = None
    while running:

        try:
            monitor_data = data_js
        except Exception as exc:
            print('Unable to decode JSON {}'.format(exc))
            continue
        if instance_labels is None:
            instance_labels = get_instance_labels(monitor_data['instance_info'])
        process_data(all_metric_objects, monitor_data, instance_labels)


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p', '--port', default=8000,
                            type=int, help='HTTP port on which to run the server')
    args = arg_parser.parse_args()

    start_http_server(args.port)
    update_loop()


if __name__ == '__main__':
    main()
