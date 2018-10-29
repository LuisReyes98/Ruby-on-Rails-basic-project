class CreateFrontendCritics < ActiveRecord::Migration[5.2]
  def change
    create_table :frontend_critics do |t|
      t.integer :score
      t.string :title
      t.string :description
      t.integer :theme_id
      t.integer :user_id

      t.timestamps
    end
  end
end
