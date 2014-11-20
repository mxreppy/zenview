/* jshint -W097 */
/* global require */
'use strict';

var angular = require('angular'); // That's right! We can just require angular as if we were in node
require('angular-router-browserify')(angular);

var HomeCtrl = require('./controllers/home.js');
var app = angular.module('myApp', ['ngRoute']);

app.config(function($routeProvider){
  $routeProvider.when("/",
    {
      templateUrl: "./views/ticket-list.html",
      controller: "HomeCtrl"
    }
  ).when("/ticket-detail/:ticketId",
    {
      templateUrl: "./views/ticket-detail.html",
      controller: "HomeCtrl"
    }
  ).otherwise({
        redirectTo: '/'
      });
});
app.controller('HomeCtrl',['$scope', '$http', '$location', '$routeParams', HomeCtrl]);
