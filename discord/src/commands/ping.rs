// commands/ping.rs

use crate::events::connection::handle_user_connection;
use crate::services::api_client;
use crate::types::{Context, Error};
use anyhow::Result;

// Fetch data from the `/ping` endpoint
#[poise::command(slash_command, prefix_command)]
pub async fn ping(ctx: Context<'_>) -> Result<(), Error> {
    
    // Check if the user is already registered
    if let Err(e) = handle_user_connection(ctx).await {
        // Handle error and notify the user
        ctx.say("Error handling user connection").await?;
        return Err(e); // Propagate the error from handle_user_connection
    }

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
