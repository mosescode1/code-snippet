// Generated using webpack-cli https://github.com/webpack/webpack-cli

const path = require('path');
const HtmlWebpackPlugin = require("html-webpack-plugin");;
const MiniCssExtractPlugin = require('mini-css-extract-plugin');


const isProduction = process.env.NODE_ENV == 'production';



const config = {
    entry: './src/index.ts',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name]-[contenthash].js',
        clean: true,
        assetModuleFilename: './assets/[name][ext]'
    },

    devServer: {
        open: true,
        static: {
            directory: path.join(__dirname, 'src'), // Set the directory to serve static files from
        },
        port: 3000,
        hot: true,
    },

    plugins: [
        new HtmlWebpackPlugin({
            template: "./src/index.html",
            title: "WebPack tutorial",
            filename: "index.html",
        }),  // Add your plugins here
        // Learn more about plugins from https://webpack.js.org/configuration/plugins/
    ],
    module: {
        rules: [
            {
                test: /\.(ts|tsx)$/i,
                loader: 'ts-loader',
                exclude: ['/node_modules/'],
            },
            // {
            //     test: /\.html$/,
            //     type: "asset/resource",
            //     generator: {
            //         filename: "[name][ext]",
            //     },
            // },
            {
                test: /\.html$/i,
                use: ["html-loader"],
            },
            {
                test: /\.css$/i,
                use: [MiniCssExtractPlugin.loader, 'css-loader'],
            },
            {
                test: /\.(eot|svg|ttf|woff|woff2|png|jpg|gif)$/i,
                type: 'asset/resource',
                generator: {
                    filename: "./assets/[name][ext]"
                }

            },

            // Add your rules for custom modules here
            // Learn more about loaders from https://webpack.js.org/loaders/
        ],
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.jsx', '.js', '...'],
    },
    devtool: false,
};

module.exports = () => {
    if (isProduction) {
        config.mode = 'production';

        config.plugins.push(new MiniCssExtractPlugin({

            filename: './styles/[name].css',  // For entry point CSS files
        }));


    } else {
        config.mode = 'development';
        config.plugins.push(new MiniCssExtractPlugin({

            filename: './styles/[name].css',  // For entry point CSS files
        }));
    }
    return config;
};
