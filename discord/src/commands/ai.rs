// commands/llm.rs

use crate::services::api_client;
use crate::types::{Context, Error};
use crate::command_with_auth;

async fn ask_output(question: String) -> Result<String, Error> {
    let body = serde_json::json!({
        "prompt": question
    });
    match api_client::post("ai/chat/ask/", &body).await {
        Ok(data) => {
            Ok(data.to_string())
        }
        Err(e) => {
            Err(format!("Error: {}", e).into())
        }
    }
}

// Ask the AI a question
async fn ask_handler(
    ctx: Context<'_>, question: String) -> Result<(), Error> {
    match ask_output(question).await {
        Ok(data) => {
            ctx.say(data).await?;
        }
        Err(e) => {
            ctx.say(format!("Error: {}", e)).await?;
        }
    }
    Ok(())
}

command_with_auth!(ask, ask_handler, question: String);
