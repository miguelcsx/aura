// config/settings.rs

use dotenv::dotenv;
use once_cell::sync::OnceCell;
use std::env;

#[derive(Debug, Clone)]
pub struct Config {
    pub api_url: String,
    pub discord_token: String,
}

// Initialize a static instance of the configuration
static CONFIG: OnceCell<Config> = OnceCell::new();

pub fn load_config() {
    // Load the configuration from the environment
    dotenv().ok();

    let api_url = env::var("API_URL").expect("API_URL must be set");
    let discord_token = env::var("DISCORD_TOKEN").expect("DISCORD_TOKEN must be set");

    let config = Config {
        api_url,
        discord_token,
    };

    // Set the configuration
    CONFIG.set(config).expect("Failed to set configuration");
}

pub fn get_config() -> &'static Config {
    CONFIG.get().expect("Configuration not loaded")
}
