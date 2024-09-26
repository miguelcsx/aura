mod config;
mod services;

use config::settings;
use services::api_client;

#[tokio::main(flavor = "current_thread")]
async fn main() {
    // Load the configuration
    settings::load_config();

    // Get the configuration
    let config = settings::get_config();

    // Print the configuration
    println!("API URL: {}", config.api_url);
    println!("Discord Token: {}", config.discord_token);

    // Get data from the API
    match api_client::get("").await {
        Ok(response) => println!("Response: {}", response),
        Err(err) => eprintln!("Error: {}", err),
    }
}
