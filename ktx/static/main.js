(function () {
	'use strict';
	
	angular.module('KTX', [])
	.controller('KTXController', ['$scope', '$log', '$http', function($scope, $log, $http) {
		// Can use either HTTP or API
		// the angular-flask example uses API
		// here I will use HTTP for learning purpose
		$scope.user = { username: '', password: '' };
		$scope.message = '';
		
		$scope.login = function() {
			$log.log('login');
			
			$http.post('/logmein', { 'username': $scope.user.username, 'password': $scope.user.password })
			.success(function(results) { 
				$log.log(results); 
				$scope.message = results;
			})
			.error(function(error) { $log.log(error); });
		}
	}]);
}());