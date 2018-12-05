class Frontend::Critic < ApplicationRecord
	belongs_to :theme 

	validates :title,presence: true
	validates :description,presence: true, length: {minimum: 20}
	validates :score,presence: true , :inclusion => 0..10
	validates :theme_id,presence: true
end
