// main.rs

mod cli;
mod commands;
mod config;
mod events;
mod services;
mod types;

use crate::config::settings::{load_config, get_config};
use crate::events::handle_event;
use crate::events::error::on_error;
use poise::serenity_prelude::{self as serenity, GatewayIntents};
use types::Data;

#[tokio::main(flavor = "current_thread")]
async fn main() {
    load_config();
    let config = get_config();
    let token = &config.discord_token;

    // Set up intents for advanced features
    let intents = GatewayIntents::GUILD_MESSAGES
        | GatewayIntents::MESSAGE_CONTENT
        | GatewayIntents::GUILD_MESSAGE_REACTIONS
        | GatewayIntents::GUILD_MEMBERS;

    // Define the bot framework
    let framework = poise::Framework::builder()
        .setup(|ctx, _ready, framework| {
            Box::pin(async move {
                poise::builtins::register_globally(ctx, &framework.options().commands).await?;
                Ok(Data {})
            })
        })
        .options(poise::FrameworkOptions {
            // event handlers for the bot (e.g. on_ready, on_message, which are in the events module)
            event_handler: |ctx, event, framework, data| {
                Box::pin(async move {
                    handle_event(ctx, event, framework, data).await?;
                    Ok(())
                })
            },
            commands: vec![commands::ping::ping()],
            on_error: |error| Box::pin(on_error(error)),
            ..Default::default()
        })
        .build();

    let client = serenity::ClientBuilder::new(token, intents)
        .framework(framework)
        .await;
    client.unwrap().start().await.unwrap();
}
