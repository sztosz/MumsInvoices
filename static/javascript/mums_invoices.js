(function () {
  'use strict';

  angular
    .module('mums_invoices', [
      'mums_invoices.config',
      'mums_invoices.routes',
      'mums_invoices.authentication',
      'mums_invoices.layout',
    ]);

  angular
    .module('mums_invoices.config', []);

  angular
    .module('mums_invoices.routes', ['ngRoute']);

  angular
    .module('mums_invoices')
    .run(run);

  run.$inject = ['$http'];

  /**
   * @name run
   * @desc Update xsrf $http headers to align with Django's defaults
   */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }

})();


