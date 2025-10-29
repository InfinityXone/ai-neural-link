from agents.agent_base import AgentBase
import subprocess
import time

class ResurrectorAgent(AgentBase):
    def __init__(self):
        super().__init__("ResurrectorAgent")
        self.targets = [
            "gateway.py",
            "agents/healers/self_heal_agent.py",
            "agents/watchers/resurrector_agent.py",
        ]

    def process_running(self, target: str) -> bool:
        try:
            out = subprocess.check_output(["pgrep", "-f", target]).decode().split()
            return len(out) > 0
        except subprocess.CalledProcessError:
            return False

    def restart_process(self, target: str):
        self.log(f"Attempting restart of {target}")
        try:
            subprocess.Popen(
                ["python3", target],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            self.log(f"✅ Restarted {target}")
        except Exception as e:
            self.log(f"❌ Failed to restart {target}: {e}", level="ERROR")

    def run(self):
        self.log("👁️ Resurrector loop active")
        while True:
            self.heartbeat()
            for t in self.targets:
                if not self.process_running(t):
                    self.log(f"⚠️ {t} is down — restarting")
                    self.restart_process(t)
            time.sleep(30)

if __name__ == "__main__":
    agent = ResurrectorAgent()
    agent.safe_run()
