class CreateBackendOpinions < ActiveRecord::Migration[5.2]
  def change
    create_table :backend_opinions do |t|
      t.integer :score
      t.integer :critic_id

      t.timestamps
    end
  end
end
