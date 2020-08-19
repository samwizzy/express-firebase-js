const path = require('path')

module.exports = {
    mode: 'development',
    entry: './app.js',
    devtool: 'inline-source-map',
    devServer: {
        contentBase: path.join(__dirname + '/public', 'dist'),
        compress: true,
        port: 8080
    },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname + '/public', 'dist'),
        publicPath: '/'
    },
    performance: {
        hints: false
    }
}

