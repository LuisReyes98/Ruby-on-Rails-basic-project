require "application_system_test_case"

class Frontend::ThemesTest < ApplicationSystemTestCase
  setup do
    @frontend_theme = frontend_themes(:one)
  end

  test "visiting the index" do
    visit frontend_themes_url
    assert_selector "h1", text: "Frontend/Themes"
  end

  test "creating a Theme" do
    visit frontend_themes_url
    click_on "New Frontend/Theme"

    fill_in "Description", with: @frontend_theme.description
    fill_in "Name", with: @frontend_theme.name
    click_on "Create Theme"

    assert_text "Theme was successfully created"
    click_on "Back"
  end

  test "updating a Theme" do
    visit frontend_themes_url
    click_on "Edit", match: :first

    fill_in "Description", with: @frontend_theme.description
    fill_in "Name", with: @frontend_theme.name
    click_on "Update Theme"

    assert_text "Theme was successfully updated"
    click_on "Back"
  end

  test "destroying a Theme" do
    visit frontend_themes_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Theme was successfully destroyed"
  end
end
