'use strict';

var HomeCtrl = function($scope, $http, $location, $routeParams) {

  $http.get('/api/zendesk/ticket/').success(function(data) {
    $scope.tickets = data.tickets;
  });

  // todo: move to ticket detail ctrl
  $scope.ticketId = $routeParams.ticketId;

  $scope.ticketDetails = function(ticketId) {
    console.log(ticketId);
    $location.path('ticket-detail/'+ticketId); // path not hash
  }
};

module.exports = HomeCtrl;