// services/api_client.rs

use crate::config::settings::get_config;
use anyhow::{Result, Context};
use reqwest::Client;
use serde_json::Value;

pub async fn get(endpoint: &str) -> Result<String> {
    let config = get_config();

    // Construct the URL
    let url = format!("{}/{}", config.api_url, endpoint);

    let client = Client::new();

    // Send a GET request to the API
    let response = client
        .get(&url)
        .header("Authorization", &config.discord_token)
        .send()
        .await
        .with_context(|| format!("Failed to send request to {url}"))?;

    if response.status().is_success() {
        let body = response
            .text()
            .await
            .with_context(|| "Failed to parse response body")?;

        // Parse the JSON response
        let json: Value = 
            serde_json::from_str(&body).with_context(|| "Failed to parse JSON response")?;
        
        // Extract the message
        if let Some(message) = json.get("message").and_then(Value::as_str) {
            Ok(message.to_string())
        } else {
            Err(anyhow::anyhow!("No message found in response"))
        }
    } else {
        Err(anyhow::anyhow!(
            "API request failed with status: {}",
            response.status()
        ))
    }
}
