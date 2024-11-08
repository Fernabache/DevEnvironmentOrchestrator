# DevEnvironmentOrchestrator
To use this repository:

Clone and install:
git clone https://github.com/username/dev-environment-orchestrator.git
cd dev-environment-orchestrator
pip install -e .

Basic usage

from dev_orchestrator import DevEnvironmentOrchestrator

orchestrator = DevEnvironmentOrchestrator("./my-project")
orchestrator.initialize_workspace()
orchestrator.watch_changes()

Development setup:
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Build package
python -m build
