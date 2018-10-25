require "application_system_test_case"

class Frontend::CriticsTest < ApplicationSystemTestCase
  setup do
    @frontend_critic = frontend_critics(:one)
  end

  test "visiting the index" do
    visit frontend_critics_url
    assert_selector "h1", text: "Frontend/Critics"
  end

  test "creating a Critic" do
    visit frontend_critics_url
    click_on "New Frontend/Critic"

    fill_in "Description", with: @frontend_critic.description
    fill_in "Score", with: @frontend_critic.score
    fill_in "Theme", with: @frontend_critic.theme_id
    fill_in "Title", with: @frontend_critic.title
    click_on "Create Critic"

    assert_text "Critic was successfully created"
    click_on "Back"
  end

  test "updating a Critic" do
    visit frontend_critics_url
    click_on "Edit", match: :first

    fill_in "Description", with: @frontend_critic.description
    fill_in "Score", with: @frontend_critic.score
    fill_in "Theme", with: @frontend_critic.theme_id
    fill_in "Title", with: @frontend_critic.title
    click_on "Update Critic"

    assert_text "Critic was successfully updated"
    click_on "Back"
  end

  test "destroying a Critic" do
    visit frontend_critics_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Critic was successfully destroyed"
  end
end
