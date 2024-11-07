// events/message.rs
use poise::serenity_prelude as serenity;
use poise::FrameworkContext;
use crate::types::{Error, Data};


pub async fn handle_message(
    _ctx: &serenity::Context,
    _framework: FrameworkContext<'_, Data, Error>,
    message: &serenity::Message,
) -> Result<(), Error> {
    // Ignore messages that are empty or start with a command prefix
    if message.content.is_empty() || message.content.starts_with("!") || message.content.starts_with("/") {
        println!("Ignoring message: {}", message.content);
        return Ok(());
    }
    Ok(())
}
