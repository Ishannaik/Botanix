document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then(function(userCredential) {
            var user = userCredential.user;
            // Additional code to handle successful sign-up
            // For example, you could redirect the user to a welcome page.
        })
        .catch(function(error) {
            var errorCode = error.code;
            var errorMessage = error.message;
            // Handle errors here (e.g., display an error message to the user)
        });
});
