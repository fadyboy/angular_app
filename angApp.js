// declare angular application in closure
(function(){
	var app = angular.module('myApp', []);

	app.controller('myAppController', ['$http', '$scope', function($http, $scope){
		$scope.appKey;
		
		$scope.appKeyValue = function(){
			$http({
				method:'POST',
				url:'http://127.0.0.1:5000/getData',
				headers:{
					'content-Type':'application/json;charset=utf-8',
					'Access-Control-Allow-Origin':'*'
				},
				data:{
					'appKey':$scope.appKey
				}

			})
			.then(function(resp){
				$scope.message = resp.data;
				$scope.appKey = '';
			}, function(resp){
				$scope.err_message = resp.data;
				$scope.appKey = '';
			});

				
		}
	}])

})();