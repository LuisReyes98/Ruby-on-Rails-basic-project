require 'test_helper'

class Frontend::CriticsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @frontend_critic = frontend_critics(:one)
  end

  test "should get index" do
    get frontend_critics_url
    assert_response :success
  end

  test "should get new" do
    get new_frontend_critic_url
    assert_response :success
  end

  test "should create frontend_critic" do
    assert_difference('Frontend::Critic.count') do
      post frontend_critics_url, params: { frontend_critic: { description: @frontend_critic.description, score: @frontend_critic.score, theme_id: @frontend_critic.theme_id, title: @frontend_critic.title } }
    end

    assert_redirected_to frontend_critic_url(Frontend::Critic.last)
  end

  test "should show frontend_critic" do
    get frontend_critic_url(@frontend_critic)
    assert_response :success
  end

  test "should get edit" do
    get edit_frontend_critic_url(@frontend_critic)
    assert_response :success
  end

  test "should update frontend_critic" do
    patch frontend_critic_url(@frontend_critic), params: { frontend_critic: { description: @frontend_critic.description, score: @frontend_critic.score, theme_id: @frontend_critic.theme_id, title: @frontend_critic.title } }
    assert_redirected_to frontend_critic_url(@frontend_critic)
  end

  test "should destroy frontend_critic" do
    assert_difference('Frontend::Critic.count', -1) do
      delete frontend_critic_url(@frontend_critic)
    end

    assert_redirected_to frontend_critics_url
  end
end
