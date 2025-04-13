module.exports = {
  productionSourceMap: false,
  // Options pour optimiser la taille du bundle
  chainWebpack: config => {
    config.optimization.minimizer('terser').tap(args => {
      const { terserOptions } = args[0];
      terserOptions.compress.drop_console = true;
      return args;
    });
  },
  // Configuration du serveur de développement
  devServer: {
    port: 8080,
    proxy: {
      '/api': {
        target: process.env.VUE_APP_API_URL || 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': '/api',
        },
      },
    },
  },
};
