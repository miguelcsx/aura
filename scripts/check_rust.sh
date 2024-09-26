#!/bin/sh

# Change to the discord directory
cd discord || {
    echo "Directory 'discord' does not exist."
    exit 1
}

# Set up Rust environment (assuming Rust is already installed)
rust_version="1.57.0"

# Optionally install Rustup (uncomment if needed)
# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Install Rust components
rustup component add rustfmt clippy

# Check for Rust errors
cargo check --all

# Run Rustfmt
cargo fmt --all -- --check

# Run Clippy
cargo clippy --all -- -D warningss
