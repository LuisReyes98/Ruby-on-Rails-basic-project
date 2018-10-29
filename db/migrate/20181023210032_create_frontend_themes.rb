class CreateFrontendThemes < ActiveRecord::Migration[5.2]
  def change
    create_table :frontend_themes do |t|
      t.string :name
      t.string :description
      t.string :image_name
      
      t.timestamps
    end
  end
end
