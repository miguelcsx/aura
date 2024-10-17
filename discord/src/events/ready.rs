// events/ready.rs

use poise::serenity_prelude::{Context, Ready};

// This function is called when the bot is ready to start receiving events
pub async fn on_ready(_ctx: Context, ready: Ready) {
    println!("{} is connected!", ready.user.name);
}
