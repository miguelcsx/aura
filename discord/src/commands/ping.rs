// commands/ping.rs

use crate::services::api_client;
use crate::types::{Context, Error};
use anyhow::Result;

// Fetch data from the `/ping` endpoint
#[poise::command(slash_command, prefix_command)]
pub async fn ping(ctx: Context<'_>) -> Result<(), Error> {
    // Call the API client to make a GET request to `/ping`
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
