import re
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

def extract_simulation_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    scenarios = re.split(r'-{70,}', content)
    iteration_data = {1: {}, 2: {}}
    device_counts = []

    for scenario in scenarios:
        if not scenario.strip():
            continue

        iteration_match = re.search(r'#iteration: (\d+)', scenario)
        if not iteration_match:
            continue
        iteration = int(iteration_match.group(1))

        devices_match = re.search(r'#devices: (\d+)', scenario)
        if not devices_match:
            continue
        devices = int(devices_match.group(1))

        if devices not in device_counts and len(device_counts) < 5:
            device_counts.append(devices)

        failed_tasks_match = re.search(r'percentage of failed tasks: ([\d.]+)%', scenario)
        failed_tasks = float(failed_tasks_match.group(1)) if failed_tasks_match else 0.0

        service_time_match = re.search(r'average service time: ([\d.]+) seconds', scenario)
        service_time = float(service_time_match.group(1)) if service_time_match else 0.0

        processing_time_match = re.search(r'average processing time: ([\d.]+) seconds', scenario)
        processing_time = float(processing_time_match.group(1)) if processing_time_match else 0.0

        network_delay_match = re.search(r'average network delay: ([\d.]+) seconds', scenario)
        network_delay = float(network_delay_match.group(1)) if network_delay_match else 0.0

        if devices in iteration_data[iteration]:
            continue

        iteration_data[iteration][devices] = {
            'failed_tasks': failed_tasks,
            'service_time': service_time,
            'processing_time': processing_time,
            'network_delay': network_delay
        }

    device_counts.sort()
    sorted_data = {1: [], 2: []}

    for devices in device_counts:
        for iteration in [1, 2]:
            if devices in iteration_data[iteration]:
                sorted_data[iteration].append(iteration_data[iteration][devices])

    return device_counts, sorted_data

def generate_js_data(device_counts, sorted_data, policy_name):
    js_code = f"""// Device counts for {policy_name}
const deviceCounts = {device_counts};

const iteration1 = {{
    failedTasks: {[d['failed_tasks'] for d in sorted_data[1]]},
    serviceTime: {[d['service_time'] for d in sorted_data[1]]},
    processingTime: {[d['processing_time'] for d in sorted_data[1]]},
    networkDelay: {[d['network_delay'] for d in sorted_data[1]]},
}};

const iteration2 = {{
    failedTasks: {[d['failed_tasks'] for d in sorted_data[2]]},
    serviceTime: {[d['service_time'] for d in sorted_data[2]]},
    processingTime: {[d['processing_time'] for d in sorted_data[2]]},
    networkDelay: {[d['network_delay'] for d in sorted_data[2]]},
}};
"""
    return js_code

def process_policy(file_path, policy_name, output_dir="js"):
    device_counts, sorted_data = extract_simulation_data(file_path)
    js_data = generate_js_data(device_counts, sorted_data, policy_name)

    os.makedirs(output_dir, exist_ok=True)  
    output_filename = os.path.join(output_dir, f"{policy_name.upper()}_data.js")

    with open(output_filename, "w", encoding="utf-8") as js_file:
        js_file.write(js_data)

    print(f" File created: {output_filename}")


if __name__ == "__main__":
    policies = {
        "AIBASED": "All_Policies/Results/Ai.txt",
        "RANDOM": "All_Policies/Results/Random.txt",
        "PER": "All_Policies/Results/Predictive.txt",
        "GAME_THEORY": "All_Policies/Results/GameTheory.txt"
    }

    for policy, path in policies.items():
        if os.path.exists(path):
            process_policy(path, policy, output_dir="All_Policies/js")  # مجلد نسبي داخل المشروع
        else:
            print(f" File not found: {path}")
