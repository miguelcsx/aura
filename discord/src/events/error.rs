// events/error.rs

use poise;
use crate::types::{Data, Error};

pub async fn on_error(error: poise::FrameworkError<'_, Data, Error>) {
    match error {
        poise::FrameworkError::Setup {error, ..} => {
            panic!("Failed to start bot: {:?}", error);
        }
        poise::FrameworkError::Command {error, ctx, ..} => {
            println!("Error in command `{}`: {:?}", ctx.command().name, error);
        } 
        error => {
            if let Err(e) = poise::builtins::on_error(error).await {
                panic!("Error in built-in error handler: {:?}", e);
            }
        }
    }
}
