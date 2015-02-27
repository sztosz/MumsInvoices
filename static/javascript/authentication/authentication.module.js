(function () {
  'use strict';

  angular
    .module('mums_invoices.authentication', [
      'mums_invoices.authentication.controllers',
      'mums_invoices.authentication.services'
    ]);

  angular
    .module('mums_invoices.authentication.controllers', []);

  angular
    .module('mums_invoices.authentication.services', ['ngCookies']);
})();
