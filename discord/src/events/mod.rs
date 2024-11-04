// events/mod.rs

pub mod error;
pub mod ready;

use crate::events::ready::on_ready;
use crate::types::{Data, Error};
use poise::serenity_prelude as serenity;

pub async fn handle_event(
    ctx: &serenity::Context,
    event: &serenity::FullEvent,
    _framework: poise::FrameworkContext<'_, Data, Error>,
    _data: &Data,
) -> Result<(), Error> {
    match event {
        serenity::FullEvent::Ready { data_about_bot, .. } => {
            on_ready(ctx.clone(), data_about_bot.clone()).await;
        }
        serenity::FullEvent::Message { new_message } => {
            println!("Message received: {:?}", new_message.content);
        }
        // Add more event cases here, e.g. Message, Reaction, etc.
        _ => {}
    }
    Ok(())
}
