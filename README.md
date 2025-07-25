# Edge-Cloud Performance Dashboard for Heart Monitoring App

This project integrates a realistic **EdgeCloudSim** simulation with a web-based dashboard to analyze and visualize the performance of a **time-sensitive healthcare application**—a smart heart monitoring app.

## 🩺 Simulation Overview

We used **Sample_App5** from EdgeCloudSim because it is designed to handle **delay-sensitive** scenarios, which are crucial in real-time health applications. The simulation explores decision-making on whether a task should be executed **on the Edge (mobile device)** or **offloaded to the Cloud**, depending on system conditions (load, delay sensitivity, number of users, etc.).

The core objective is to evaluate system behavior when the number of users increases from **100 to 500 patients**. These users represent people using the heart monitoring app simultaneously.

Key questions addressed in the simulation:

- How does service time change as the number of users increases?
- How does the number of failed or delayed tasks evolve?
- Which scheduling policy yields better performance under pressure?


## ⚙️ Application: `HEART_MONITORING_APP`

| Parameter                   | Value            | Description                                           |
|----------------------------|------------------|-------------------------------------------------------|
| usage_percentage           | 100%             | All users run this app                                |
| prob_cloud_selection       | 1                | Tasks are processed on the cloud                      |
| delay_sensitivity          | 0.8              | High sensitivity to delay                             |
| max_delay_requirement      | 1.5 seconds      | Maximum acceptable delay                              |
| poisson_interarrival       | 6 seconds        | Average time between task arrivals                    |
| active_period              | 3600 seconds     | App is active for 1 hour                              |
| idle_period                | 1 second         | Idle time between tasks                               |
| data_upload / download     | 10 MB / 15 MB    | Data size per task                                    |
| task_length                | 1500 MI          | Million Instructions per task                         |
| required_core              | 1                | CPU cores needed per task                             |
| vm_utilization_on_edge     | 0                | Edge not used in this config (can be modified)        |
| vm_utilization_on_cloud    | 1                | Cloud is fully utilized                               |
| vm_utilization_on_mobile   | 3                | High resource use if processed on mobile              |

---

## 🔁 Simulation Parameters

| Parameter                    | Value             |
|-----------------------------|-------------------|
| simulation_time             | 60 minutes        |
| warm_up_period              | 3 minutes         |
| file_log_enabled            | true              |
| deep_file_log_enabled       | false             |
| min_number_of_devices       | 100               |
| max_number_of_devices       | 500               |
| device_counter_step         | 100               |
| vm_load_check_interval      | 0.025 seconds     |
| location_check_interval     | 0.005 seconds     |
| ap_delay_check_interval     | 0.1 seconds       |

---

## 🧠 Orchestrator Policies Compared

The simulation tests multiple **orchestrator policies** to decide execution location:

| Policy         | Description |
|----------------|-------------|
| `RANDOM`       | Randomly selects Edge or Cloud each time |
| `PREDICTIVE`   | Chooses based on system performance/load prediction |
| `GAME_THEORY`  | Optimizes choice for both user and system using game theory |
| `AI_BASED`     | AI-powered decision making using system/historical data |

---

## 📊 Dashboard & Result Visualization

A custom **interactive dashboard** was developed using:

- **Python (Matplotlib, Pandas)**: to extract and process simulation results
- **JavaScript (Chart.js)**: to visualize metrics dynamically per policy

You can view simulation metrics like:
- Average service time
- Failed Tasks Percentage
- Average Processing Time
- Average Network Delay

➡️ Live Dashboard:  
[https://ramamhallla.github.io/Edge-Cloud-Performance-Dashboard/](https://ramamhallla.github.io/Edge-Cloud-Performance-Dashboard/)


## 📌 Notes

- This project represents a comprehensive case study focused on **evaluating resource allocation strategies between Edge and Cloud infrastructures within real-time smart healthcare systems**.
- It was implemented and tested using **Eclipse**, **Java 8+**, and **EdgeCloudSim** modified configuration files.


## 👩‍💻 Author

Rama Mhallla  
Vincenzo Damico

MSc in Telecommunication Engineering – University of Calabria  
[GitHub Profile](https://github.com/RamaMhallla)
