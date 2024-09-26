// discord/src/services/api_client.rs

use reqwest::Client;
use crate::config::settings::get_config;
use std::error::Error;


pub async fn get(endpoint: &str) -> Result<String, Box<dyn Error>> {
    // Get the configuration
    let config = get_config();

    // Construct the URL
    let url = format!("{}/{}", config.api_url, endpoint);

    // Create a new reqwest client
    let client = Client::new();

    // Send a GET request to the API
    let response = client.get(&url)
        .header("Authorization", &config.discord_token)
        .send()
        .await?;

    if response.status().is_success() {
        let body = response.text().await?;
        Ok(body)
    } else {
        Err("Failed to get data".into())
    }
}

