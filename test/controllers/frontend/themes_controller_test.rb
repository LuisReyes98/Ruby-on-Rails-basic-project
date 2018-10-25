require 'test_helper'

class Frontend::ThemesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @frontend_theme = frontend_themes(:one)
  end

  test "should get index" do
    get frontend_themes_url
    assert_response :success
  end

  test "should get new" do
    get new_frontend_theme_url
    assert_response :success
  end

  test "should create frontend_theme" do
    assert_difference('Frontend::Theme.count') do
      post frontend_themes_url, params: { frontend_theme: { description: @frontend_theme.description, name: @frontend_theme.name } }
    end

    assert_redirected_to frontend_theme_url(Frontend::Theme.last)
  end

  test "should show frontend_theme" do
    get frontend_theme_url(@frontend_theme)
    assert_response :success
  end

  test "should get edit" do
    get edit_frontend_theme_url(@frontend_theme)
    assert_response :success
  end

  test "should update frontend_theme" do
    patch frontend_theme_url(@frontend_theme), params: { frontend_theme: { description: @frontend_theme.description, name: @frontend_theme.name } }
    assert_redirected_to frontend_theme_url(@frontend_theme)
  end

  test "should destroy frontend_theme" do
    assert_difference('Frontend::Theme.count', -1) do
      delete frontend_theme_url(@frontend_theme)
    end

    assert_redirected_to frontend_themes_url
  end
end
