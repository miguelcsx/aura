// events/mod.rs
pub mod connection;
pub mod message;
pub mod error;
pub mod ready;

use crate::events::message::handle_message;
use crate::events::ready::on_ready;
use crate::types::{Data, Error};
use poise::serenity_prelude as serenity;

pub async fn handle_event(
    ctx: &serenity::Context,
    event: &serenity::FullEvent,
    framework: poise::FrameworkContext<'_, Data, Error>,
    _data: &Data,
) -> Result<(), Error> {
    match event {
        serenity::FullEvent::Ready { data_about_bot, .. } => {
            on_ready(ctx.clone(), data_about_bot.clone()).await;
        }
        serenity::FullEvent::Message { new_message } => {
            handle_message(ctx, framework, new_message).await?;
        }
        _ => {}
    }
    Ok(())
}
