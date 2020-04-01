// vue.config.js
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: "http://0.0.0.0:8080/",
  outputDir: "./dist/",
  devServer: {
    headers: {
      "Access-Control-Allow-Origin": ["*"]
    }
  },
  configureWebpack: {
    plugins: [new BundleTracker({ filename: "./webpack-stats.json" })],
    optimization: {
      splitChunks: false
    }
  }
};
