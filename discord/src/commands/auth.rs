// commands/auth.rs

use crate::events::connection::handle_user_connection;
use crate::types::{Context, Error};
use anyhow::Result;

// Wrapper function that handles the authentication check
pub async fn with_auth<'a, F, Fut>(ctx: Context<'a>, f: F) -> Result<(), Error>
where
    F: FnOnce(Context<'a>) -> Fut,
    Fut: std::future::Future<Output = Result<(), Error>> + 'a,
{
    // Check if the user is already registered
    if let Err(e) = handle_user_connection(ctx).await {
        ctx.say("Error handling user connection").await?;
        return Err(e);
    }
    
    // Execute the wrapped command
    f(ctx).await
}

// Macro to reduce boilerplate even further
#[macro_export]
macro_rules! command_with_auth {
    ($name:ident, $cmd:expr $(, $arg:ident : $arg_ty:ty)*) => {
        #[poise::command(slash_command, prefix_command)]
        pub async fn $name(ctx: Context<'_> $(, $arg: $arg_ty)*) -> Result<(), Error> {
            $crate::commands::auth::with_auth(ctx, |ctx| async move {
                $cmd(ctx $(, $arg)*).await
            }).await
        }
    };
}
