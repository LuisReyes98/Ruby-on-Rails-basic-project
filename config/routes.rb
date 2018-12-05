Rails.application.routes.draw do
  
  devise_for :users
	
  namespace :frontend , path: '/' do
    resources :critics, :themes
  end
  root 'views#index'
  get '/' , to: 'views#index'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
