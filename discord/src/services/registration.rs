// services/registration.rs

use crate::services::api_client;
use anyhow::{Context, Result};
use serde_json::{json, Value};

pub async fn get_user_by_discord_id(discord_id: &str) -> Result<Option<Value>> {
    let endpoint = format!("user/account/{}", discord_id);
    match api_client::get(&endpoint).await {
        Ok(response) => {
            let json: Value = serde_json::from_str(&response).context("Failed to parse JSON response")?;
            Ok(Some(json))
        }
        Err(e) => {
            if e.to_string().contains("Not found") {
                Ok(None)
            } else {
                Err(e)
            }
        }
    }
}


pub async fn create_user(
    username: &str,
    email: &str,
    role: &str,
    discord_id: &str,
) -> Result<Value> {
    let user_data = json!({
        "username": username,
        "email": email,
        "role": role,
        "discord_id": discord_id,
    });

    // Send the request to create the user
    let user_response = api_client::post("user/", &user_data).await?;
    let user_json: Value = serde_json::from_str(&user_response)
        .context("Failed to parse user creation JSON response")?;

    // Ensure the user was created successfully (i.e., it has an ID)
    if user_json["id"].is_null() {
        return Err(anyhow::anyhow!("User creation failed: no ID returned"));
    }

    // Return the created user JSON for later use
    Ok(user_json)
}
