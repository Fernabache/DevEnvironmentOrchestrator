
from dev_orchestrator import DevEnvironmentOrchestrator

# Initialize orchestrator
orchestrator = DevEnvironmentOrchestrator("./my-project")

# Initialize workspace with default template
orchestrator.initialize_workspace()

# Start watching for changes
orchestrator.watch_changes()

# Sync environments
orchestrator.sync_environment("development", "staging")

# Learn patterns
patterns = orchestrator.learn_patterns()
print("Learned patterns:", patterns)

# examples/advanced_patterns.py

from dev_orchestrator import DevEnvironmentOrchestrator
from pathlib import Path

def setup_complex_workspace():
    """Example of setting up a complex workspace"""
    
    # Initialize with microservices template
    orchestrator = DevEnvironmentOrchestrator("./microservices-project")
    orchestrator.initialize_workspace(template="microservices")
    
    # Configure multiple environments
    environments = ["development", "staging", "production"]
    
    for env in environments:
        env_path = Path(f"environments/{env}")
        orchestrator.initialize_workspace(template="microservices", path=env_path)
        
    # Start pattern learning
    orchestrator.watch_changes()
    
    # Wait for patterns to emerge
    import time
    time.sleep(3600)  # Wait an hour
    
    # Analyze patterns
    patterns = orchestrator.learn_patterns()
    
    # Apply learned patterns
    for env in environments:
        orchestrator.apply_patterns(env, patterns)

if __name__ == "__main__":
    setup_complex_workspace()
