class Frontend::Theme < ApplicationRecord
	has_many :critics , class_name: "Frontend::Critic", through: :theme_id
	
	validates :name,presence: true
	#validates :name,presence: true,uniqueness: true
	validates :description,presence: true, length: {minimum: 20}
end
