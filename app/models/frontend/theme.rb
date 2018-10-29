class Frontend::Theme < ApplicationRecord
	has_many :critics , class_name: "Frontend::Critic", through: :theme_id
end
