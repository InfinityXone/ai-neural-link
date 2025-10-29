import json

def aggregate_data():
    try:
        with open("swarm_metrics.json", "r") as f:
            data = json.load(f)
            print(f"[AGGREGATE] {len(data['active_agents'])} agents reporting.")
    except Exception as e:
        print(f"[ERROR] Could not load metrics: {str(e)}")

if __name__ == "__main__":
    aggregate_data()
