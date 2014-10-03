'use strict';

var HomeCtrl = function($scope, $http) {

  $http.get('/api/zendesk/ticket/').success(function(data) {
    $http.get('/api/zendesk/ticket/' + data.tickets[0].id)
      .success(function(data) {
        $scope.ticket = data;
      });
  });
};

module.exports = HomeCtrl;
