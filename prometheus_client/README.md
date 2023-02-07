
neuron-monitor | python3.7  /opt/aws/neuron/bin/neuron-monitor-prometheus.py --port 8008
curl http://localhost:8008


-------------------
/opt/aws/neuron/bin/neuron-monitor-prometheus.py
에서는 소스코드에서 글로벌로 함수를 알아서 호출하여 사용하기 떄문에 따로 호출이 없음

------------------------
그냥
{'neuron_runtime_data': [], 'system_data': {'memory_info': {'period': 0.071320236, 'memory_total_bytes': 8033951744, 'memory_used_bytes': 7020883968, 'swap_total_bytes': 0, 'swap_used_bytes': 0, 'error': ''}, 'neuron_hw_counters': {'period': 0.071320337, 'neuron_devices': [{'neuron_device_index': 0, 'mem_ecc_corrected': 0, 'mem_ecc_uncorrected': 0, 'sram_ecc_uncorrected': 0, 'sram_ecc_corrected': 0}], 'error': ''}, 'vcpu_usage': {'period': 0.071314674, 'average_usage': {'user': 10.34, 'nice': 0, 'system': 3.45, 'idle': 86.21, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, 'usage_data': {'0': {'user': 0, 'nice': 0, 'system': 0, 'idle': 100, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '1': {'user': 0, 'nice': 0, 'system': 0, 'idle': 100, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '2': {'user': 0, 'nice': 0, 'system': 12.5, 'idle': 87.5, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '3': {'user': 37.5, 'nice': 0, 'system': 12.5, 'idle': 50, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}}, 'context_switch_count': 299, 'error': ''}}, 'instance_info': {'instance_name': '', 'instance_id': 'i-0823d657f57057590', 'instance_type': 'inf1.xlarge', 'instance_availability_zone': 'us-east-2a', 'instance_availability_zone_id': 'use2-az1', 'instance_region': 'us-east-2', 'ami_id': 'ami-071c33e7823c066b5', 'subnet_id': 'subnet-dd4589b6', 'error': ''}, 'neuron_hardware_info': {'neuron_device_count': 1, 'neuroncore_per_device_count': 4, 'error': ''}}



런
<class 'dict'> {'neuron_runtime_data': [{'pid': 15439, 'neuron_runtime_tag': '15439', 'error': '', 'report': {'execution_stats': {'period': 0.062386649, 'error_summary': {'generic': 0, 'numerical': 0, 'transient': 0, 'model': 0, 'runtime': 0, 'hardware': 0}, 'execution_summary': {'completed': 14, 'completed_with_err': 0, 'completed_with_num_err': 0, 'timed_out': 0, 'incorrect_input': 0, 'failed_to_queue': 0}, 'latency_stats': {'total_latency': {'p0': 0.0032498836517333984, 'p1': 0.0032498836517333984, 'p100': 0.0033423900604248047, 'p25': 0.0032606124877929688, 'p50': 0.003278970718383789, 'p75': 0.0033016204833984375, 'p99': 0.003339529037475586}, 'device_latency': {'p0': 0.003128528594970703, 'p1': 0.003128528594970703, 'p100': 0.0032167434692382812, 'p25': 0.0031554698944091797, 'p50': 0.003170490264892578, 'p75': 0.0031723976135253906, 'p99': 0.0031936168670654297}}, 'error': ''}, 'memory_used': {'period': 0.062512119, 'neuron_runtime_used_bytes': {'host': 1119887360, 'neuron_device': 63118912, 'usage_breakdown': {'host': {'application_memory': 1117293568, 'constants': 0, 'dma_buffers': 16512, 'tensors': 2577280}, 'neuroncore_memory_usage': {'0': {'constants': 61766864, 'model_code': 1308832, 'model_shared_scratchpad': 0, 'runtime_memory': 43216, 'tensors': 0}, '1': {'constants': 0, 'model_code': 0, 'model_shared_scratchpad': 0, 'runtime_memory': 0, 'tensors': 0}, '2': {'constants': 0, 'model_code': 0, 'model_shared_scratchpad': 0, 'runtime_memory': 0, 'tensors': 0}, '3': {'constants': 0, 'model_code': 0, 'model_shared_scratchpad': 0, 'runtime_memory': 0, 'tensors': 0}}}}, 'loaded_models': [{'name': '1.13.5.0+7dcf000a6-/tmp/tmpg0xeg0mi', 'uuid': '59e693c8a68c11edaad302a141b792b4', 'model_id': 10001, 'is_running': True, 'subgraphs': {'sg_00': {'memory_used_bytes': {'host': 12328, 'neuron_device': 62547744, 'usage_breakdown': {'host': {'application_memory': 12328, 'constants': 0, 'dma_buffers': 0, 'tensors': 0}, 'neuron_device': {'constants': 61766864, 'model_code': 737664, 'runtime_memory': 43216, 'tensors': 0}}}, 'neuroncore_index': 0, 'neuron_device_index': 0}}}], 'error': ''}, 'neuron_runtime_vcpu_usage': {'period': 0.062523811, 'vcpu_usage': {'user': 4, 'system': 0}, 'error': ''}, 'neuroncore_counters': {'period': 0.062463159, 'neuroncores_in_use': {'0': {'neuroncore_utilization': 89.01827638996558}, '1': {'neuroncore_utilization': 0}, '2': {'neuroncore_utilization': 0}, '3': {'neuroncore_utilization': 0}}, 'error': ''}}}], 'system_data': {'memory_info': {'period': 0.047664199, 'memory_total_bytes': 8033951744, 'memory_used_bytes': 6720876544, 'swap_total_bytes': 0, 'swap_used_bytes': 0, 'error': ''}, 'neuron_hw_counters': {'period': 0.047726075, 'neuron_devices': [{'neuron_device_index': 0, 'mem_ecc_corrected': 0, 'mem_ecc_uncorrected': 0, 'sram_ecc_uncorrected': 0, 'sram_ecc_corrected': 0}], 'error': ''}, 'vcpu_usage': {'period': 0.047687008, 'average_usage': {'user': 26.32, 'nice': 0, 'system': 0, 'idle': 73.68, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, 'usage_data': {'0': {'user': 50, 'nice': 0, 'system': 0, 'idle': 50, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '1': {'user': 16.67, 'nice': 0, 'system': 0, 'idle': 83.33, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '2': {'user': 0, 'nice': 0, 'system': 0, 'idle': 100, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}, '3': {'user': 20, 'nice': 0, 'system': 0, 'idle': 80, 'io_wait': 0, 'irq': 0, 'soft_irq': 0}}, 'context_switch_count': 1978, 'error': ''}}, 'instance_info': {'instance_name': '', 'instance_id': 'i-0823d657f57057590', 'instance_type': 'inf1.xlarge', 'instance_availability_zone': 'us-east-2a', 'instance_availability_zone_id': 'use2-az1', 'instance_region': 'us-east-2', 'ami_id': 'ami-071c33e7823c066b5', 'subnet_id': 'subnet-dd4589b6', 'error': ''}, 'neuron_hardware_info': {'neuron_device_count': 1, 'neuroncore_per_device_count': 4, 'error': ''}}




---------------------------------
뉴런 공식 모니터링 (안달릴떄)
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 248.0
python_gc_objects_collected_total{generation="1"} 100.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 42.0
python_gc_collections_total{generation="1"} 3.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="16",version="3.7.16"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 2.27328e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.097152e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.67573525218e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.08
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP system_memory_total_bytes System memory total_bytes bytes
# TYPE system_memory_total_bytes gauge
system_memory_total_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 8.033951744e+09
# HELP system_memory_used_bytes System memory used_bytes bytes
# TYPE system_memory_used_bytes gauge
system_memory_used_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 6.98753024e+09
# HELP system_swap_total_bytes System swap total_bytes bytes
# TYPE system_swap_total_bytes gauge
system_swap_total_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
# HELP system_swap_used_bytes System swap used_bytes bytes
# TYPE system_swap_used_bytes gauge
system_swap_used_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
# HELP hardware_ecc_events_total Hardware ecc events total
# TYPE hardware_ecc_events_total counter
hardware_ecc_events_total{availability_zone="us-east-2a",event_type="mem_ecc_corrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
hardware_ecc_events_total{availability_zone="us-east-2a",event_type="mem_ecc_uncorrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
hardware_ecc_events_total{availability_zone="us-east-2a",event_type="sram_ecc_corrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
hardware_ecc_events_total{availability_zone="us-east-2a",event_type="sram_ecc_uncorrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
# HELP hardware_ecc_events_created Hardware ecc events total
# TYPE hardware_ecc_events_created gauge
hardware_ecc_events_created{availability_zone="us-east-2a",event_type="mem_ecc_corrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.675735252889595e+09
hardware_ecc_events_created{availability_zone="us-east-2a",event_type="mem_ecc_uncorrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.6757352528896165e+09
hardware_ecc_events_created{availability_zone="us-east-2a",event_type="sram_ecc_corrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.675735252889632e+09
hardware_ecc_events_created{availability_zone="us-east-2a",event_type="sram_ecc_uncorrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.6757352528896492e+09
# HELP system_vcpu_count System vCPU count
# TYPE system_vcpu_count gauge
system_vcpu_count{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 4.0
# HELP system_vcpu_usage_ratio System CPU utilization ratio
# TYPE system_vcpu_usage_ratio gauge
system_vcpu_usage_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6",usage_type="user"} 0.002
system_vcpu_usage_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6",usage_type="system"} 0.0015
# HELP instance_info EC2 instance information
# TYPE instance_info gauge
instance_info{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.0


--------------------------------
뉴런 공식 (달릴떄)
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 248.0
python_gc_objects_collected_total{generation="1"} 100.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 42.0
python_gc_collections_total{generation="1"} 3.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="16",version="3.7.16"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 2.25394688e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.0619264e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.67573580656e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.06999999999999999
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP execution_errors_total Execution errors total
# TYPE execution_errors_total counter
execution_errors_total{availability_zone="us-east-2a",error_type="generic",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0
execution_errors_total{availability_zone="us-east-2a",error_type="numerical",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0
execution_errors_total{availability_zone="us-east-2a",error_type="transient",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0
execution_errors_total{availability_zone="us-east-2a",error_type="model",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0
execution_errors_total{availability_zone="us-east-2a",error_type="runtime",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0
execution_errors_total{availability_zone="us-east-2a",error_type="hardware",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0
# HELP execution_errors_created Execution errors total
# TYPE execution_errors_created gauge
execution_errors_created{availability_zone="us-east-2a",error_type="generic",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 1.6757358073695595e+09
execution_errors_created{availability_zone="us-east-2a",error_type="numerical",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 1.6757358073695862e+09
execution_errors_created{availability_zone="us-east-2a",error_type="transient",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 1.675735807369603e+09
execution_errors_created{availability_zone="us-east-2a",error_type="model",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 1.6757358073696237e+09
execution_errors_created{availability_zone="us-east-2a",error_type="runtime",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 1.6757358073696394e+09
execution_errors_created{availability_zone="us-east-2a",error_type="hardware",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 1.6757358073696558e+09
# HELP execution_status_total Execution status total
# TYPE execution_status_total counter
execution_status_total{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="completed",subnet_id="subnet-dd4589b6"} 2977.0
execution_status_total{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="completed_with_err",subnet_id="subnet-dd4589b6"} 0.0
execution_status_total{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="completed_with_num_err",subnet_id="subnet-dd4589b6"} 0.0
execution_status_total{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="timed_out",subnet_id="subnet-dd4589b6"} 0.0
execution_status_total{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="incorrect_input",subnet_id="subnet-dd4589b6"} 0.0
execution_status_total{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="failed_to_queue",subnet_id="subnet-dd4589b6"} 0.0
# HELP execution_status_created Execution status total
# TYPE execution_status_created gauge
execution_status_created{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="completed",subnet_id="subnet-dd4589b6"} 1.675735807369699e+09
execution_status_created{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="completed_with_err",subnet_id="subnet-dd4589b6"} 1.675735807369714e+09
execution_status_created{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="completed_with_num_err",subnet_id="subnet-dd4589b6"} 1.6757358073697314e+09
execution_status_created{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="timed_out",subnet_id="subnet-dd4589b6"} 1.6757358073697498e+09
execution_status_created{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="incorrect_input",subnet_id="subnet-dd4589b6"} 1.6757358073697636e+09
execution_status_created{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",status_type="failed_to_queue",subnet_id="subnet-dd4589b6"} 1.6757358073697774e+09
# HELP execution_latency_seconds Execution latency in seconds
# TYPE execution_latency_seconds gauge
execution_latency_seconds{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",percentile="p0",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.003222942352294922
execution_latency_seconds{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",percentile="p1",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0032320022583007812
execution_latency_seconds{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",percentile="p100",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.004114866256713867
execution_latency_seconds{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",percentile="p25",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.003286123275756836
execution_latency_seconds{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",percentile="p50",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0033063888549804688
execution_latency_seconds{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",percentile="p75",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0033516883850097656
execution_latency_seconds{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",percentile="p99",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0035369396209716797
# HELP neuron_runtime_memory_used_bytes Runtime memory used bytes
# TYPE neuron_runtime_memory_used_bytes gauge
neuron_runtime_memory_used_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",memory_location="host",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 1.127288832e+09
neuron_runtime_memory_used_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",memory_location="neuron_device",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 6.3118912e+07
# HELP neuron_runtime_vcpu_usage_ratio Runtime vCPU utilization ratio
# TYPE neuron_runtime_vcpu_usage_ratio gauge
neuron_runtime_vcpu_usage_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6",usage_type="user"} 0.0365
neuron_runtime_vcpu_usage_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6",usage_type="system"} 0.0231
# HELP neuroncore_utilization_ratio NeuronCore utilization ratio
# TYPE neuroncore_utilization_ratio gauge
neuroncore_utilization_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuroncore="0",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.8633101879976985
neuroncore_utilization_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuroncore="1",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0
neuroncore_utilization_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuroncore="2",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0
neuroncore_utilization_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuroncore="3",region="us-east-2",runtime_tag="15439",subnet_id="subnet-dd4589b6"} 0.0
# HELP system_memory_total_bytes System memory total_bytes bytes
# TYPE system_memory_total_bytes gauge
system_memory_total_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 8.033951744e+09
# HELP system_memory_used_bytes System memory used_bytes bytes
# TYPE system_memory_used_bytes gauge
system_memory_used_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 7.090806784e+09
# HELP system_swap_total_bytes System swap total_bytes bytes
# TYPE system_swap_total_bytes gauge
system_swap_total_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
# HELP system_swap_used_bytes System swap used_bytes bytes
# TYPE system_swap_used_bytes gauge
system_swap_used_bytes{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
# HELP hardware_ecc_events_total Hardware ecc events total
# TYPE hardware_ecc_events_total counter
hardware_ecc_events_total{availability_zone="us-east-2a",event_type="mem_ecc_corrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
hardware_ecc_events_total{availability_zone="us-east-2a",event_type="mem_ecc_uncorrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
hardware_ecc_events_total{availability_zone="us-east-2a",event_type="sram_ecc_corrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
hardware_ecc_events_total{availability_zone="us-east-2a",event_type="sram_ecc_uncorrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 0.0
# HELP hardware_ecc_events_created Hardware ecc events total
# TYPE hardware_ecc_events_created gauge
hardware_ecc_events_created{availability_zone="us-east-2a",event_type="mem_ecc_corrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.6757358073704762e+09
hardware_ecc_events_created{availability_zone="us-east-2a",event_type="mem_ecc_uncorrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.6757358073704946e+09
hardware_ecc_events_created{availability_zone="us-east-2a",event_type="sram_ecc_corrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.6757358073705146e+09
hardware_ecc_events_created{availability_zone="us-east-2a",event_type="sram_ecc_uncorrected",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",neuron_device_index="0",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.6757358073705287e+09
# HELP system_vcpu_count System vCPU count
# TYPE system_vcpu_count gauge
system_vcpu_count{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 4.0
# HELP system_vcpu_usage_ratio System CPU utilization ratio
# TYPE system_vcpu_usage_ratio gauge
system_vcpu_usage_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6",usage_type="user"} 0.2798
system_vcpu_usage_ratio{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6",usage_type="system"} 0.029300000000000003
# HELP instance_info EC2 instance information
# TYPE instance_info gauge
instance_info{availability_zone="us-east-2a",instance_id="i-0823d657f57057590",instance_name="",instance_type="inf1.xlarge",region="us-east-2",subnet_id="subnet-dd4589b6"} 1.0

--------------------------------------
프로메테우스 예제
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 99.0
python_gc_objects_collected_total{generation="1"} 255.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 40.0
python_gc_collections_total{generation="1"} 3.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="16",version="3.7.16"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 2.24321536e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 1.9738624e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.67573547023e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.06
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP request_processing_seconds Time spent processing request
# TYPE request_processing_seconds summary
request_processing_seconds_count 32.0
request_processing_seconds_sum 15.970196242999805
# HELP request_processing_seconds_created Time spent processing request
# TYPE request_processing_seconds_created gauge
request_processing_seconds_created 1.6757354708648455e+09

--------------------------------------