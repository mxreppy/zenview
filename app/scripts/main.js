/* jshint -W097 */
/* global require */
'use strict';

var angular = require('angular'); // That's right! We can just require angular as if we were in node

var HomeCtrl = require('./controllers/home.js');

var app = angular.module('myApp', []);

app.controller('HomeCtrl',['$scope', HomeCtrl]);
