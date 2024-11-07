// commands/ping.rs
use crate::services::api_client;
use crate::types::{Context, Error};
use crate::command_with_auth;
use anyhow::Result;


async fn ping_output() -> Result<String, Error> {
    match api_client::get("ping").await {
        Ok(data) => {
            Ok(data.to_string())
        }
        Err(e) => {
            Err(format!("Error: {}", e).into())
        }
    }
}

// Ping server to check if it's alive
async fn ping_handler(ctx: Context<'_>) -> Result<(), Error> {
    match ping_output().await {
        Ok(data) => {
            ctx.say(data).await?;
        }
        Err(e) => {
            ctx.say(format!("Error: {}", e)).await?;
        }
    }
    Ok(())
}

command_with_auth!(ping, ping_handler);
