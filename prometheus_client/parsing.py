from prometheus_client import start_http_server, Summary
import random
import time

# https://velog.io/@seokbin/%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%952-Custom-Exporter-%EA%B0%9C%EB%B0%9C
info_dict = {'neuron_runtime_data': [{'pid': 15439, 'neuron_runtime_tag': '15439', 'error': '', 'report': {'execution_stats': {'period': 0.062386649, 'error_summary': {'generic': 0, 'numerical': 0, 'transient': 0, 'model': 0, 'runtime': 0, 'hardware': 0}, 'execution_summary': {'completed': 14, 'completed_with_err': 0, 'completed_with_num_err': 0, 'timed_out': 0, 'incorrect_input': 0, 'failed_to_queue': 0}, 'latency_stats': {'total_latency': {'p0': 0.0032498836517333984, 'p1': 0.0032498836517333984, 'p100': 0.0033423900604248047, 'p25': 0.0032606124877929688, 'p50': 0.003278970718383789, 'p75': 0.0033016204833984375, 'p99': 0.003339529037475586}, 'device_latency': {'p0': 0.003128528594970703, 'p1': 0.003128528594970703, 'p100': 0.0032167434692382812, 'p25': 0.0031554698944091797, 'p50': 0.003170490264892578, 'p75': 0.0031723976135253906, 'p99': 0.0031936168670654297}}, 'error': ''}, 'memory_used': {'period': 0.062512119, 'neuron_runtime_used_bytes': {'host': 1119887360, 'neuron_device': 63118912, 'usage_breakdown': {'host': {'application_memory': 1117293568, 'constants': 0, 'dma_buffers': 16512, 'tensors': 2577280}, 'neuroncore_memory_usage': {'0': {'constants': 61766864, 'model_code': 1308832, 'model_shared_scratchpad': 0, 'runtime_memory': 43216, 'tensors': 0}, '1': {'constants': 0, 'model_code': 0, 'model_shared_scratchpad': 0, 'runtime_memory': 0, 'tensors': 0}, '2': {'constants': 0, 'model_code': 0, 'model_shared_scratchpad': 0, 'runtime_memory': 0, 'tensors': 0}, '3': {'constants': 0, 'model_code': 0, 'model_shared_scratchpad': 0, 'runtime_memory': 0, 'tensors': 0}}}}, 'loaded_models': [{'name': '1.13.5.0+7dcf000a6-/tmp/tmpg0xeg0mi', 'uuid': '59e693c8a68c11edaad302a141b792b4', 'model_id': 10001, 'is_running': True, 'subgraphs': {'sg_00': {'memory_used_bytes': {'host': 12328, 'neuron_device': 62547744, 'usage_breakdown': {'host': {'application_memory': 12328, 'constants': 0, 'dma_buffers': 0, 'tensors': 0}, 'neuron_device': {'constants': 61766864, 'model_code': 737664, 'runtime_memory': 43216, 'tensors': 0}}}, 'neuroncore_index': 0, 'neuron_device_index': 0}}}], 'error': ''}, 'neuron_runtime_vcpu_usage': {'period': 0.062523811, 'vcpu_usage': {'user': 4, 'system': 0}, 'error': ''}, 'neuroncore_counters': {'period': 0.062463159, 'neuroncores_in_use': {'0': {'neuroncore_utilization': 89.01827638996558}, '1': {'neuroncore_utilization': 0}, '2': {'neuroncore_utilization': 0}, '3': {'neuroncore_utilization': 0}}, 'error': ''}}}], 'system_data': {'memory_info': {'period': 0.047664199, 'memory_total_bytes': 8033951744, 'memory_used_bytes': 6720876544, 'swap_total_bytes': 0, 'swap_used_bytes': 0, 'error': ''}, 'neuron_hw_counters': {'period': 0.047726075, 'neuron_devices': [{'neuron_device_index': 0, 'mem_ecc_corrected': 0, 'mem_ecc_uncorrected': 0, 'sram_ecc_uncorrected': 0, 'sram_ecc_corrected': 0}], 'error': ''}, 'vcpu_usage': {'period': 0.047687008, 'average_usage': {'user': 26.32, 'nice': 0, 'system': 0, 'idle': 73.68, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, 'usage_data': {'0': {'user': 50, 'nice': 0, 'system': 0, 'idle': 50, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '1': {'user': 16.67, 'nice': 0, 'system': 0, 'idle': 83.33, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '2': {'user': 0, 'nice': 0, 'system': 0, 'idle': 100, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '3': {'user': 20, 'nice': 0, 'system': 0, 'idle': 80, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}}, 'context_switch_count': 1978, 'error': ''}}, 'instance_info': {'instance_name': '', 'instance_id': 'i-0823d657f57057590', 'instance_type': 'inf1.xlarge', 'instance_availability_zone': 'us-east-2a', 'instance_availability_zone_id': 'use2-az1', 'instance_region': 'us-east-2', 'ami_id': 'ami-071c33e7823c066b5', 'subnet_id': 'subnet-dd4589b6', 'error': ''}, 'neuron_hardware_info': {'neuron_device_count': 1, 'neuroncore_per_device_count': 4, 'error': ''}}
# Create a metric to track time spent and requests made.


print(0)
info_dict['instance_info']

# if __name__ == '__main__':
#     # Start up the server to expose the metrics.
#     start_http_server(9090)
#     # Generate some requests.
#     while True:
#         process_request(random.random())
        
# # curl "http://localhost:32210"