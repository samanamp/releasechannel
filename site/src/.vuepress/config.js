const { description } = require('../../package')
const axios = require('axios');
const sidebar = require('vuepress-auto-sidebar')
const dirTree = require('directory-tree');
const path = require('path');

var applications = [];
dirTree(path.join(__dirname, '../applications'), {extensions:/\.md/}, (item, PATH) => applications.push(item));
applications = applications.map(children => {
    return path.parse(children.name).name  !== 'README' ? path.join.apply(null, children.path.split(path.sep).slice(7)) : path.join.apply(null, children.path.split(path.sep).slice(7)).replace('README.md', '');
});
module.exports = {
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  title: 'Release Channel',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#description
   */
  description: description,
  

  /**
   * Extra tags to be injected to the page HTML `<head>`
   *
   * ref：https://v1.vuepress.vuejs.org/config/#head
   */
  head: [
    ['meta', { name: 'theme-color', content: '#3eaf7c' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }]
  ],

  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    searchPlaceholder: 'Search app...',
    smoothScroll: true,
    repo: '',
    editLinks: false,
    docsDir: '',
    editLinkText: '',
    nextLinks: false,
    prevLinks: false,
    lastUpdated: false,
    nav: [
      {
        text: 'Applications',
        link: '/applications/'
      },
      {
        text: 'GitHub Source',
        link: 'https://github.com/samanamp/releasechannel.git'
      }
    ],
    sidebar: {
      '/applications/': applications
    }
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: [
    '@vuepress/plugin-back-to-top',
    '@vuepress/plugin-medium-zoom',
  ]
}
