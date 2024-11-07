// services/api_client.rs

use crate::config::settings::get_config;
use anyhow::{Context, Result};
use reqwest::{Client, Response};
use serde_json::Value;


async fn handle_response(response: Response) -> Result<String> {
    let status = response.status();
    
    if status.is_success() {
        let body = response
            .text()
            .await
            .context("Failed to parse response body")?;
            
        // Try to parse the response as JSON
        let json: Value = serde_json::from_str(&body).context("Failed to parse JSON response")?;
            
        // If it's a message response, extract the message
        if let Some(message) = json.get("message").and_then(Value::as_str) {
            Ok(message.to_string())
        } else {
            // If it's not a message response, return the entire JSON body
            Ok(body)
        }
    } else if status.as_u16() == 404 {
        Err(anyhow::anyhow!("Not found"))
    } else {
        Err(anyhow::anyhow!(
            "API request failed with status: {}",
            status
        ))
    }
}

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
        .context(format!("Failed to send GET request to {}", url))?;
    handle_response(response).await
}


pub async fn post(endpoint: &str, body: &Value) -> Result<String> {
    let config = get_config();
    let url = format!("{}/{}", config.api_url, endpoint);
    let client = Client::new();

    let response = client
        .post(&url)
        .header("Authorization", &config.discord_token)
        .json(body)
        .send()
        .await
        .context(format!("Failed to send POST request to {}", url))?;

    handle_response(response).await
}
