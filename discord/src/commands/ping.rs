// commands/ping.rs
use crate::services::api_client;
use crate::types::{Context, Error};
use crate::command_with_auth;
use anyhow::Result;

async fn ping_handler(ctx: Context<'_>) -> Result<(), Error> {
    match api_client::get("ping").await {
        Ok(data) => {
            ctx.say(data.to_string()).await?;
        }
        Err(e) => {
            ctx.say(format!("Error: {}", e)).await?;
        }
    }
    Ok(())
}

command_with_auth!(ping, ping_handler);
