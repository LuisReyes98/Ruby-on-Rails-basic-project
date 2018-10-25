Rails.application.routes.draw do
  

  namespace :frontend , path: '/' do
    resources :critics, :themes
  end
  root 'views#index'
  get '/home' , to: 'views#index'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
