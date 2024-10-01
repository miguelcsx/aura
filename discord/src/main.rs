// main.rs

mod types;
mod commands;
mod config;
mod services;

use types::Data;
use poise::serenity_prelude as serenity;
use crate::config::settings::{load_config, get_config};

#[tokio::main(flavor = "current_thread")]
async fn main() {
    // Load the configuration
    load_config();
    let config = get_config();
    let token = &config.discord_token;

    // Set up intents
    let intents = serenity::GatewayIntents::non_privileged();

    // Define the bot framework
    let framework = poise::Framework::builder()
        .options(poise::FrameworkOptions {
            commands: vec![
                commands::ping::ping(),
            ],
            ..Default::default()
        })
        .setup(|ctx, _ready, framework| {
            Box::pin(async move {
                poise::builtins::register_globally(ctx, &framework.options().commands).await?;
                Ok(Data {})
            })
        })
        .build();

        let client = serenity::ClientBuilder::new(token, intents)
            .framework(framework)
            .await;
        client.unwrap().start().await.unwrap();
}
