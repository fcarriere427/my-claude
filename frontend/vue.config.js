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
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
};
