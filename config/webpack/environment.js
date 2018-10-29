const { environment } = require('@rails/webpacker')
const vue =  require('./loaders/vue')

// const file-loader =  require('./loaders/file-loader')


environment.loaders.append('vue', vue)
// environment.loaders.append('file-loader', file-loader)

module.exports = environment
