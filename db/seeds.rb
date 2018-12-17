# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
user = User.create(email: 'admin@admin.com' , password: 'admin123')
user.save

Frontend::Theme.create(name: 'Libros',description: 'Libros, Revistas, Comics y demas...')
Frontend::Theme.create(name: 'Restaurantes',description: 'Comidas, Ubicación y Atención al servicio')
Frontend::Theme.create(name: 'Peliculas',description: 'Ultimos Exitos de Hollywood y cine Internacional')

Frontend::Critic.create(score: 10 ,title: 'Avengers 4',description: 'Mejor pelicula del siglo' , theme_id: 3)
Frontend::Critic.create(score: 5 ,title: 'X-Men 2',description: 'Regular' , theme_id: 3)