// events/connection.rs
use crate::services::registration;
use crate::types::{Context, Error};
use anyhow::Result;
use poise::serenity_prelude as serenity;

#[derive(Debug, poise::Modal)]
struct RegistrationModal {
    #[name = "Email"]
    email: String,
    #[name = "Role (student/assistant/teacher)"]
    #[placeholder = "Enter your role"]
    role: String,
}

pub async fn handle_user_connection(ctx: Context<'_>) -> Result<(), Error> {
    // Get the user's Discord ID and username
    let discord_id = ctx.author().id.to_string();
    let username = ctx.author().name.clone();

    // Check if the user already exists in the database
    match registration::get_user_by_discord_id(&discord_id).await? {

        Some(_) => {
            // User already exists, no need to show registration modal
            println!("User with discord ID {} already exists", discord_id);
            Ok(())
        }
        None => {
            // If the user does not exist, proceed with registration
            let reply = {
                let components = vec![serenity::CreateActionRow::Buttons(vec![
                    serenity::CreateButton::new("register_modal")
                        .label("Register")
                        .style(serenity::ButtonStyle::Success),
                ])];
                poise::CreateReply::default()
                    .content("Please click the button below to register")
                    .components(components)
            };

            ctx.send(reply).await?;

            // Wait for button interaction
            if let Some(mci) = serenity::ComponentInteractionCollector::new(ctx.serenity_context())
                .timeout(std::time::Duration::from_secs(300)) // 5 minutes timeout
                .filter(move |mci| mci.data.custom_id == "register_modal")
                .await
            {
                // Execute modal when button is clicked
                let data = poise::execute_modal_on_component_interaction::<RegistrationModal>(
                    ctx,
                    mci,
                    None,
                    None,
                )
                .await?;

                // Ensure we have data from the modal
                if let Some(modal_data) = data {
                    // Validate role
                    let valid_roles = ["student", "assistant", "teacher"];
                    if !valid_roles.contains(&modal_data.role.to_lowercase().as_str()) {
                        return Err(Error::from(anyhow::anyhow!("Invalid role selected")));
                    }

                    // Create user
                    match registration::create_user(
                        &username,
                        &modal_data.email,
                        &modal_data.role.to_lowercase(),
                        &discord_id,
                    )
                    .await
                    {
                        Ok(_) => {
                            println!("User with discord ID {} created", discord_id);
                            Ok(())
                        }
                        Err(e) => Err(Error::from(e)),
                    }
                } else {
                    Err(Error::from(anyhow::anyhow!("No data from modal")))
                }
            } else {
                // Timeout occurred or collector ended
                Ok(())
            }
        }
    }
}
