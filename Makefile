.PHONY: all aura discord

all: aura discord

# Load environment variables
load-env:
	@if [-f .env]; then \
		export $(cat .env | xargs); \
	else \
		echo "No .env file found"; \
	fi

# Build Aura
aura:
	@$(MAKE) load-env
	@echo "Starting Aura..."
	(python -m aura) & # Run Aura in the background

discord:
	@echo "Starting Discord..."
	@cd discord && cargo build && cargo run
