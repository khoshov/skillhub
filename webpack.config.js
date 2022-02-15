const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const StylelintPlugin = require('stylelint-webpack-plugin');

module.exports = {
    context: __dirname,
    entry: {
        main: './assets/js/index',
        vendor: './assets/js/vendor'
    },
    output: {
        path: path.resolve('./assets/webpack_bundles/'),
        filename: "[name]-[fullhash].js",
        clean: true
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new StylelintPlugin({fix: true, failOnError: false})
    ],
    module: {
        rules: [
            {
                test: /\.s[ac]ss$/i,
                use: [{
                    loader: 'style-loader',
                }, {
                    loader: 'css-loader',
                }, {
                    loader: 'postcss-loader',
                    options: {
                        postcssOptions: {
                            plugins: function () {
                                return [
                                    require('autoprefixer')
                                ];
                            }
                        }
                    }
                }, {
                    loader: 'sass-loader'
                }]
            },
        ],
    },
}
